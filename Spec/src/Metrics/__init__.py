from .Hash import metrics_hash
from .Market import metrics_market
from .Rewards import metrics_rewards

metrics = []
metrics.extend(metrics_hash)
metrics.extend(metrics_market)
metrics.extend(metrics_rewards)
