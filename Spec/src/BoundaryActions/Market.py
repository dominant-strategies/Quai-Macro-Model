test_quai_conversion = {
    "name": "TEST Quai Conversion",
    "description": "Test function that moves to exchange 100 Quai.",
    "logic": "Return a space with quai conversion of 100",
}

test_qi_conversion = {
    "name": "TEST Qi Conversion",
    "description": "Test function that moves to exchange 100 Qi.",
    "logic": "Return a space with qi conversion of 100",
}

conversions_boundary_action = {
    "name": "Conversions Boundary Action",
    "description": "Boundary action which determines amount of potentially converted Qi or Quai.",
    "constraints": [],
    "boundary_action_options": [test_quai_conversion, test_qi_conversion],
    "called_by": [],
    "codomain": ["Conversion Space"],
    "parameters_used": [],
    "metrics_used": ["Conversion Rate Metric"],
}

price_movements_boundary_action = {
    "name": "Price Movements Boundary Action",
    "description": "Boundary action which begins the process of price changes.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": [],
    "codomain": ["Price Movement Space"],
    "parameters_used": ["Asset Return Parameterization"],
}


market_boundary_actions = [conversions_boundary_action, price_movements_boundary_action]
