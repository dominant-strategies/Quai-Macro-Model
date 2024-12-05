def update_block_difficulty_mechanism(state, params, spaces):
    state["Block Difficulty"] = spaces[0]["Block Difficulty"]


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
    state["Mining Log"].append(spaces[0])

def update_hashrate_mechanism(state, params, spaces):
    prev_hashpower = state["Aggregate Hashpower"]
    # use the percentage of miners that are not mining and update the aggregate
    # hashpower
    state["Aggregate Hashpower"] = (prev_hashpower + 0.01 * prev_hashpower) *  (1 - state["Ratio of Miners not Mining"])
