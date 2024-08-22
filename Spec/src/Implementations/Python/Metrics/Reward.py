from math import log


def qi_to_hash_metric(state, params, spaces):
    return spaces[0]["Qi"] / state["K Qi"]


def quai_to_hash_metric(state, params, spaces):
    return params["Quai Reward Base Parameter"] ** (spaces[0]["Quai"] / state["K Quai"])


def hash_to_qi_metric(state, params, spaces):
    return spaces[0]["Hash"] * state["K Qi"]


def hash_to_quai_metric(state, params, spaces):
    return state["K Quai"] * log(
        spaces[0]["Hash"], params["Quai Reward Base Parameter"]
    )
