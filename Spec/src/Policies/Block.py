block_reward_policy_option1 = {
    "name": "Block Reward Policy V1",
    "description": r"Basic policy option which uses the $k_{Quai}$ and $k_{Qi}$",
    "logic": r"""The following are the computations for the offered rewards in Quai and Qi, we denote the parameter Quai Reward Base Parameter as B:
1. d = difficulty for a given block
2. $Qi = \frac{d}{k_{Qi}}$
3. $Quai = B^{-(1+k_{Quai})} \cdot \log_B(d)$
4. Return spaces of [{"Quai Reward Offered": Quai,
        "Qi Reward Offered": Qi,
        "Block Difficulty": d}]
        
These computations are done for each of the blocks presented from the DOMAIN""",
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
    "domain": ["Mined Blocks Space"],
    "codomain": ["Block Reward Options Space"],
    "parameters_used": ["Quai Reward Base Parameter"],
    "metrics_used": [],
}

mining_payment_policy_option1 = {
    "name": "Deterministic Mining Payment Policy",
    "description": "User chooses either all Qi or all Quai based on which is more valuable based on USD prices.",
    "logic": """Compare the price of Qi times Qi amount to price of Quai times Quai amount and pick the larger sum. Then the values for each iteration loop are as follows:
1. Qi Space is equal to 0 or the Qi amount
2. Quai Space is equal to 0 or the Quai amount
3. Mined Ratio Space has 0 if Qi was chosen, 1 if Quai was chosen
4. Qi Hash Space has 0 if Quai was chosen, otherwise $QiToHashMetric(Qi)$
5. Quai Hash Space has 0 if Qi was chosen, otherwise $QuaiToHashMetric(Quai)$
6. The first space passed out before those 5 will be a copy of the domain space filled in with the options chosen by each miner""",
}

mining_payment_policy = {
    "name": "Mining Payment Policy",
    "description": "Policy which determines what amount of Quai vs. Qi is taken as payment.",
    "constraints": [],
    "policy_options": [mining_payment_policy_option1],
    "domain": ["Block Reward Options Space"],
    "codomain": [
        "Mined Blocks Space 2",
        "Qi Space",
        "Quai Space",
        "Mined Ratio Space",
        "Qi Hash Space",
        "Quai Hash Space",
    ],
    "parameters_used": [],
    "metrics_used": ["Qi to Hash Metric", "Quai to Hash Metric"],
}

mezzanine_wiring_passthrough = {
    "name": "Mezzanine Wiring Passthrough",
    "description": "Policy which passes through the spaces for the mezzanine wiring.",
    "constraints": [],
    "policy_options": [],
    "domain": [
        "Qi Space",
        "Quai Space",
        "Mined Ratio Space",
        "Qi Hash Space",
        "Quai Hash Space",
    ],
    "codomain": [
        "Qi Space",
        "Quai Space",
        "Mined Ratio Space",
        "Qi Hash Space",
        "Quai Hash Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}


mining_policy_v1 = {
    "name": "Mining Policy V1",
    "description": "A baseline mining policy",
    "logic": """1. Create a space with no attributes
2. Assign the "Block Difficulty" as the array of difficulties presented in the domain
3. Add an attribute for "Mining Time" which is the sum of block difficulties / the aggregate hashpower taken from the domain
4. Find the new block difficulty by TBD""",
}


mining_policy = {
    "name": "Mining Policy",
    "description": "Policy for mining and how long it takes to mine as well as difficulty adjustment.",
    "constraints": [],
    "policy_options": [mining_policy_v1],
    "domain": ["Pre-Mining Space"],
    "codomain": ["Mined Blocks Space"],
    "parameters_used": [],
    "metrics_used": [],
}


block_policies = [
    block_reward_policy,
    mining_payment_policy,
    mining_policy,
    mezzanine_wiring_passthrough,
]
