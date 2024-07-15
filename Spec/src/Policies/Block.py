block_reward_policy_option1 = {
    "name": "Block Reward Policy V1",
    "description": r"Basic policy option which uses the $k_{Quai}$ and $k_{Qi}$",
    "logic": r"""The following are the computations for the offered rewards in Quai and Qi:
1. d = DOMAIN[0]["Block Difficulty"]
2. $Qi = \frac{d}{k_{Qi}}$
3. $Quai = 2^{-(1+k_{Quai})} \cdot \log_2(d)$
4. Return spaces of [{"Quai Reward Offered": Quai,
        "Qi Reward Offered": Qi,
        "Block Difficulty": d}]""",
}

block_reward_policy = {
    "name": "Block Reward Policy",
    "description": r"""[[Block Reward Policy|Quai block rewards]] are proportional to [[Block Difficulty|"bits" of difficulty]], which can be approximately represented by the number of leading zeros in each [[Hash Type|hash]] that "finds" a valid block. [[Quai Type|Quai]] has an effectively fixed supply, as [[Quai Inflation Rate Metric|inflation]] trends towards zero over time.
$$
\text { BlockReward }_{Q u a i} \propto \log _2 \text { (Difficulty) }
$$

[[Qi Type|Qi]] block rewards are linearly proportional to "[[Hash Type|hashes]]" of [[Block Difficulty|difficulty]], or the expected number of [[Hash Type|hashes]] needed to [[Mining Wiring|mine a block]] at the current difficulty.
$$
\text { BlockReward }_{Q i} \propto(\text { Difficulty })
$$

This logarithmic versus linear relationship produces the significant difference between [[Quai Type|Quai]] scarcity and [[Qi Type|Qi]] expansion. For every doubling ( $2 \mathrm{x})$ in [[Block Difficulty|difficulty]] or [[Hash Type|hashes]], there is only one added unit ( +1 ) in bits. Over time, this ensures [[Quai Type|Quai]]'s scarcity, while [[Qi Type|Qi]] is naturally connected to the [[Miner]] cost of production and thus functions as a loose measure of energy or electricity pricing.

Importantly, these block reward functions only define how many Quai/Qi tokens can potentially be emitted. Actual, realized supply emissions from block rewards are determined by the choices miners must make to receive only either Quai or Qi, a selection they may change going forward at any time.""",
    "constraints": [],
    "policy_options": [block_reward_policy_option1],
    "domain": ["Block Difficulty Space"],
    "codomain": ["Block Reward Options Space"],
    "parameters_used": [],
    "metrics_used": [],
}

mining_payment_policy_option1 = {
    "name": "Deterministic Mining Payment Policy",
    "description": "User chooses either all Qi or all Quai based on which is more valuable.",
    "logic": "Compare the price of Qi times Qi amount to price of Quai times Quai amount and pick the larger sum.",
}

mining_payment_policy = {
    "name": "Mining Payment Policy",
    "description": "Policy which determines what amount of Quai vs. Qi is taken as payment.",
    "constraints": [],
    "policy_options": [mining_payment_policy_option1],
    "domain": ["Block Reward Options Space"],
    "codomain": [],  # ["Block Reward Space"],
    "parameters_used": [],
    "metrics_used": [],
}


block_policies = [block_reward_policy, mining_payment_policy]
