## Description

[[Block Reward Policy|Quai block rewards]] are proportional to [[Block Difficulty|"bits" of difficulty]], which can be approximately represented by the number of leading zeros in each [[Hash Type|hash]] that "finds" a valid block. [[Quai Type|Quai]] has an effectively fixed supply, as [[Quai Inflation Rate Metric|inflation]] trends towards zero over time.
$$
\text { BlockReward }_{Q u a i} \propto \log _2 \text { (Difficulty) }
$$

[[Qi Type|Qi]] block rewards are linearly proportional to "[[Hash Type|hashes]]" of [[Block Difficulty|difficulty]], or the expected number of [[Hash Type|hashes]] needed to [[Mining Wiring|mine a block]] at the current difficulty.
$$
\text { BlockReward }_{Q i} \propto(\text { Difficulty })
$$

This logarithmic versus linear relationship produces the significant difference between [[Quai Type|Quai]] scarcity and [[Qi Type|Qi]] expansion. For every doubling ( $2 \mathrm{x})$ in [[Block Difficulty|difficulty]] or [[Hash Type|hashes]], there is only one added unit ( +1 ) in bits. Over time, this ensures [[Quai Type|Quai]]'s scarcity, while [[Qi Type|Qi]] is naturally connected to the [[Miner]] cost of production and thus functions as a loose measure of energy or electricity pricing.

Importantly, these block reward functions only define how many Quai/Qi tokens can potentially be emitted. Actual, realized supply emissions from block rewards are determined by the choices miners must make to receive only either Quai or Qi, a selection they may change going forward at any time.
## Called By
1. [[Mine Block Boundary Action]]
## Domain Spaces
1. [[Block Difficulty Space]]
## Followed By
1. [[Mining Payment Policy]]
## Codomain Spaces
1. [[Block Reward Options Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Block Reward Policy V1
#### Description
Basic policy option which uses the $k_{Quai}$ and $k_{Qi}$
#### Logic
The following are the computations for the offered rewards in Quai and Qi:
1. d = DOMAIN[0]["Block Difficulty"]
2. $Qi = \frac{d}{k_{Qi}}$
3. $Quai = 2^{-(1+k_{Quai})} \cdot \log_2(d)$
4. Return spaces of [{"Quai Reward Offered": Quai,
        "Qi Reward Offered": Qi,
        "Block Difficulty": d}]

