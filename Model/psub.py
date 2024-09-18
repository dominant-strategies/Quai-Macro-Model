psub_blocks = []


def p_price(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Price Movements Wiring"](state, _params, [])
    return {}


def p_conversions(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Conversions Wiring"](state, _params, [])
    return {}


def p_mine_blocks(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Mine Block Wiring"](state, _params, [])
    return {}


def p_unlock(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Unlock Tokens Wiring"](state, _params, [])
    return {}


def p_beta(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Update Population Beta Wiring"](state, _params, [])
    return {}


def p_log(_params, substep, state_history, state) -> dict:
    _params["MSI"].components["Log Simulation Data Mechanism"](state, _params, [])
    return {}


psub_blocks = [
    {
        "policies": {
            "test": p_price,
        },
        "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
    },
    {
        "policies": {
            "test": p_conversions,
        },
        "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
    },
    {
        "policies": {
            "test": p_mine_blocks,
        },
        "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
    },
    {
        "policies": {
            "test": p_unlock,
        },
        "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
    },
    {
        "policies": {
            "test": p_beta,
        },
        "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
    },
    {
        "policies": {
            "test": p_log,
        },
        "variables": {"IGNORE": lambda a, b, c, d, e: ("IGNORE", 0)},
    },
]
