mine_block_boundary_action1 = {
    "name": "Mine Block Boundary Action V1",
    "description": "Boundary action for determining the blocks to mine and aggregate hashpower.",
    "logic": "",
}

mine_block_boundary_action = {
    "name": "Mine Block Boundary Action",
    "description": "Boundary action which determines the block difficulty for the current block to be mined.",
    "constraints": [],
    "boundary_action_options": [mine_block_boundary_action1],
    "called_by": [],
    "codomain": [
        "Pre-Mining Space",
    ],
    "parameters_used": [],
}

block_boundary_actions = [mine_block_boundary_action]
