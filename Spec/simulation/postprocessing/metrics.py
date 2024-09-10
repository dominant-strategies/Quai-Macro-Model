def difficulty_metrics(metrics, state, params, df):
    metrics["Difficulty Mu"] = df["Block Difficulty"].mean()
    metrics["Difficulty Sigma"] = df["Block Difficulty"].std()


def reward_metrics(metrics, state, params, df):
    metrics["Block Reward Ratio Mu"] = df["Block Reward Ratio"].mean()
    metrics["Block Reward Ratio Sigma"] = df["Block Reward Ratio"].std()
    metrics["Conversion Rate Mu"] = df["Conversion Rate"].mean()
    metrics["Conversion Rate Sigma"] = df["Conversion Rate"].std()


def controller_metrics(metrics, state, params, df):
    metrics["K Qi / K Quai Mu"] = df["K Qi / K Quai"].mean()
    metrics["K Qi / K Quai Sigma"] = df["K Qi / K Quai"].std()


def mined_ratio_metrics(metrics, state, params, df):
    metrics["Mined Ratio (Block Percent) Mu"] = df["Mined Ratio (Block Percent)"].mean()
    metrics["Mined Ratio (Block Percent) Sigma"] = df[
        "Mined Ratio (Block Percent)"
    ].std()


def beta_convergance(metrics, state, params, df, target_norm=0.25):

    temp = df[df["Beta Estimation Norm"] < target_norm]
    if len(temp) == 0:
        metrics["Time to Beta Convergance"] = None
    else:
        metrics["Time to Beta Convergance"] = temp["Block Number"].min()
