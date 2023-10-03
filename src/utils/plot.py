import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tabulate import tabulate

# Setting the style
sns.set_theme(style="ticks", palette="pastel")
sns.set(font_scale=0.8)


def compute_stats_count(train, field, counting=False):
    """
    Compute statistics for counting occurrences of values in a given field of the provided DataFrame.

    Args:
    - train (pd.DataFrame): DataFrame containing the data.
    - field (str): The column name for which statistics are computed.
    - counting (bool, optional): If True, computes count and percentage of occurrences.
                                 If False, computes raw values and percentage of contribution.
                                 Defaults to False.

    Returns:
    - list of tuples: A list of tuples containing (value, count, percentage) statistics.
    """
    count, index, perc = [], [], []

    if counting:
        # Compute count of occurrences for each unique value in the specified field
        count = train[field].value_counts().values
        index = train[field].value_counts().index
        perc = train[field].value_counts().values / len(train[field]) * 100
    else:
        # Use raw values of the specified field
        count = train[field].values
        index = train[field].index
        perc = train[field].values / train[field].sum() * 100

    # Combine the computed statistics into a list of tuples
    stats_list = list(zip(index, count, perc))

    return stats_list


# percent patches type 1
def percented_patches_first(ax, col_stats):
    patches = ax.patches
    for i in range(len(patches)):
        x = patches[i].get_y() + patches[i].get_height() / 2
        y = patches[i].get_width() + 0.05
        ax.annotate("{:.2f}%".format(col_stats[i][2]), (y, x), va="center")


# percent patches type 2
def percented_patches_second(ax, col_stats):
    patches = ax.patches
    for i in range(len(patches)):
        x = patches[i].get_y() + patches[i].get_height() / 2
        y = patches[i].get_width() + 0.05
        ax.annotate("{:.2f}%".format(col_stats[i]), (y, x), va="center")


def plot_target_variable_distribution(data_frame, target_colname):
    target_dist = compute_stats_count(data_frame, target_colname, counting=True)
    target_df = pd.DataFrame(target_dist, columns=["Value", "Count", "Percentage"])
    print(target_df)

    # Plot the countplot
    plt.figure(figsize=(6, 2))
    plt.title("Target Variable Distribution")
    ax = sns.countplot(data=data_frame, y=target_colname)
    percented_patches_second(
        ax, target_df["Percentage"].values
    )  # Pass the values as a list
    plt.tight_layout()

    plt.show()
