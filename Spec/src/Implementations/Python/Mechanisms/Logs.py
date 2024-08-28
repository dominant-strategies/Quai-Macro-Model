def update_historical_converted_qi_mechanism(state, params, spaces):
    if spaces[0]:
        state["Historical Converted Qi"].append(spaces[0])


def update_historical_converted_quai_mechanism(state, params, spaces):
    if spaces[0]:
        state["Historical Converted Quai"].append(spaces[0])


def log_simulation_data_mechanism(state, params, spaces):
    log = {}

    log["Estimate Beta0"] = state["Estimated Mining Beta Vector"][0]
    log["Estimate Beta1"] = state["Estimated Mining Beta Vector"][1]

    log["Population Beta0"] = state["Population Mining Beta Vector"][0]
    log["Population Beta1"] = state["Population Mining Beta Vector"][1]

    state["Simulation History Log"].append(log)
