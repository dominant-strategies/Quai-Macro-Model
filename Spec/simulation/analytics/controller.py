import matplotlib.pyplot as plt
import numpy as np


def plot_betas(df):
    df.set_index("Block Number")[["Population Beta0", "Estimate Beta0"]].plot(
        kind="line"
    )
    plt.xlabel("Prime Block Number")
    plt.ylabel("Beta Value")
    plt.title("Population vs. Estimate of Beta0")
    plt.show()

    df.set_index("Block Number")[["Population Beta1", "Estimate Beta1"]].plot(
        kind="line"
    )
    plt.xlabel("Prime Block Number")
    plt.ylabel("Beta Value")
    plt.title("Population vs. Estimate of Beta1")
    plt.show()


def plot_beta_errors(df):

    df.set_index("Block Number")[["Beta0 Error", "Beta1 Error"]].plot(style=".")
    plt.xlabel("Prime Block Number")
    plt.ylabel("Error in Beta Value")
    plt.yscale("log")
    plt.title("Error in Beta0 and Beta1")
    plt.show()


def plot_beta_error_norm(df):
    df.set_index("Block Number")["Beta Estimation Norm"].plot(style=".")
    plt.xlabel("Prime Block Number")
    plt.ylabel("Error Norm ")
    plt.yscale("log")
    plt.title("Error Norm for Beta Estimation")
    plt.show()


def plot_mined_block_percent(df):
    df.set_index("Block Number")["Mined Ratio (Block Percent)"].rolling(30).mean().plot(
        kind="line"
    )
    plt.xlabel("Prime Block Number")
    plt.ylabel("Percentage of Blocks Quai Taken")
    plt.title("30 Day Rolling Average of Mining Percentages")
    plt.show()


def plot_block_difficulty(df):
    df.set_index("Block Number")["Block Difficulty"].plot(kind="line")
    plt.xlabel("Prime Block Number")
    plt.ylabel("Difficulty")
    plt.title("Global Block Difficulty")
    plt.show()


def plot_kqi_ratio(df):
    df.set_index("Block Number")["K Qi / K Quai"].plot(kind="line")
    plt.xlabel("Prime Block Number")
    plt.ylabel("K Qi / K Quai")
    plt.title("Ratio of K Qi to K Quai")
    plt.show()


def difficulty_mining_scatter(df):
    df.plot(kind="scatter", x="Block Difficulty", y="Mined Ratio (Block Percent)")
    plt.xlabel("Block Difficulty")
    plt.ylabel("Percentage of Blocks Quai Taken")
    plt.title("Difficulty vs. Quai Taken")
    plt.show()
