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


"""def mining_policy_v1(state, params, spaces):
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
    return [space]"""


def mining_policy_v1(state, params, spaces):
    aggregate_hashpower, block_hashes = (
        spaces[0]["Aggregate Hashpower"],
        spaces[0]["Blocks to Mine"],
    )

    space = {}
    space["Block Difficulty"] = [x["Difficulty"] for x in block_hashes]
    space["Mining Time"] = sum(space["Block Difficulty"]) / aggregate_hashpower
    space["New Difficulty"] = state["Block Difficulty"]

    return [space]


def block_reward_policy_v1(state, params, spaces):
    space = deepcopy(spaces[0])
    space["Quai Reward Offered"] = [
        state["Metrics"]["Hash to Quai Metric"](state, params, [{"Hash": x}])
        for x in space["Block Difficulty"]
    ]
    space["Qi Reward Offered"] = [
        state["Metrics"]["Hash to Qi Metric"](state, params, [{"Hash": x}])
        for x in space["Block Difficulty"]
    ]

    return [space]


def deterministic_mining_payment_policy(state, params, spaces):
    mined_quai = 0
    mined_qi = 0
    quai_hash = 0
    qi_hash = 0
    space0 = deepcopy(spaces[0])
    space0["Quai Taken"] = []
    space0["Qi Taken"] = []

    bd_l, quai_rew_l, qi_reward_l = (
        spaces[0]["Block Difficulty"],
        spaces[0]["Quai Reward Offered"],
        spaces[0]["Qi Reward Offered"],
    )
    for bd, quai_rew, qi_rew in zip(bd_l, quai_rew_l, qi_reward_l):
        if quai_rew * state["Quai Price"] >= qi_rew * state["Qi Price"]:
            mined_quai += quai_rew
            quai_hash += bd
            space0["Quai Taken"].append(quai_rew)
            space0["Qi Taken"].append(0)
        else:
            mined_qi += qi_rew
            qi_hash += bd
            space0["Quai Taken"].append(0)
            space0["Qi Taken"].append(qi_rew)

    space1 = {"Qi": mined_qi}
    space2 = {"Quai": mined_quai}
    space3 = {
        "Block Height": state["Block Number"],
        "Ratio": mined_quai / (mined_quai + mined_qi),
    }
    space4 = {
        "Block Height": state["Block Number"],
        "Hash Value": qi_hash,
    }
    space5 = {
        "Block Height": state["Block Number"],
        "Hash Value": quai_hash,
    }
    return [space0, space1, space2, space3, space4, space5]


def logistic_probability_payment_policy(state, params, spaces):
    mined_quai = 0
    mined_qi = 0
    quai_hash = 0
    qi_hash = 0
    space0 = deepcopy(spaces[0])
    space0["Quai Taken"] = []
    space0["Qi Taken"] = []

    bd_l, quai_rew_l, qi_reward_l = (
        spaces[0]["Block Difficulty"],
        spaces[0]["Quai Reward Offered"],
        spaces[0]["Qi Reward Offered"],
    )
    for bd, quai_rew, qi_rew in zip(bd_l, quai_rew_l, qi_reward_l):
        if quai_rew * state["Quai Price"] >= qi_rew * state["Qi Price"]:
            mined_quai += quai_rew
            quai_hash += bd
            space0["Quai Taken"].append(quai_rew)
            space0["Qi Taken"].append(0)
        else:
            mined_qi += qi_rew
            qi_hash += bd
            space0["Quai Taken"].append(0)
            space0["Qi Taken"].append(qi_rew)

    space1 = {"Qi": mined_qi}
    space2 = {"Quai": mined_quai}
    space3 = {
        "Block Height": state["Block Number"],
        "Ratio": mined_quai / (mined_quai + mined_qi),
    }
    space4 = {
        "Block Height": state["Block Number"],
        "Hash Value": qi_hash,
    }
    space5 = {
        "Block Height": state["Block Number"],
        "Hash Value": quai_hash,
    }
    return [space0, space1, space2, space3, space4, space5]
