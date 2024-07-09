[[Quai Type|Quai]] is a digitally scarce asset designed to function as a programmable store-of-value within [[Quai Network]]. [[Quai Type|Quai]] has an effectively fixed supply in the sense that [[Inflation Metric|inflation]] trends toward zero and there will be a terminal supply amount -- however, [[Token Dynamics - Example Supply Growth|this terminal supply amount will be determined by market dynamics, and is not predefined]]

[[Quai Type|Quai]] is the native token of the account-based [[Execution Shard|shards]] within [[Quai Network]], supporting [[Smart Contract|smart-contracting]] capabilities with modified [[Ethereum Virtual Machine|EVMs]].

## [[Quai Type|Quai]] [[Emissions]]

[[Block Reward Space|Quai rewards]] are [[Block Reward Policy|issued]] in proportion to the [[Block Difficulty|“bits” of difficulty]] that a valid [[block hash]] achieved, approximately represented by the number of leading zeros in the target value.

$$\text { BlockReward }{ }_{Q u a i} \propto \log _2(\text { Difficulty })$$

Note that there is a proportionality constant/variable in the Quai block reward function above, the exact calculus for which will be shared publicly closer to Mainnet launch.

## [[Quai Supply Metric|Quai Supply]]

The [[Quai Supply Metric|supply of Quai]] is determined by the following formula:

$$\text { Supply }_{Q u a i}=\left(\text { Genesis }_{Q u a i}\right)+\sum\left(\text { Emissions }_{Q u a i}\right) \pm \sum\left(\text { Conversions }_{Q u a i}\right)$$
## Description

The [[Block Reward Policy|block reward function]] only defines how many [[Quai Type|Quai]] tokens can _potentially_ be emitted. Actual, realized supply [[emissions]] from block rewards are determined by the [[Mining Payment Policy|choices miners must make to receive only either Quai or Qi]], a selection they may change going forward at any time.

In addition to the effects from this new flow of [[Quai Type|Quai]] and/or [[Qi Type|Qi]] issuance, the respective supply stock of Quai is affected by the [[Genesis Quai Parameter|initial genesis allocation of Quai]] and the [[Controller Exchange Rate Wiring|conversion feature between existing Qi and Quai]] at the current [[Block Mining Rewards Ratio Metric|block mining rewards ratio]] (e.g. between the # of Quai tokens/block and # of Qi tokens/block), which is accessible to anyone -- not just [[Miner|miners]].

As such, the supply of Quai at any given time is the cumulative result of the [genesis allocation](https://qu.ai/docs/learn/tokenomics/genesis-allocations/), [miner-selected emissions](https://qu.ai/docs/learn/tokenomics/token-dynamics/block-rewards/), and [token conversions](https://qu.ai/docs/learn/tokenomics/token-dynamics/conversions/).