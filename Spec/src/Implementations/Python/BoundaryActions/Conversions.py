from random import random


def conversions_boundary_action_v1(state, params, spaces):
    if len(state["Historical Mined Ratio"]) > 0:
        quai_probability = state["Historical Mined Ratio"][-1]
    else:
        quai_probability = 0.5
    if random() < quai_probability:
        q = "Quai"
    else:
        q = "Qi"
    if q == "Quai":
        circulating = state["Stateful Metrics"]["Circulating Quai Supply"](
            state, params
        )
    else:
        circulating = state["Stateful Metrics"]["Circulating Qi Supply"](state, params)
    print(circulating)
    assert False


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
