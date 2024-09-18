psub_blocks = []


[
    "Price Movements Wiring",
    "Conversions Wiring",
    "Mine Block Wiring",
    "Unlock Tokens Wiring",
    "Update Population Beta Wiring",
    "Log Simulation Data Mechanism",
]


def p_log(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Log Simulation Data Mechanism"](state, _params, [])
    return {}


test_block = {
    "policies": {
        "test": p_log,
    },
    "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
}

psub_blocks.append(test_block)
