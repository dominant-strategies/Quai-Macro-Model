import numpy as np


def test_price_movements_boundary(state, params, spaces):
    space = {"Qi Return": 0.05, "Quai Return": 0.1}
    return [space]


def hashpower_price_movement(state, params, spaces):
    ewm_lambda = params["Price EWMA Lambda"]
    c = state["Metrics"]["Conversion Rate Metric"](state, params, [])
    p_quai = state["Quai Price"]
    p_qi = state["Qi Price"]
    hashpower_cost = params["Hashpower Cost Series"][state["Block Number"]]
    qi_sigma = params["Qi Price Movemement Sigma"]
    quai_sigma = params["Quai Price Movemement Sigma"]

    p_qi_new = (
        ewm_lambda * hashpower_cost
        + (1 - ewm_lambda) * p_qi
        + np.random.normal(0, qi_sigma)
    )
    p_quai_new = (
        ewm_lambda * c * p_qi
        + (1 - ewm_lambda) * p_quai
        + np.random.normal(0, quai_sigma)
    )

    space = {"Qi Return": p_qi_new / p_qi - 1, "Quai Return": p_quai_new / p_quai - 1}
    return [space]
