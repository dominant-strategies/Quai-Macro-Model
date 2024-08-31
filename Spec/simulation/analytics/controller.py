import matplotlib.pyplot as plt
import numpy as np


def plot_betas(df):
    df.set_index("Block Number")[["Population Beta0", "Estimate Beta0"]].plot(
        kind="line"
    )
    plt.ylabel("Beta Value")
    plt.title("Population vs. Estimate of Beta0")
    plt.show()

    df.set_index("Block Number")[["Population Beta1", "Estimate Beta1"]].plot(
        kind="line"
    )
    plt.ylabel("Beta Value")
    plt.title("Population vs. Estimate of Beta0")
    plt.show()


def plot_beta_errors(df):
    # Calculate the error in the beta values
    df["Beta0 Error"] = np.abs(df["Population Beta0"] - df["Estimate Beta0"])
    df["Beta1 Error"] = np.abs(df["Population Beta1"] - df["Estimate Beta1"])

    df.set_index("Block Number")[["Beta0 Error", "Beta1 Error"]].plot(style=".")

    plt.ylabel("Error in Beta Value")
    plt.yscale("log")
    plt.title("Error in Beta0 and Beta1")
    plt.show()
