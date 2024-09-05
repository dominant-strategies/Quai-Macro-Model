def difficulty_metrics(metrics, state, params, df):
    metrics["Difficulty Mu"] = df["Block Difficulty"].mean()
    metrics["Difficulty Sigma"] = df["Block Difficulty"].std()
