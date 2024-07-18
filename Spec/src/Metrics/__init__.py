from .Dummy import metrics_x
from .Hash import metrics_hash
from .Market import metrics_market

metrics = []
metrics.extend(metrics_x)
metrics.extend(metrics_hash)
metrics.extend(metrics_market)
