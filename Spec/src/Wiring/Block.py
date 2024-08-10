block_wiring = []

block_wiring.append(
    {
        "name": "Mine Block Wiring",
        "components": [
            "Mine Block Boundary Action",
            "Mining Policy",
            "Block Reward Policy",
            "Mining Payment Policy",
            "Mining Mechanisms",
        ],
        "description": "The wiring for mining a block",
        "constraints": [],
        "type": "Stack",
    }
)

block_wiring.append(
    {
        "name": "Mining Mechanisms",
        "components": [
            "Increment Block Number Mechanism",
            "Mint Qi Tokens Mechanism",
            "Mint Quai Tokens Mechanism",
            "Update Historical Mined Ratio Mechanism",
            "Update Historical Qi Hash Mechanism",
            "Update Historical Quai Hash Mechanism",
        ],
        "description": "The mechanisms associated with mining a block",
        "constraints": [],
        "type": "Parallel",
    }
)
