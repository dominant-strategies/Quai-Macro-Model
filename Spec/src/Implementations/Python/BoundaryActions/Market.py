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

    # This makes the market price an independent variable, decouples from hash
    p_qi_new = (
        (1 - ewm_lambda) * p_qi + np.random.normal(1, qi_sigma) * p_qi * ewm_lambda
    )

    p_quai_new = (
        (1 - ewm_lambda) * p_quai + np.random.normal(1, quai_sigma) * p_quai * ewm_lambda
    ) * 0.99

    space = {
        "Qi Return": max(p_qi_new / p_qi - 1, -0.99),
        "Quai Return": max(p_quai_new / p_quai - 1, -0.99),
    }
    return [space]
