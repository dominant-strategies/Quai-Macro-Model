from .Dummy import dummy_metric
from .Vesting import circulating_quai_supply, circulating_qi_supply

stateful_metrics = {
    "dummy_metric": dummy_metric,
    "Circulating Quai Supply": circulating_quai_supply,
    "Circulating Qi Supply": circulating_qi_supply,
}
