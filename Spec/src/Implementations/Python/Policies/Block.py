from bisect import bisect


def compute_progress(state, params, block_hashes, block_hashes_cs, aggregate_hashpower):
    total_hashpower = params["Target Mining Time"] * aggregate_hashpower
    # Prime block mined
    if total_hashpower >= block_hashes_cs[-1]:
        time_to_mine = block_hashes_cs[-1] / total_hashpower * params["Target Time"]

        mined_blocks = block_hashes
        block_hashes, block_hashes_cs = [], []
    else:
        time_to_mine = params["Target Mining Time"]
        i = bisect(block_hashes_cs, total_hashpower)
        mined_blocks = block_hashes[:i]
        if i > 0:
            block_hashes_cs[i:] -= block_hashes_cs[i - 1]
            block_hashes, block_hashes_cs = block_hashes[i:], block_hashes_cs[i:]

    return block_hashes, block_hashes_cs, time_to_mine, mined_blocks


def compute_difficulty_change(
    state, params, time_to_mine, block_hashes, block_hashes_cs
):
    assert False, "Ensure that block difficulties are updated"
    percentage_of_target = time_to_mine / params["Target Time"]
    new_difficulty = state["Global Difficulty"]

    print("-" * 20 + "Difficulty Adjustment" + "-" * 20)
    print("Time in mining was {} of target time".format(percentage_of_target))

    # Too fast if it finishes the block within less than 80% of target time , increase difficulty by 5%
    if percentage_of_target < 0.8:
        new_difficulty = new_difficulty * 1.05
        print("Difficulty adjusted upwards by 5%")
    # Too slow, did not complete in time
    elif percentage_of_target >= 1:
        new_difficulty = new_difficulty * 0.95
        print("Difficulty adjusted downwards by 5%")
    else:
        print("Difficulty not changed, within reasonable range")
    print("New difficulty: {}".format(new_difficulty))
    print()
    return new_difficulty


def mining_policy_v1(state, params, spaces):
    aggregate_hashpower, block_hashes, block_hashes_cs = (
        spaces[0]["Aggregate Hashpower"],
        spaces[0]["Blocks to Mine"],
        spaces[0]["Block Hash Cumulative Sum"],
    )
    l1 = []
    l2 = []
    new_difficulty = state["Block Difficulty"]
    while len(block_hashes) > 0:
        block_hashes, block_hashes_cs, time_to_mine, mined_blocks = compute_progress(
            state, params, block_hashes, block_hashes_cs, aggregate_hashpower
        )
        l1.append(mined_blocks)
        l2.append(time_to_mine)
        block_hashes, block_hashes_cs, new_difficulty = compute_difficulty_change(
            state, params, time_to_mine, block_hashes, block_hashes_cs
        )

    print(l1, l2, new_difficulty)
