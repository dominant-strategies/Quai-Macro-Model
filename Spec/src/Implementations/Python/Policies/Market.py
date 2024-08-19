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

    # Minting Spaces
    space1 = {"Qi": max(0, qi)}
    space2 = {"Quai": max(0, quai)}

    # Burning Spaces
    space3 = {"Qi": -min(0, qi)}
    space4 = {"Quai": -min(0, quai)}

    if qi < 0:
        space5 = {"Qi": qi, "Quai": quai, "Time": state["Time"]}
        space6 = None
    elif quai < 0:
        space5 = None
        space6 = {"Qi": qi, "Quai": quai, "Time": state["Time"]}

    else:
        space5 = None
        space6 = None
    return [space1, space2, space3, space4, space5, space6]


def price_movements_policy_v1(state, params, spaces):
    pass
