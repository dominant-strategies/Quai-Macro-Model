vesting_wiring = []

vesting_wiring.append(
    {
        "name": "Unlock Tokens Wiring",
        "components": [
            "Unlock Tokens Control Action",
            "Unlock Tokens Policy",
            "Unlock Tokens Mechanism",
        ],
        "description": "The wiring for movements on the price of Qi and Quai",
        "constraints": [],
        "type": "Stack",
    }
)

vesting_wiring.append(
    {
        "name": "DO NOT USE Unlock Tokens Wiring",
        "components": [
            "Unlock Tokens Control Action",
            "Unlock Tokens Policy",
            "Unlock Tokens Mechanism",
            "DO NOT USE Print Hello Boundary Action",
        ],
        "description": "The wiring for movements on the price of Qi and Quai",
        "constraints": [],
        "type": "Stack",
    }
)
