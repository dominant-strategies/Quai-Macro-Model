def set_k_mechanism(state, params, spaces):
    if spaces[0]["K Quai"] <= 0:
        print(
            "A value of {} was passed for setting KQuai, changing it to 1e-10".format(
                spaces[0]["K Quai"]
            )
        )
        spaces[0]["K Quai"] = 1e-10
    if spaces[0]["K Qi"] <= 0:
        print(
            "A value of {} was passed for setting KQi, changing it to 1e-10".format(
                spaces[0]["K Qi"]
            )
        )
        spaces[0]["K Qi"] = 1e-10
    state["K Quai"] = spaces[0]["K Quai"]
    state["K Qi"] = spaces[0]["K Qi"]


def set_estimated_beta_vector_mechanism(state, params, spaces):
    state["Estimated Mining Beta Vector"] = spaces[0]["Beta"]
