import numpy as np


def conversion_rate_metric(state, params, spaces):

    hash_val = state["Block Difficulty"]

    quai_reward = state["Metrics"]["Hash to Quai Metric"](
        state, params, [{"Hash": hash_val}]
    )
    qi_reward = state["Metrics"]["Hash to Qi Metric"](
        state, params, [{"Hash": hash_val}]
    )
    ratio = quai_reward / qi_reward * (1 / np.log(hash_val))
    return ratio


def current_block_reward_ratio_metric(state, params, spaces):
    hash_val = state["Block Difficulty"]

    quai_reward = state["Metrics"]["Hash to Quai Metric"](
        state, params, [{"Hash": hash_val}]
    )
    qi_reward = state["Metrics"]["Hash to Qi Metric"](
        state, params, [{"Hash": hash_val}]
    )

    ratio = quai_reward / qi_reward
    return ratio
