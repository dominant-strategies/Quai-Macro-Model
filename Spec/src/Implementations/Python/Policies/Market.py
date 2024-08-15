def block_reward_ratio_conversion_policy(state, params, spaces):
    asset = spaces[0]["Token"]
    amount = spaces[0]["Amount"]
    assert asset in ["Quai", "Qi"], "{} is not a valid asset".format(asset)
    assert amount >= 0, "Amount must be positive"
    conversion_rate = state["Metrics"]["Current Block Reward Ratio Metric"](
        state, params, []
    )
    if asset == "Quai":
        if amount < params["Minimum Quai Conversion Amount"]:
            quai = 0
            qi = 0
        elif amount >= state["Quai Supply"]:
            quai = 0
            qi = 0
        else:
            quai = -amount
            qi = amount / conversion_rate
    else:
        if amount < params["Minimum Qi Conversion Amount"]:
            quai = 0
            qi = 0
        elif amount >= state["Qi Supply"]:
            quai = 0
            qi = 0
        else:
            qi = -amount
            quai = amount * conversion_rate
    print(qi, quai)
