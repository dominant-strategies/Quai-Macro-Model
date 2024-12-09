import numpy as np
from random import choice
from scipy.stats import norm


def create_block_hashes_v1(state, params):

    # Get the baseline block difficulties without randomness
    prime_block_hashes = [
        state["Block Difficulty"] * params["Block Difficulty Multiples"]["Prime"]
    ]
    region_block_hashes = [
        state["Block Difficulty"] * params["Block Difficulty Multiples"]["Region"]
    ] * state["Number of Regions"]
    zone_block_hashes = (
        [state["Block Difficulty"] * params["Block Difficulty Multiples"]["Zone"]]
        * state["Number of Regions"]
        * state["Zones per Region"]
    )

    # Merge and order
    block_hashes = []
    types = []
    while len(region_block_hashes) > 0:
        for _ in range(state["Zones per Region"]):
            types.append("Zone")
            block_hashes.append(zone_block_hashes.pop())
        block_hashes.append(region_block_hashes.pop())
        types.append("Region")
    block_hashes.append(prime_block_hashes.pop())
    types.append("Prime")

    # Add in randomness
    block_hashes = np.array(block_hashes)
    mutlipliers = np.random.lognormal(0, 0.05, len(block_hashes))
    block_hashes = block_hashes * mutlipliers
    block_hashes = block_hashes.round().astype(int)

    # Get cumulative sum for later computation of how far the aggregate hash rate gets us
    block_hashes_cs = np.cumsum(block_hashes)

    block_hashes = [
        {"Difficulty": x, "Block Type": y} for x, y in zip(block_hashes, types)
    ]

    return block_hashes, block_hashes_cs


def create_aggregate_hashpower_v1(state, params):
    return 1000 * state["Qi Price"]


def mine_block_boundary_action_v1(state, params, spaces):
    space = {}
    space["Aggregate Hashpower"] = create_aggregate_hashpower_v1(state, params)
    space["Blocks to Mine"], space["Block Hash Cumulative Sum"] = (
        create_block_hashes_v1(state, params)
    )
    return [space]


def mine_block_boundary_action_v2(state, params, spaces):
    space = {}
    space["Aggregate Hashpower"] = params["Aggregate Hashpower Series"][
        state["Block Number"]
    ]
    space["Blocks to Mine"], space["Block Hash Cumulative Sum"] = (
        create_block_hashes_v1(state, params)
    )
    return [space]


def test_mine_block_boundary_action(state, params, spaces):
    space = {}
    space["Aggregate Hashpower"] = params["Aggregate Hashpower Series"][
        state["Block Number"]
    ]

    space["Blocks to Mine"] = [
        {"Difficulty": state["Block Difficulty"]} for _ in range(16)
    ]
    return [space]

def mine_block_boundary_action_v3(state, params, spaces):
    space = {}

    n_blocks = state["Number of Regions"] ** 2 * state["Zones per Region"] ** 2

    space["Blocks to Mine"] = []

    space["Quai Reward"] = []
    space["Qi Reward"] = []

    # set the block difficulty to the difficulty of the last block from the
    # previous epoch
    block_difficulty = state["Block Difficulty"]

    for _ in range(n_blocks):

        quai_reward = state["Metrics"]["Hash to Quai Metric"](state, params, [{"Hash": block_difficulty}])
        qi_reward = state["Metrics"]["Hash to Qi Metric"](state, params, [{"Hash": block_difficulty}])

        reward = 0
        # Make the miner decision of what to mine
        if quai_reward * state["Quai Price"] > qi_reward * state["Qi Price"]:
            space["Quai Reward"].append(quai_reward)
            space["Qi Reward"].append(0)
            reward = quai_reward / (state["K Quai"] * block_difficulty) # Qi per Hash Unit
        else:
            space["Quai Reward"].append(0)
            space["Qi Reward"].append(qi_reward)
            reward = qi_reward / block_difficulty # Qi per Hash Unit
        
        z_value_for_cost = (params["Hashpower Cost Series"][state["Block Number"]] - reward)/params["Hashpower Cost Series Sigma"]

        percent_interested_in_mining = norm.cdf(z_value_for_cost) * 100

        # If the percent interested in mining is significantly greater than 50 increase the
        # population hash rate that is mining by a 0.1, otherwise decrease
        # it by 0.1 percent
        if percent_interested_in_mining > 75:
            state["Population Mining Hashrate"] = state["Population Mining Hashrate"] * 1.001
        elif percent_interested_in_mining < 25:
            state["Population Mining Hashrate"] = state["Population Mining Hashrate"] * 0.999


        # calculate the new lambda for the new new block sample
        lam = block_difficulty / (state["Population Mining Hashrate"] * percent_interested_in_mining)
        time_to_find_block = np.random.poisson(lam=lam, size=1)

        target_time = params["Target Mining Time"]

        new_difficulty = (
            block_difficulty
            + 0.001
            * ((target_time - time_to_find_block[0]) / target_time)
            * block_difficulty
        )

        # update the block difficulty variable to the newly calculated block difficulty
        block_difficulty = new_difficulty

        space["Blocks to Mine"].append({"Difficulty": block_difficulty})
    
    space["Aggregate Hashpower"] = state["Population Mining Hashrate"]

    L = state["Stateful Metrics"]["Current Lockup Options"](state, params)
    H = list(L.keys())
    space["Locking Times"] = [choice(H) for _ in range(n_blocks)]
    return [space]


def do_not_use_print_hello(state, params, spaces):
    print("HELLO")
    return []
