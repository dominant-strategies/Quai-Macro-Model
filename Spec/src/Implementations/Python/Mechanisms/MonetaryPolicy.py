def mint_qi_tokens_mechanism(state, params, spaces):
    amount = spaces[0]["Qi"]
    if amount == 0:
        return
    assert amount > 0, "Amount must be positive. spaces: {}, state: {}".format(
        spaces, state
    )
    state["Qi Supply"] += amount


def mint_quai_token_mechanism(state, params, spaces):
    amount = spaces[0]["Quai"]
    if amount == 0:
        return
    assert amount > 0, "Amount must be positive"
    state["Quai Supply"] += amount


def burn_qi_tokens_mechanism(state, params, spaces):
    amount = spaces[0]["Qi"]
    if amount == 0:
        return
    assert amount > 0, "Amount must be positive"
    state["Qi Supply"] -= amount


def burn_quai_tokens_mechanism(state, params, spaces):
    amount = spaces[0]["Quai"]
    if amount == 0:
        return
    assert amount > 0, "Amount must be positive"
    state["Quai Supply"] -= amount


def update_prices_mechanism(state, params, spaces):
    state["Qi Price"] = spaces[0]["Qi Price"]
    state["Quai Price"] = spaces[0]["Quai Price"]


def update_locked_qi_mechanism(state, params, spaces):
    state["Locked Qi Supply"] += spaces[0]["Qi"]


def update_locked_quai_mechanism(state, params, spaces):
    state["Locked Quai Supply"] += spaces[0]["Quai"]
