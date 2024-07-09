---
aliases:
  - block reward function
---

[[Block Reward Space|Quai rewards]] are [[Block Reward Policy|issued]] in proportion to the [[Block Difficulty|“bits” of difficulty]] that a valid [[block hash]] achieved, approximately represented by the number of leading zeros in the target value.

$$\text { BlockReward }{ }_{Q u a i} \propto \log _2(\text { Difficulty })$$


[[Block Reward Policy|Qi rewards are issued in direct linear proportion to “hashes” of difficulty,]] or the expected number of hashes needed to mine a block at the current [[Block Difficulty|difficulty]]. If [[Block Difficulty|difficulty]] rises (the expected number of hashes needed to find a block goes up), the [[Qi Type|Qi]] reward of blocks will also begin to rise. Inversely, if the [[Block Difficulty|difficulty]] lowers (the expected number of hashes needed to find a block goes down), the Qi reward of blocks will begin to lower.

$$\text { BlockReward }_{Q i} \propto(\text { Difficulty })$$
