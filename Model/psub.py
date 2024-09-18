psub_blocks = []


def p_log(_params, substep, state_history, state) -> dict:
    print(_params["MSI"])


test_block = {
    "policies": {
        "test": p_log,
    },
    "variables": {},
}

psub_blocks.append(test_block)
