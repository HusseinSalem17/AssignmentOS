import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


def visualize_individual_column(data, header_name):
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
                #tight_layout() automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
                plt.tight_layout()
                plt.show()
        else:
            print(f"Column '{header_name}' does not exist in the data.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
