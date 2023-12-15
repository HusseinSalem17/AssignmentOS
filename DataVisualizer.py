import matplotlib.pyplot as plt
import seaborn as sns
import random
from tqdm import tqdm


class DataVisualizer:
    def __init__(self):
        sns.set(style="whitegrid")
        sns.set_palette("husl")

    def visualize_individual_column(self, data, header_name):
        try:
            plt.figure(figsize=(12, 8))

            if header_name in data.columns:
                column_data = data[header_name]

                if column_data.dtype == "object":
                    # Categorical column visualization
                    value_counts = column_data.value_counts()

                    sns.barplot(x=value_counts.index, y=value_counts.values)
                    plt.title(f"{header_name} Histogram")
                    plt.xlabel(header_name)
                    plt.ylabel("Count")

                    # Display value counts on the plot
                    for i, count in enumerate(value_counts.values):
                        plt.text(i, count, str(count), ha="center", va="bottom")

                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()
                    print(f"\nValue counts for column '{header_name}':")
                    print(value_counts)
                else:
                    # Numerical column visualization
                    sns.histplot(
                        column_data,
                        kde=True,
                        color=random.choice(list(sns.color_palette())),
                    )
                    plt.title(f"{header_name} Histogram")
                    plt.xlabel(header_name)
                    plt.ylabel("Frequency")

                    # Display descriptive statistics
                    descriptive_stats = column_data.describe()
                    print(f"\nDescriptive statistics for column '{header_name}':")
                    print(descriptive_stats)
                    plt.tight_layout()
                    plt.show()
            else:
                print(f"Column '{header_name}' does not exist in the data.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def visualize_boxplot(self, data, x_column, y_column):
        try:
            visualization_name = "Boxplot"

            # Display progress bar
            with tqdm(total=len(data)) as pbar:
                plt.figure(figsize=(8, 6))

                if data[x_column].dtype == "object":
                    # Categorical x column and numerical y column
                    unique_x = data[x_column].unique()
                    colors = random.choices(list(sns.color_palette()), k=len(unique_x))

                    sns.boxplot(data=data, x=x_column, y=y_column, palette=colors)
                    plt.title(f"{x_column} vs {y_column} {visualization_name}")
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)

                elif data[y_column].dtype == "object":
                    # Numerical x column and categorical y column
                    unique_y = data[y_column].unique()
                    colors = random.choices(list(sns.color_palette()), k=len(unique_y))

                    sns.boxplot(data=data, x=x_column, y=y_column, palette=colors)
                    plt.title(f"{x_column} vs {y_column} {visualization_name}")
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)

                else:
                    # Numerical x and y columns
                    sns.boxplot(data=data, x=x_column, y=y_column)
                    plt.title(f"{x_column} vs {y_column} {visualization_name}")
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)

                plt.tight_layout()
                plt.show()

                pbar.update(len(data))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def visualize_pie_chart(self, data, column):
        try:
            visualization_type = "Pie Chart"

            # Count the occurrences of each unique value in the column
            value_counts = data[column].value_counts()

            # Get the labels and corresponding counts
            labels = value_counts.index
            counts = value_counts.values

            # Create a pie chart
            plt.figure(figsize=(8, 6))
            plt.pie(
                counts,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90,
                colors=sns.color_palette("Set3"),
            )

            plt.title(f"{column} {visualization_type}")
            plt.axis("equal")
            plt.show()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def visualize_scatterplot(self, data, x_column, y_column):
        visualization_type = "Scatterplot"

        try:
            # Display progress bar
            with tqdm(total=len(data)) as pbar:
                plt.figure(figsize=(8, 6))

                if (
                    data[x_column].dtype == "object"
                    and data[y_column].dtype == "object"
                ):
                    # Categorical x and y columns
                    unique_x = data[x_column].unique()
                    colors = random.choices(list(sns.color_palette()), k=len(unique_x))

                    sns.scatterplot(
                        data=data, x=x_column, y=y_column, hue=x_column, palette=colors
                    )

                elif data[x_column].dtype == "object":
                    # Categorical x column and numerical y column
                    unique_x = data[x_column].unique()
                    colors = random.choices(list(sns.color_palette()), k=len(unique_x))

                    sns.stripplot(
                        data=data, x=x_column, y=y_column, hue=x_column, palette=colors
                    )

                elif data[y_column].dtype == "object":
                    # Numerical x column and categorical y column
                    unique_y = data[y_column].unique()
                    colors = random.choices(list(sns.color_palette()), k=len(unique_y))

                    sns.stripplot(
                        data=data, x=x_column, y=y_column, hue=y_column, palette=colors
                    )

                else:
                    # Numerical x and y columns
                    sns.scatterplot(data=data, x=x_column, y=y_column)

                plt.title(f"{x_column} vs {y_column} {visualization_type}")
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.tight_layout()
                plt.show()

                pbar.update(len(data))

        except Exception as e:
            print(f"An error occurred: {str(e)}")
