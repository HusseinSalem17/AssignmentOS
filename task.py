from DataVisualizer import DataVisualizer
import threading
from search_algorithms import *
import time
from utils import load_data, preprocess_data

data = None
search = None


def load_and_preprocess_data():
    while True:
        try:
            file_path = input("Enter the path to the data file: ")

            # Define a variable to store the loaded data
            loaded_data = None

            # Function to load data in a separate thread
            def load_data_thread():
                nonlocal loaded_data
                global search
                loaded_data, search = load_data(file_path)

            # Start loading data in a separate thread
            load_data_thread = threading.Thread(target=load_data_thread)
            load_data_thread.start()

            # Wait for the data loading thread to finish
            load_data_thread.join()

            # Print the loaded data
            print("\nDataFrame:")
            print(loaded_data)
            global data
            data = loaded_data

            # Use the same thread for preprocessing the loaded data
            res = preprocess_data(loaded_data)
            return res

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry != "yes":
                exit()


def print_available_columns(data):
    print("\nAvailable Columns:")
    for i, column in enumerate(data.columns):
        print(f"{i}. {column}")


def visualize_histogram(preprocessed_data, data_visualizer):
    try:
        data_to_visualize = (
            preprocessed_data
            if int(input("\nChoose type:\n1. header, 2. column values: ")) == 2
            else data
        )
        print_available_columns(data_to_visualize)
        column_choice = int(
            input(
                "Enter the number corresponding to the column you want to visualize: "
            )
        )
        visualize_individual_column(data_to_visualize, column_choice, data_visualizer)
    except ValueError:
        print("Invalid input. Please enter either 1 or 2.")
    if not try_another_visualization():
        exit()


def visualize_box_plot(preprocessed_data, data_visualizer):
    try:
        data_to_visualize = (
            preprocessed_data
            if int(input("\nChoose type:\n1. header, 2. column values: ")) == 2
            else data
        )
        print_available_columns(data_to_visualize)
        x_column_choice = int(
            input("Enter the number corresponding to the x-axis column: ")
        )
        y_column_choice = int(
            input("Enter the number corresponding to the y-axis column: ")
        )
        visualize_boxplot(
            data_to_visualize, x_column_choice, y_column_choice, data_visualizer
        )
    except ValueError:
        print("Invalid input. Please enter either 1 or 2.")
    if not try_another_visualization():
        exit()


def visualize_scatter_plot(preprocessed_data, data_visualizer):
    try:
        data_to_visualize = (
            preprocessed_data
            if int(input("\nChoose type:\n1. header, 2. column values: ")) == 2
            else data
        )
        print_available_columns(data_to_visualize)
        x_column_choice = int(
            input("Enter the number corresponding to the x-axis column: ")
        )
        y_column_choice = int(
            input("Enter the number corresponding to the y-axis column: ")
        )
        visualize_scatterplot(
            data_to_visualize, x_column_choice, y_column_choice, data_visualizer
        )
    except ValueError:
        print("Invalid input. Please enter either 1 or 2.")
    if not try_another_visualization():
        exit()


def visualize_pie_chart_plot(preprocessed_data, data_visualizer):
    try:
        data_to_visualize = (
            preprocessed_data
            if int(input("\nChoose type:\n1. header, 2. column values: ")) == 2
            else data
        )
        print_available_columns(data_to_visualize)
        column_choice = int(
            input(
                "Enter the number corresponding to the column you want to visualize: "
            )
        )
        visualize_pie_chart(data_to_visualize, column_choice, data_visualizer)
    except ValueError:
        print("Invalid input. Please enter either 1 or 2.")
    if not try_another_visualization():
        exit()


def visualize_individual_column(data, column_choice, data_visualizer):
    if 0 <= column_choice < len(data.columns):
        column = data.columns[column_choice]
        data_visualizer.visualize_individual_column(data, column)


def visualize_boxplot(data, x_column_choice, y_column_choice, data_visualizer):
    if 0 <= x_column_choice < len(data.columns) and 0 <= y_column_choice < len(
        data.columns
    ):
        x_column = data.columns[x_column_choice]
        y_column = data.columns[y_column_choice]
        data_visualizer.visualize_boxplot(data, x_column, y_column)


def visualize_scatterplot(data, x_column_choice, y_column_choice, data_visualizer):
    if 0 <= x_column_choice < len(data.columns) and 0 <= y_column_choice < len(
        data.columns
    ):
        x_column = data.columns[x_column_choice]
        y_column = data.columns[y_column_choice]
        data_visualizer.visualize_scatterplot(data, x_column, y_column)


def visualize_pie_chart(data, column_choice, data_visualizer):
    if 0 <= column_choice < len(data.columns):
        column = data.columns[column_choice]
        data_visualizer.visualize_pie_chart(data, column)


def try_another_visualization():
    return (
        input("Do you want to try another visualization? (yes/no): ").lower() == "yes"
    )


def run_search_algorithms(data, search_string):
    # Split content into words
    words = data.split()

    def convert_lower():
        for i in range(len(words)):
            words[i] = words[i].lower()

    thread = threading.Thread(target=convert_lower)
    thread.start()
    thread.join()
    result = []

    # Create threads for each search algorithm
    threads = [
        threading.Thread(target=linear_search, args=(words, search_string, result)),
        threading.Thread(
            target=binary_search, args=(sorted(words), search_string, result)
        ),
        threading.Thread(
            target=jump_search, args=(sorted(words), search_string, result)
        ),
    ]

    # Start the threads
    start_times = [time.time() for _ in threads]
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for i, thread in enumerate(threads):
        thread.join()
        end_time = time.time()
        print(f"{thread.name} finished in {end_time - start_times[i]:.4f} seconds")

    # Print the results
    for res in result:
        print(res)


def search_data(data):
    search_string = input("Enter the search string: ").lower()

    # Run search algorithms in separate threads
    run_search_algorithms(data, search_string)


def main():
    preprocessed_data = load_and_preprocess_data()
    data_visualizer = DataVisualizer()

    while True:
        print("\nMain Menu:")
        print("1. Visualize Data")
        print("2. Search Data")
        print("3. Exit")

        choice = int(input("Enter the number corresponding to your choice: "))

        if choice == 3:
            break
        elif choice == 1:
            visualize_data_menu(preprocessed_data, data_visualizer)
        elif choice == 2:
            search_data(search)
        else:
            print("Invalid choice. Please try again.")


def visualize_data_menu(preprocessed_data, data_visualizer):
    while True:
        print("\nVisualization Options:")
        print("1. Visualize Histogram ")
        print("2. Visualize Box Plot ")
        print("3. Visualize Scatter Plot ")
        print("4. Visualize Pie Chart ")
        print("5. Back to Main Menu ")

        choice = int(
            input(
                "Enter the number corresponding to the visualization option you want to choose: "
            )
        )

        if choice == 5:
            break
        elif choice == 1:
            visualize_histogram(preprocessed_data, data_visualizer)
        elif choice == 2:
            visualize_box_plot(preprocessed_data, data_visualizer)
        elif choice == 3:
            visualize_scatter_plot(preprocessed_data, data_visualizer)
        elif choice == 4:
            visualize_pie_chart_plot(preprocessed_data, data_visualizer)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


def print_available_columns(data):
    print("\nAvailable Columns:")
    for i, column in enumerate(data.columns):
        print(f"{i}. {column}")
