import numpy as np


def test_price_movements_boundary(state, params, spaces):
    space = {"Qi Return": 0.05, "Quai Return": 0.1}
    return [space]


def hashpower_price_movement(state, params, spaces):
    ewm_lambda = params["Price EWMA Lambda"]
    # c = state["Metrics"]["Conversion Rate Metric"](state, params, [])
    p_quai = state["Quai Price"]
    p_qi = state["Qi Price"]
    hashpower_cost = params["Hashpower Cost Series"][state["Block Number"]]
    qi_sigma = params["Qi Price Movemement Sigma"]
    quai_sigma = params["Quai Price Movemement Sigma"]

    # Getting the previous p_quai value
    p_quai = p_quai * state["Circulating Quai Supply"][state["Block Number"]-1] / state["Market Quai Supply Demand"]

    print("Circulating Quai supply n-2", state["Circulating Quai Supply"][state["Block Number"]-1])
    print("Circulating Quai supply n-1", state["Stateful Metrics"]["Circulating Quai Supply"](state, params))

    print("price of Quai before the demand adjustment", p_quai)
    p_quai = p_quai * state["Market Quai Supply Demand"] / state["Stateful Metrics"]["Circulating Quai Supply"](state, params)
    print("price of Quai after the demand adjustment", p_quai)

    # Getting the previous p_qi value
    p_qi = p_qi * state["Circulating Qi Supply"][state["Block Number"]-1] / state["Market Qi Supply Demand"]

    print("Circulating Qi supply n-2", state["Circulating Qi Supply"][state["Block Number"]-1])
    print("Circulating Qi supply n-1", state["Stateful Metrics"]["Circulating Qi Supply"](state, params))

    print("price of Qi before the demand adjustment", p_qi)
    p_qi = p_qi * state["Market Qi Supply Demand"] / state["Stateful Metrics"]["Circulating Qi Supply"](state, params)
    print("price of Qi after the demand adjustment", p_qi)


    # This makes the market price an independent variable, decouples from hash
    p_qi_new = (
        (1 - ewm_lambda) * p_qi + np.random.normal(1, qi_sigma) * p_qi * ewm_lambda
    )

    p_quai_new = (
        (1 - ewm_lambda) * p_quai + np.random.normal(1, quai_sigma) * p_quai * ewm_lambda
    ) * 0.999

    space = {
        "Qi Return": p_qi_new,
        "Quai Return": p_quai_new,
    }
    return [space]
