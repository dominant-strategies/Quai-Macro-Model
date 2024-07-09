---
aliases:
  - Quai Supply
---


## Functional Form

$$\text { Supply }_{Q u a i}=\left(\text { Genesis }_{Q u a i}\right)+\sum\left(\text { Emissions }_{Q u a i}\right) \pm \sum\left(\text { Conversions }_{Q u a i}\right)$$

The metric will be based on the [[Genesis Quai Parameter]] and outputs from both the [[Block Reward Policy]] and [[Conversions Wiring]].

## Description

The [[Block Reward Policy|block reward function]] only defines how many [[Quai Type|Quai]] tokens can _potentially_ be emitted. Actual, realized supply [[emissions]] from block rewards are determined by the [[Mining Payment Policy|choices miners must make to receive only either Quai or Qi]], a selection they may change going forward at any time.

In addition to the effects from this new flow of [[Quai Type|Quai]] and/or [[Qi Type|Qi]] issuance, the respective supply stock of Quai is affected by the [[Genesis Quai Parameter|initial genesis allocation of Quai]] and the [[Controller Exchange Rate Wiring|conversion feature between existing Qi and Quai]] at the current [[Block Mining Rewards Ratio Metric|block mining rewards ratio]] (e.g. between the # of Quai tokens/block and # of Qi tokens/block), which is accessible to anyone -- not just [[Miner|miners]].

As such, the supply of Quai at any given time is the cumulative result of the [genesis allocation](https://qu.ai/docs/learn/tokenomics/genesis-allocations/), [miner-selected emissions](https://qu.ai/docs/learn/tokenomics/token-dynamics/block-rewards/), and [token conversions](https://qu.ai/docs/learn/tokenomics/token-dynamics/conversions/).