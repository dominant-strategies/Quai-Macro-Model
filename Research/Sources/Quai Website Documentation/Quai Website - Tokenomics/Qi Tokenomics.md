[[Qi Type|Qi]] is a token designed to enable and scale the use of cryptocurrency as a unit measure and medium of exchange within [[Quai Network]]. [[Qi Type|Qi]] has a highly responsive and accommodative supply, with an [[Qi Issuance Rate Metric|issuance]] and [[Qi Inflation Rate Metric|inflation rate]] in direct proportion to demand.

[[Qi Type|Qi]] is the native token of the [[UTXO Execution Shard|UTXO shards]] within [[Quai Network]], with fixed denominations and no scripting capabilities.

## [[Qi Type|Qi]] [[Emissions]][​](https://qu.ai/docs/learn/tokenomics/tokenomics-overview/qi/#qi-emissions "Direct link to Qi Emissions")

[[Block Reward Policy|Qi rewards are issued in direct linear proportion to “hashes” of difficulty,]] or the expected number of hashes needed to mine a block at the current [[Block Difficulty|difficulty]]. If [[Block Difficulty|difficulty]] rises (the expected number of hashes needed to find a block goes up), the [[Qi Type|Qi]] reward of blocks will also begin to rise. Inversely, if the [[Block Difficulty|difficulty]] lowers (the expected number of hashes needed to find a block goes down), the Qi reward of blocks will begin to lower.

$$\text { BlockReward }_{Q i} \propto(\text { Difficulty })$$


Note that there is a proportionality constant/variable in the Qi [block reward](https://qu.ai/docs/learn/tokenomics/token-dynamics/block-rewards/) function above, the exact calculus for which will be shared publicly closer to Mainnet launch.

## [[Qi Supply Metric|Qi Supply]]

The supply of [[Qi Type|Qi]] is determined by the following formula:

$$\text { Supply }{ }_{Q i}=\sum\left(\text { Emissions }_{Q i}\right) \pm \sum\left(\text { Conversions }_{Q i}\right)$$

The [[Block Reward Policy|block reward function]] only defines how many [[Qi Type|Qi]] tokens can _potentially_ be emitted. Actual, realized supply [[emissions]] from block rewards are determined by the [[Mining Payment Policy|choices miners must make to receive only either Quai or Qi, a selection they may change going forward at any time]].

In addition to the effects from this new flow of Quai and/or Qi issuance, the respective supply stock of [[Qi Type|Qi]] is affected by the [[Conversions Wiring|conversion feature between existing Qi and Quai]] at the current [[Current Block Reward Ratio Metric|block mining rewards ratio]] (e.g. between the # of [[Quai Type|Quai]] tokens/block and # of [[Qi Type|Qi]] tokens/block), which is accessible to anyone -- not just miners.

As such, the supply of Qi at any given time is the cumulative result of [miner-selected emissions](https://qu.ai/docs/learn/tokenomics/token-dynamics/block-rewards/) and [token conversions](https://qu.ai/docs/learn/tokenomics/token-dynamics/conversions/).