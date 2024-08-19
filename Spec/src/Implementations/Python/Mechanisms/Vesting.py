def unlock_tokens_mechanism(state, params, spaces):
    state["Locked Quai Supply"] -= spaces[0]["Quai Tokens"]
    state["Locked Qi Supply"] -= spaces[0]["Qi Tokens"]
    state["Quai Unlock Schedule"] = spaces[0]["Quai Unlock Schedule"]
    state["Qi Unlock Schedule"] = spaces[0]["Qi Unlock Schedule"]
