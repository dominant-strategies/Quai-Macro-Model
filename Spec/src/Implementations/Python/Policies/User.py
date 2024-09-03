def update_population_beta_policy_passthrough(state, params, spaces):
    beta = spaces[0]["Beta"]
    assert beta[0] < 0, "Beta0 must be negative"
    assert beta[1] > 0, "Beta1 must be positive"

    return spaces
