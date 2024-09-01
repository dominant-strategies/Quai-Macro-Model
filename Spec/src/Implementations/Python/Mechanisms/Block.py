def update_block_difficulty_mechanism(state, params, spaces):

    new = (
        state["Block Difficulty"] * (params["Difficulty Adjustment Period"] - 1)
        + spaces[0]["Block Difficulty"]
    ) / params["Difficulty Adjustment Period"]
    if new < 2:
        print(
            "Difficulty was getting adjusted to be below 2, setting to 2 to avoid issues from extremely low difficulties"
        )
        new = 2
    state["Block Difficulty"] = new


def append_to_unlock_schedule_mechanism(state, params, spaces):
    state["Quai Unlock Schedule"].extend(spaces[0]["Quai Schedule Entry"])
    state["Quai Unlock Schedule"] = sorted(
        state["Quai Unlock Schedule"], key=lambda x: x["time"]
    )

    state["Qi Unlock Schedule"].extend(spaces[0]["Quai Schedule Entry"])
    state["Qi Unlock Schedule"] = sorted(
        state["Qi Unlock Schedule"], key=lambda x: x["time"]
    )


def update_historical_mined_ratio_mechanism(state, params, spaces):
    state["Historical Mined Ratio"].append(spaces[0])


def update_historical_qi_hash_mechanism(state, params, spaces):
    if spaces[0]:
        state["Historical Qi Hash"].append(spaces[0])


def update_historical_quai_hash_mechanism(state, params, spaces):
    if spaces[0]:
        state["Historical Quai Hash"].append(spaces[0])


def increment_block_number_mechanism(state, params, spaces):
    state["Block Number"] += 1


def increment_time_mechanism(state, params, spaces):
    state["Time"] += spaces[0]["Mining Time"] / 60 / 60 / 24


def log_mined_blocks_mechanism(state, params, spaces):
    state["Mining Log"].append(spaces)
