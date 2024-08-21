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
        "description": """"The wiring for mining a block.

For the decision between Qi and Quai, the idea is that there should be a Schelling point, if the miner is mining and Qi is an option, they will only look at Qi as making sense if the market price is above their production price.

If the demand for Qi is greater than the supply, there should be a profitable opportunity until market price approaches at which point amount of Qi is at equilibrium because the market price matches the production price.""",
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
