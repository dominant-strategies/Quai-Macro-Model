from .Dummy import dummy_letter_count_policy
from .Block import (
    mining_policy_v1,
    block_reward_policy_v1,
    deterministic_mining_payment_policy,
)


policies = {
    "DUMMY Letter Count Policy V1": dummy_letter_count_policy,
    "Mining Policy V1": mining_policy_v1,
    "Block Reward Policy V1": block_reward_policy_v1,
    "Deterministic Mining Payment Policy": deterministic_mining_payment_policy,
}
