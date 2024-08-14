from .Reward import (
    qi_to_hash_metric,
    quai_to_hash_metric,
    hash_to_qi_metric,
    hash_to_quai_metric,
)

metrics = {
    "Qi to Hash Metric": qi_to_hash_metric,
    "Quai to Hash Metric": quai_to_hash_metric,
    "Hash to Qi Metric": hash_to_qi_metric,
    "Hash to Quai Metric": hash_to_quai_metric,
}
