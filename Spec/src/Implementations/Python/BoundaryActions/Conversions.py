from random import random, choice
import numpy as np


def conversions_boundary_action_v1(state, params, spaces):
    if len(state["Historical Mined Ratio"]) > 0:
        quai_probability = state["Historical Mined Ratio"][-1]["Ratio"]
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
    T = circulating * params["Speculator Percentage"]
    C = T * max(
        min(
            1,
            np.random.normal(
                params["Conversion Percentage Mu"],
                params["Conversion Percentage Sigma"],
            ),
        ),
        0,
    )
    L = state["Stateful Metrics"]["Current Lockup Options"](state, params)
    H = choice(list(L.keys()))
    space = {"Token": q, "Amount": C, "Locking Time": H}
    return [space]


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


def do_not_use_conversion(state, params, spaces):
    space = {
        "Token": "Qi",
        "Amount": 100 * params["Probability of Rational Miners"],
        "Locking Time": list(
            state["Stateful Metrics"]["Current Lockup Options"](state, params).keys()
        )[1],
    }
    return [space]
