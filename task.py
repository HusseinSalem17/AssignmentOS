
import threading
from boxPlot import visualize_boxplot
from histogram import visualize_individual_column
from pieChart import visualize_pie_chart
from scatterPlot import visualize_scatterplot

from utils import load_data, preprocess_data


def main():
    while True:
        try:
            file_path = input("Enter the path to the data file: ")
            data = load_data(file_path)
            print("\nDataFrame:")
            print(data)
            preprocessed_data = preprocess_data(data)

            while True:
                print("\nVisualization Options:")
                print("1. Visualize Histogram ")
                print("2. Visualize Box Plot ")
                print("3. Visualize Scatter Plot ")
                print("4. Visualize Pie Chart ")
                print("5. Exit ")

                choice = int(
                    input(
                        "Enter the number corresponding to the visualization option you want to choose: "
                    )
                )

                if choice == 5:
                    break
                elif choice == 1:
                    try:
                        type = int(
                            input("\nChoose type:\n1. header, 2. column values: ")
                        )
                        if type == 2:
                            data = preprocessed_data
                        elif type != 1:
                            raise ValueError
                    except ValueError:
                        print("Invalid input. Please enter either 1 or 2.")
                        choice = input(
                            "Enter 'exit' to quit or press any key to try again: "
                        )
                        if choice.lower() == "exit":
                            exit()
                    print("\nAvailable Columns:")
                    for i, column in enumerate(data.columns):
                        print(f"{i}. {column}")

                    column_choice = int(
                        input(
                            "Enter the number corresponding to the column you want to visualize: "
                        )
                    )
                    if 0 <= column_choice < len(data.columns):
                        column = data.columns[column_choice]
                        # visualize_individual_column(data, column)
                        # use threading for visualization
                        thread = threading.Thread(
                            target=visualize_individual_column,
                            args=(
                                data,
                                column,
                            ),
                        )
                        thread.start()
                    else:
                        print("Invalid choice. Please try again.")

                    if not try_another_visualization():
                        break
                elif choice == 2:
                    while True:
                        try:
                            type = int(
                                input(
                                    "\nChoose comparison type:\n1. Compare between two headers, 2. Compare between two column values: "
                                )
                            )
                            if type == 2:
                                data = preprocessed_data
                            elif type != 1:
                                raise ValueError
                        except ValueError:
                            print("Invalid input. Please enter either 1 or 2.")
                            choice = input(
                                "Enter 'exit' to quit or press any key to try again: "
                            )
                            if choice.lower() == "exit":
                                exit()
                        print("\nAvailable Columns:")
                        for i, column in enumerate(data.columns):
                            print(f"{i}. {column}")

                        x_column_choice = int(
                            input(
                                "Enter the number corresponding to the x-axis column: "
                            )
                        )
                        y_column_choice = int(
                            input(
                                "Enter the number corresponding to the y-axis column: "
                            )
                        )
                        if 0 <= x_column_choice < len(
                            data.columns
                        ) and 0 <= y_column_choice < len(data.columns):
                            x_column = data.columns[x_column_choice]
                            y_column = data.columns[y_column_choice]
                            # visualize_boxplot(data, x_column, y_column)
                            thread = threading.Thread(
                                target=visualize_boxplot,
                                args=(
                                    data,
                                    x_column,
                                    y_column,
                                ),
                            )
                            thread.start()
                            if not try_another_visualization():
                                break
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == 3:
                    try:
                        type = int(
                            input(
                                "\nChoose comparison type:\n1. Compare between two headers, 2. Compare between two column values: "
                            )
                        )
                        if type == 2:
                            data = preprocessed_data
                        elif type != 1:
                            raise ValueError
                    except ValueError:
                        print("Invalid input. Please enter either 1 or 2.\n")
                    print("\nAvailable Columns:")
                    for i, column in enumerate(data.columns):
                        print(f"{i}. {column}")

                    x_column_choice = int(
                        input("Enter the number corresponding to the x-axis column: ")
                    )
                    y_column_choice = int(
                        input("Enter the number corresponding to the y-axis column: ")
                    )
                    if 0 <= x_column_choice < len(
                        data.columns
                    ) and 0 <= y_column_choice < len(data.columns):
                        x_column = data.columns[x_column_choice]
                        y_column = data.columns[y_column_choice]
                        # visualize_scatterplot(data, x_column, y_column)
                        thread = threading.Thread(
                            target=visualize_scatterplot,
                            args=(
                                data,
                                x_column,
                                y_column,
                            ),
                        )
                        thread.start()
                        if not try_another_visualization():
                            break
                    else:
                        print("Invalid choice. Please try again.")
                elif choice == 4:
                    try:
                        type = int(
                            input("\nChoose type:\n1. header, 2. column values: ")
                        )
                        if type == 2:
                            data = preprocessed_data
                        elif type != 1:
                            raise ValueError
                    except ValueError:
                        print("Invalid input. Please enter either 1 or 2.")
                        choice = input(
                            "Enter 'exit' to quit or press any key to try again: "
                        )
                        if choice.lower() == "exit":
                            exit()
                    print("\nAvailable Columns:")
                    for i, column in enumerate(data.columns):
                        print(f"{i}. {column}")

                    column_choice = int(
                        input(
                            "Enter the number corresponding to the column you want to visualize: "
                        )
                    )
                    if 0 <= column_choice < len(data.columns):
                        column = data.columns[column_choice]
                        # visualize_pie_chart(data, column)
                        thread = threading.Thread(
                            target=visualize_pie_chart,
                            args=(
                                data,
                                column,
                            ),
                        )
                        thread.start()
                        if not try_another_visualization():
                            break
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry != "yes":
                exit()


def try_another_visualization():
    """
    Asks the user if they want to try another visualization.
    Returns True if yes, False otherwise.
    """
    return (
        input("Do you want to try another visualization? (yes/no): ").lower() == "yes"
    )

if __name__ == "__main__":
    main()
