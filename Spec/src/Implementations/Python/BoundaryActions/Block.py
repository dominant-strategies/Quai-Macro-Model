import numpy as np
from random import choice


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
    space["Aggregate Hashpower"] = params["Aggregate Hashpower Series"][
        state["Block Number"]
    ]

    n_blocks = state["Number of Regions"] ** 2 * state["Zones per Region"] ** 2

    space["Blocks to Mine"] = [
        {
            "Difficulty": state["Block Difficulty"]
            * max(
                np.random.normal(
                    params["Difficulty Randomness Mu"],
                    params["Difficulty Randomness Sigma"],
                ),
                0.01,
            )
        }
        for _ in range(n_blocks)
    ]
    L = state["Stateful Metrics"]["Current Lockup Options"](state, params)
    H = list(L.keys())
    space["Locking Times"] = [choice(H) for _ in range(n_blocks)]
    return [space]
