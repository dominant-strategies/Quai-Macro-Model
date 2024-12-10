def update_population_beta_boundary_action_signal(state, params, spaces):
    return [{"Beta": params["Population Beta Signal"][state["Block Number"]]}]
