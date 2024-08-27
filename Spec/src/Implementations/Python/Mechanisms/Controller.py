def set_k_mechanism(state, params, spaces):
    state["K Quai"] = spaces[0]["K Quai"]
    state["K Qi"] = spaces[0]["K Qi"]


def set_estimated_beta_vector_mechanism(state, params, spaces):
    state["Estimated Mining Beta Vector"] = spaces[0]["Beta"]
