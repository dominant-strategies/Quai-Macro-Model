block_wiring = []

block_wiring.append(
    {
        "name": "Mine Block Wiring",
        "components": [
            "Mine Block Boundary Action",
            "Block Reward Policy",
            # "Mining Payment Policy",
            # "Mining Mechanisms",
        ],
        "description": "The wiring for mining a block",
        "constraints": [],
        "type": "Stack",
    }
)

block_wiring.append(
    {
        "name": "Mining Mechanisms",
        "components": ["Placeholder"],
        "description": "The mechanisms associated with mining a block",
        "constraints": [],
        "type": "Parallel",
    }
)
