def update_block_difficulty_mechanism(state, params, spaces):
    new = (
        state["Block Difficulty"] * (params["Difficulty Adjustment Period"] - 1)
        + spaces[0]["Block Difficulty"]
    ) / params["Difficulty Adjustment Period"]
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
    print("Mined ratio")
    print(spaces)


def update_historical_qi_hash_mechanism(state, params, spaces):
    print("update_historical_qi_hash_mechanism")
    print(spaces)


def update_historical_quai_hash_mechanism(state, params, spaces):
    print("update_historical_quai_hash_mechanism")
    print(spaces)


def increment_block_number_mechanism(state, params, spaces):
    spaces["Block Number"] += 1
