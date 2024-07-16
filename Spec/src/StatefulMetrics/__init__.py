from .Dummy import dummy_stateful_metrics
from .BlockReward import block_reward_stateful_metrics

stateful_metrics = []
stateful_metrics.extend(dummy_stateful_metrics)
stateful_metrics.extend(block_reward_stateful_metrics)
