conversions_boundary_action = {
    "name": "Conversions Boundary Action",
    "description": "Boundary action which determines amount of potentially converted Qi or Quai.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": [],
    "codomain": ["Conversion Space"],
    "parameters_used": [],
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
