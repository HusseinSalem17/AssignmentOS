import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


def visualize_pie_chart(data, column):
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
