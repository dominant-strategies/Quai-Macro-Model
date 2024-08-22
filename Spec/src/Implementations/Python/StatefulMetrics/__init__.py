from .Dummy import dummy_metric
from .Vesting import (
    circulating_quai_supply,
    circulating_qi_supply,
    current_lockup_options,
)

stateful_metrics = {
    "dummy_metric": dummy_metric,
    "Circulating Quai Supply": circulating_quai_supply,
    "Circulating Qi Supply": circulating_qi_supply,
    "Current Lockup Options": current_lockup_options,
}
