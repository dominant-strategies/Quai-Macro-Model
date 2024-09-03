update_population_boundary_action_option1 = {
    "name": "Update Population Beta Boundary Action Signal",
    "description": "Signal based approach that picks the current index of the block as the signal for population beta update",
    "logic": "Return the population beta from PARAMS['Population Beta Signal'][state['Block Number']]",
}

update_population_boundary_action = {
    "name": "Update Population Beta Boundary Action",
    "description": "Boundary action which determines the update of the current population beta.",
    "constraints": [],
    "boundary_action_options": [update_population_boundary_action_option1],
    "called_by": [],
    "codomain": [
        "Beta Vector Space",
    ],
    "parameters_used": ["Population Beta Signal"],
    "metrics_used": [],
}

user_boundary_actions = [update_population_boundary_action]
