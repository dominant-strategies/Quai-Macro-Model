def circulating_quai_supply(state, params):
    return state["Quai Supply"] - state["Locked Quai Supply"]


def circulating_qi_supply(state, params):
    return state["Qi Supply"] - state["Locked Qi Supply"]


def current_lockup_options(state, params):
    year = 1 + int(state["Time"] / 365)
    year = min(year, max(params["Lockup Options"].keys()))
    return params["Lockup Options"][year]
