import os
import sqlite3
import pandas as pd


def read_data_from_db(file_path):
    conn = sqlite3.connect(file_path)

    try:
        cursor = conn.cursor()

        # Retrieve the first table name from the sqlite_master table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 1")
        result = cursor.fetchone()

        if result is None:
            print("No tables found in the database.")
            conn.close()
            return None

        table_name = result[0]

        # Read the data from the retrieved table
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql_query(query, conn)
        conn.close()
        return data

    except sqlite3.Error as e:
        print(f"An error occurred while reading the database: {e}")
        return None


def load_data(path):
    try:
        _, file_extension = os.path.splitext(path)

        if file_extension == ".csv":
            data = pd.read_csv(path)
        elif file_extension in [".xls", ".xlsx"]:
            data = pd.read_excel(path)
        elif file_extension in [".db", ".sql"]:
            data = read_data_from_db(path)

        else:
            raise ValueError(
                "Unsupported file format. Please provide a CSV, Excel, SQL, or SQLite database file."
            )

        return data

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

    except pd.errors.ParserError:
        print(
            "Error occurred while parsing the file. Please check if the file format is correct."
        )
        return None

    except Exception as e:
        print("An error occurred while loading the data:", str(e))
        return None


def preprocess_data(data):
    # Identify column types
    categorical_columns = data.select_dtypes(include="object").columns
    numerical_columns = data.select_dtypes(include=["int", "float"]).columns

    # Handle missing values in numerical columns
    data[numerical_columns] = data[numerical_columns].fillna(
        data[numerical_columns].mean()
    )

    # Handle missing values in categorical columns
    data[categorical_columns] = data[categorical_columns].fillna(
        data[categorical_columns].mode().iloc[0]
    )

    # Encode categorical features
    encoded_data = pd.get_dummies(data, columns=categorical_columns)

    # Scale numerical features
    scaled_data = (
        encoded_data[numerical_columns] - encoded_data[numerical_columns].mean()
    ) / encoded_data[numerical_columns].std()
    encoded_data[numerical_columns] = scaled_data

    # Rename columns with camel case
    encoded_data.columns = encoded_data.columns.str.replace("_", "")

    return encoded_data
