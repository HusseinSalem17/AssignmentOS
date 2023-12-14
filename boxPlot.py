import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

import tqdm


def visualize_boxplot(data, x_column, y_column):
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
