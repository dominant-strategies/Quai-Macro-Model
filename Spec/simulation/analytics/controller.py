import matplotlib.pyplot as plt


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
