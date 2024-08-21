mine_block_boundary_action1 = {
    "name": "Mine Block Boundary Action V1",
    "description": "Boundary action for determining the blocks to mine and aggregate hashpower.",
    "logic": """1. Aggregate hashpower is a dummy assumption right now equal to 1000 * the Qi Price
    2. Prime blocks, region blocks and zone blocks are created based on network size and their difficulties equal the global difficulty times their difficulty multipliers from the parameters
    3. Noise is added to all the block difficulties as a multiplier from a lognormal distribution with mean 0 and standard deviation of .05
    4. A cumulative sum array is also created of difficulty for ease in computation for the simulation""",
}

mine_block_boundary_action2 = {
    "name": "Mine Block Boundary Action V2",
    "description": "Boundary action for determining the blocks to mine and aggregate hashpower.",
    "logic": """1. Aggregate hashpower is pulled from the [[Aggregate Hashpower Series]] parameter
    TBD""",
}

mine_block_boundary_action = {
    "name": "Mine Block Boundary Action",
    "description": "Boundary action which determines the the aggregate hashpower as well as the blocks that need to be mined and their difficulties.",
    "constraints": [],
    "boundary_action_options": [
        mine_block_boundary_action1,
        mine_block_boundary_action2,
    ],
    "called_by": [],
    "codomain": [
        "Pre-Mining Space",
    ],
    "parameters_used": ["Aggregate Hashpower Series"],
}

block_boundary_actions = [mine_block_boundary_action]
