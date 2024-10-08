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

    for x in [
        "Qi Supply",
        "Quai Supply",
        "Locked Qi Supply",
        "Locked Quai Supply",
        "Block Number",
        "Block Difficulty",
        "Number of Regions",
        "Zones per Region",
        "K Qi",
        "K Quai",
        "Quai Price",
        "Qi Price",
        "Time",
        "Delta Time",
    ]:
        log[x] = state[x]

    if len(state["Historical Mined Ratio"]) > 0:
        log["Mined Ratio"] = state["Historical Mined Ratio"][-1]["Ratio"]

        temp = state["Mining Log"][-1]["Quai Taken"]
        log["Mined Ratio (Block Percent)"] = sum([x > 0 for x in temp]) / len(temp)
    else:
        log["Mined Ratio"] = None
        log["Mined Ratio (Block Percent)"] = None

    log["Block Reward Ratio"] = state["Metrics"]["Current Block Reward Ratio Metric"](
        state, params, []
    )
    log["Conversion Rate"] = state["Metrics"]["Conversion Rate Metric"](
        state, params, []
    )
    log["K Qi / K Quai"] = state["K Qi"] / state["K Quai"]

    state["Simulation History Log"].append(log)
