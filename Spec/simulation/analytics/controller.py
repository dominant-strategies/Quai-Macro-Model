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

    df.set_index("Block Number")[["Beta0 Error", "Beta1 Error"]].plot(style=".")

    plt.ylabel("Error in Beta Value")
    plt.yscale("log")
    plt.title("Error in Beta0 and Beta1")
    plt.show()


def plot_beta_error_norm(df):
    df.set_index("Block Number")["Beta Estimation Norm"].plot(style=".")
    plt.ylabel("Error Norm ")
    plt.yscale("log")
    plt.title("Error Norm for Beta Estimation")
    plt.show()
