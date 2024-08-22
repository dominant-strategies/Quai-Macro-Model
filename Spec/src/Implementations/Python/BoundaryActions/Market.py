def test_price_movements_boundary(state, params, spaces):
    space = {"Qi Return": 0.05, "Quai Return": 0.1}
    return [space]


def hashpower_price_movement(state, params, spaces):
    ewm_lambda = params["Price EWMA Lambda"]
    c = state["Metrics"]["Conversion Rate Metric"]()
