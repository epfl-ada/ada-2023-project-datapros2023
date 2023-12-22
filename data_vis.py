import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def get_ylims(data_series: pd.Series) -> tuple:
    """Helper function to determine limits for data plotting.

    Args:
        data_series (pd.Series): Data series to be plotted

    Returns:
        tuple: Minimual and maximal limits for plotting.
    """
    lim = max(np.abs(np.max(data_series)), np.abs(np.min(data_series)))
    return (-lim - 0.1 * lim, lim + 0.1 * lim)


def plot_n_sum_avg(data_frame: pd.DataFrame, title: str, normalized: bool = True):
    """Plot sums and averages of word weights side-by-side on the same
    plot. Each will have its own y-axis, while the x-axis is shared.

    Args:
        data_frame (pd.DataFrame): Must contain columns [word, sum, occ, avg, nsum, navg].
        title (str): Plot title.
        normalized (bool, optional): If true, plot the normalized colummns, otherwise,
        plot the original values. Defaults to True.
    """
    bar_width = 0.35
    c1 = "#2ecc71"  # Color for the 1st plot
    c2 = "#9b59b6"  # Color for the 2nd plot

    if normalized:
        sum_series = data_frame["nsum"]
        avg_series = data_frame["navg"]
    else:
        avg_series = data_frame["avg"]
        sum_series = data_frame["sum"]

    # Generate x values based on the DataFrame index
    x = np.arange(len(data_frame))

    # Create the first bar plot on the left y-axis
    fig, ax1 = plt.subplots(figsize=(14, 6))
    ax1.bar(
        x,
        sum_series,
        width=bar_width,
        color=c1,
        label="Normalized total weight",
        bottom=0,
    )
    ax1.set_xlabel("Word")
    ax1.set_ylabel("Normalized total weight", color=c1)
    ax1.tick_params("y", colors=c1)

    # Create a a second bar plot on the right y-axis
    ax2 = ax1.twinx()
    ax2.bar(
        x + bar_width,
        avg_series,
        width=bar_width,
        color=c2,
        label="Normalized average weight",
        bottom=0,
    )
    ax2.set_ylabel("Normalized average weight", color=c2)
    ax2.tick_params("y", colors=c2)

    # Set symmetrical ylims if plotting normalized data.
    if normalized:
        ax1.set_ylim(get_ylims(sum_series))
        ax2.set_ylim(get_ylims(avg_series))

    # Plot y=0 line for prettier plot
    plt.axhline(y=0, color="black", linestyle="--")

    # Set x-axis ticks and labels
    ax1.set_xticks(x + bar_width / 2)
    ax1.set_xticklabels(data_frame["word"], rotation=45)

    # Set title and legend
    plt.title(title)
    #plt.savefig('lda_figs/' + title + '.png')
    fig.tight_layout()

    plt.show()
