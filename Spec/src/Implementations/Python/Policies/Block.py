from bisect import bisect
import numpy as np
from copy import deepcopy
from math import log


def compute_progress(state, params, block_hashes, block_hashes_cs, aggregate_hashpower):
    total_hashpower = params["Target Mining Time"] * aggregate_hashpower
    # Prime block mined
    if total_hashpower >= block_hashes_cs[-1]:
        time_to_mine = (
            block_hashes_cs[-1] / total_hashpower * params["Target Mining Time"]
        )

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
    state, params, time_to_mine, block_hashes, block_hashes_cs, new_difficulty
):
    percentage_of_target = time_to_mine / params["Target Mining Time"]

    # Too fast if it finishes the block within less than 80% of target time , increase difficulty by 5%
    if percentage_of_target < 0.8:
        new_difficulty = new_difficulty * 1.05
        for y in block_hashes:
            y["Difficulty"] = int(y["Difficulty"] * 1.05)
        block_hashes_cs = np.cumsum([x["Difficulty"] for x in block_hashes])
        # print("Difficulty adjusted upwards by 5%")
    # Too slow, did not complete in time
    elif percentage_of_target >= 1:
        new_difficulty = new_difficulty * 0.95
        for y in block_hashes:
            y["Difficulty"] = int(y["Difficulty"] * 0.95)
        block_hashes_cs = np.cumsum([x["Difficulty"] for x in block_hashes])
        # print("Difficulty adjusted downwards by 5%")
    else:
        # print("Difficulty not changed, within reasonable range")
        pass
    return block_hashes, block_hashes_cs, new_difficulty


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
            state, params, time_to_mine, block_hashes, block_hashes_cs, new_difficulty
        )

    space = {}
    space["New Difficulty"] = new_difficulty
    l = []
    for x, y in zip(l1, l2):
        l.append({"Mined Blocks": x, "Mining Time": y})
    space["Mining Epochs"] = l
    return [space]


def calculate_qi_reward(difficulty, k_qi):
    return difficulty / k_qi


def calculate_quai_reward(difficulty, k_quai, quai_base):
    return quai_base ** -(1 + k_quai) * log(difficulty, quai_base)


def block_reward_policy_v1(state, params, spaces):
    space = deepcopy(spaces[0])
    epochs = space.pop("Mining Epochs")
    for x in epochs:
        for y in x["Mined Blocks"]:
            y["Qi Reward Offered"] = calculate_qi_reward(y["Difficulty"], state["K Qi"])
            y["Quai Reward Offered"] = calculate_quai_reward(
                y["Difficulty"], state["K Quai"], params["Quai Reward Base Parameter"]
            )
    space["Mined Blocks"] = epochs
    return [space]


def deterministic_mining_payment_policy(state, params, spaces):
    mined_quai = 0
    mined_qi = 0
    quai_hash = 0
    qi_hash = 0
    for block_epoch in spaces[0]["Mined Blocks"]:
        for block in block_epoch["Mined Blocks"]:
            if (
                block["Quai Reward Offered"] * state["Quai Price"]
                >= block["Qi Reward Offered"] * state["Qi Price"]
            ):
                print("Quai")
            else:
                print("Qi")
