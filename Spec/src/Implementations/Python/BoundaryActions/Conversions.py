def conversions_boundary_action_v1(state, params, spaces):
    return test_quai_conversion(state, params, spaces)


def test_quai_conversion(state, params, spaces):
    return [
        {
            "Token": "Quai",
            "Amount": 100,
            "Locking Time": list(
                state["Stateful Metrics"]["Current Lockup Options"](
                    state, params
                ).keys()
            )[1],
        }
    ]


def test_qi_conversion(state, params, spaces):
    return [
        {
            "Token": "Qi",
            "Amount": 100,
            "Locking Time": list(
                state["Stateful Metrics"]["Current Lockup Options"](
                    state, params
                ).keys()
            )[1],
        }
    ]
