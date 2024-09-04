from .Dummy import dummy_letter_count_policy
from .Block import (
    mining_policy_v1,
    block_reward_policy_v1,
    deterministic_mining_payment_policy,
    logistic_probability_payment_policy,
)
from .Market import block_reward_ratio_conversion_policy, price_movements_policy_v1
from .Vesting import unlock_tokens_policy_v1
from .Controller import (
    sgd_logistic_classifier_training,
    reward_ratio_gain,
    mezzanine_wiring_passthrough,
    rolling_logistic_regression_estimation,
)
from .User import update_population_beta_policy_passthrough

policies = {
    "DUMMY Letter Count Policy V1": dummy_letter_count_policy,
    "Mining Policy V1": mining_policy_v1,
    "Block Reward Policy V1": block_reward_policy_v1,
    "Deterministic Mining Payment Policy": deterministic_mining_payment_policy,
    "Block Reward Ratio Conversion Policy": block_reward_ratio_conversion_policy,
    "Price Movements Policy V1": price_movements_policy_v1,
    "Unlock Tokens Policy V1": unlock_tokens_policy_v1,
    "Logistic Probability Payment Policy": logistic_probability_payment_policy,
    "SGD Logistic Classifier Training": sgd_logistic_classifier_training,
    "Reward Ratio Gain": reward_ratio_gain,
    "Mezzanine Wiring Passthrough": mezzanine_wiring_passthrough,
    "Update Population Beta Policy Passthrough": update_population_beta_policy_passthrough,
    "Rolling Logistic Regression Estimation": rolling_logistic_regression_estimation,
}
