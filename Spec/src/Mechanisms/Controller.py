set_k_mechanism = {
    "name": "Set K Mechanism",
    "description": "A mechanism which sets the values for K",
    "constraints": [],
    "logic": "",
    "domain": [
        "K Space",
    ],
    "parameters_used": [
        "State Update Skipping Parameter",
    ],
    "updates": [
        ("Global", "K Quai", False),
        ("Global", "K Qi", False),
    ],
}

set_estimated_beta_vector_mechanism = {
    "name": "Set Estimated Beta Vector Mechanism",
    "description": "A mechanism which sets the beta vector estimation",
    "constraints": [],
    "logic": "",
    "domain": [
        "Beta Vector Space",
    ],
    "parameters_used": [],
    "updates": [
        ("Global", "Estimated Mining Beta Vector", False),
    ],
}


controller_mechanisms = [set_k_mechanism, set_estimated_beta_vector_mechanism]
