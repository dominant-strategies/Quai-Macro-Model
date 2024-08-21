def circulating_quai_supply(state, params):
    return state["Quai Supply"] - state["Locked Quai Supply"]


def circulating_qi_supply(state, params):
    return state["Qi Supply"] - state["Locked Qi Supply"]
