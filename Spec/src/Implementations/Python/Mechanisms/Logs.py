def update_historical_converted_qi_mechanism(state, params, spaces):
    if spaces[0]:
        state["Historical Converted Qi"].append(spaces[0])


def update_historical_converted_quai_mechanism(state, params, spaces):
    if spaces[0]:
        state["Historical Converted Quai"].append(spaces[0])


def log_simulation_data_mechanism(state, params, spaces):
    log = {}
    state["Simulation History Log"].append(log)
