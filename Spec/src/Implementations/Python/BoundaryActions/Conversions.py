from random import random, choice
import numpy as np


def conversions_boundary_action_v1(state, params, spaces):
    market_exchange_rate = state["Qi Price"]/state["Quai Price"]
    protocol_exchange_rate = state["K Quai"] * np.log2(state["Block Difficulty"])/(state["K Qi"] * state["Block Difficulty"])

    print("k quai", state["K Quai"], "k qi", state["K Qi"])
    print("market exchange rate", market_exchange_rate, "protocol exchange rate", protocol_exchange_rate)

    # TODO: If needed this can be made a state variable or params that gets
    # adjusted for more dynamic testing
    number_total_conversions = 100
    p_quai_conversion = 0.05
    p_qi_conversion = 0.05

    tokens = []
    amounts = []
    
    # If the protocol exchange rate is greater than the market exchange rate 
    # Quai is at a discount relative to Qi, so rational speculators would 
    # convert Qi to Quai
    # q value here is the token that is getting converted, in the next policy
    # the supply adjustment is handled
    if protocol_exchange_rate > market_exchange_rate:
        q = "Qi"
    else:
        q = "Quai"

    if q == "Quai":
        circulating = state["Stateful Metrics"]["Circulating Quai Supply"](
            state, params
        )
        # If the supply is more than 1000, limit it to 1000
        # circulating = min(1000, circulating)
    else:
        circulating = 100 * state["Stateful Metrics"]["Circulating Qi Supply"](state, params)
        # If the supply is more than 1000, limit it to 1000
        # circulating = min(1000, circulating)

    T = circulating * params["Speculator Percentage"] * params["Speculator Rationality Ratio"]
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
    print("Speculators are trying to convert", q)

    tokens.append(q)
    amounts.append(C)

    random_allocation = random()
    
    print("Quai supply", state["Stateful Metrics"]["Circulating Quai Supply"](state, params))
    print("Qi supply", state["Stateful Metrics"]["Circulating Qi Supply"](state, params))

    tokens.append("Qi")
    amounts.append(min(state["Stateful Metrics"]["Circulating Qi Supply"](state, params), 1000) * random_allocation * (1 - params["Speculator Rationality Ratio"]))

    tokens.append("Quai")
    amounts.append(min(state["Stateful Metrics"]["Circulating Quai Supply"](state, params), 1000) * (1 - random_allocation) * (1 - params["Speculator Rationality Ratio"]))

    L = state["Stateful Metrics"]["Current Lockup Options"](state, params)
    H = choice(list(L.keys()))
    space = {"Token": tokens, "Amount": amounts, "Locking Time": H}

    print("converted ", space)
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
