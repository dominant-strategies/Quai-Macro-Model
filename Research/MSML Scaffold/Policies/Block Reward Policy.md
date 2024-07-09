---
aliases:
  - block reward function
  - Quai Block Rewards
  - Qi Block Rewards
---

[[Block Reward Space|Quai rewards]] are [[Block Reward Policy|issued]] in proportion to the [[Block Difficulty|“bits” of difficulty]] that a valid [[Block Hash]] achieved, approximately represented by the number of leading zeros in the target value.

$$\text { BlockReward }{ }_{Q u a i} \propto \log _2(\text { Difficulty })$$


[[Block Reward Policy|Qi rewards are issued in direct linear proportion to “hashes” of difficulty,]] or the expected number of hashes needed to [[Mining Wiring|mine a block]] at the current [[Block Difficulty|difficulty]]. If [[Block Difficulty|difficulty]] rises (the expected number of [[Hash Type|hashes]] needed to find a block goes up), the [[Qi Type|Qi]] reward of blocks will also begin to rise. Inversely, if the [[Block Difficulty|difficulty]] lowers (the expected number of [[Hash Type|hashes]] needed to find a block goes down), the [[Qi Type|Qi]] reward of blocks will begin to lower.

$$\text { BlockReward }_{Q i} \propto(\text { Difficulty })$$

## Definition 2

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

## Old Code - Quai/Qi Reward Functions

- From supply.py

    def quaiReward(self):
               
        self.hashController()
        #self.linearController()
        self.quaiRewardVal = 2 ** -(1 + self.kquai) * np.log2(self.diff)
        return self.quaiRewardVal

    def qiReward(self):
        self.qiRewardVal = self.diff/self.kqi
        return self.qiRewardVal