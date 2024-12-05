def block_reward_ratio_conversion_policy(state, params, spaces):

    lockup_return = state["Stateful Metrics"]["Current Lockup Options"](state, params)[
        spaces[0]["Locking Time"]
    ]

    assets = spaces[0]["Token"]
    amounts = spaces[0]["Amount"]

    for i in range(0, len(assets)):
        asset = assets[i]
        amount = amounts[i]
        assert asset in ["Quai", "Qi"], "{} is not a valid asset".format(asset)
        assert amount >= 0, "Amount must be positive"
        conversion_rate = state["Metrics"]["Conversion Rate Metric"](state, params, [])
        if asset == "Quai":
            if amount < params["Minimum Quai Conversion Amount"]:
                quai = 0
                qi = 0
            elif amount >= state["Quai Supply"]:
                quai = 0
                qi = 0
            else:
                quai = -amount
                qi = amount / conversion_rate * lockup_return
        else:
            if amount < params["Minimum Qi Conversion Amount"]:
                quai = 0
                qi = 0
            elif amount >= state["Qi Supply"]:
                quai = 0
                qi = 0
            else:
                qi = -amount
                quai = amount * conversion_rate * lockup_return

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
    space7 = space1
    space8 = space2

    t = spaces[0]["Locking Time"] * 365 + state["Time"]
    if qi > 0:
        a = [{"amount": qi, "recipient": "Conversions", "time": t}]
        b = []
    elif quai > 0:
        a = []
        b = [{"amount": quai, "recipient": "Conversions", "time": t}]
    else:
        a = []
        b = []
    space9 = {"Qi Schedule Entry": a, "Quai Schedule Entry": b}

    return [space1, space2, space3, space4, space5, space6, space7, space8, space9]


def price_movements_policy_v1(state, params, spaces):
    assert (
        min(spaces[0].values()) > -1
    ), "Values must be greater than -1 (otherwise prices could become negative)"

    r1 = spaces[0]["Qi Return"]
    r2 = spaces[0]["Quai Return"]

    space = {
        "Qi Price": state["Qi Price"] * (1 + r1),
        "Quai Price": state["Quai Price"] * (1 + r2),
    }

    return [space]
