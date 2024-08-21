def update_block_difficulty_mechanism(state, params, spaces):
    new = (
        state["Block Difficulty"] * (params["Difficulty Adjustment Period"] - 1)
        + spaces[0]["Block Difficulty"]
    ) / params["Difficulty Adjustment Period"]
    state["Block Difficulty"] = new
