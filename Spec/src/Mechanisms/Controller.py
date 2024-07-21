set_k_mechanism = {
    "name": "Set K Mechanism",
    "description": "A mechanism which sets the values for K",
    "constraints": [],
    "logic": "",
    "domain": [
        "K Space",
    ],
    "parameters_used": [],
    "updates": [
        ("Global", "K Quai", False),
        ("Global", "K Qi", False),
    ],
}

controller_mechanisms = [set_k_mechanism]
