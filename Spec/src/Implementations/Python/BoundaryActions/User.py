def update_population_beta_boundary_action_signal(state, params, spaces):
    print("using the population beta from the params")
    return [{"Beta": params["Population Beta Signal"][state["Block Number"]]}]
