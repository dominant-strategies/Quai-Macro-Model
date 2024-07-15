[[Proof-of-Work|Work-based protocols]] are simply systems for regulating supply-side production functions in response to observable market demand proxies. These protocols periodically set [[Block Difficulty|difficulty]] and [[Block Reward Policy|block reward values]], establishing a desired or expected rate of block production and new supply issuance based on the estimated [[Hashrate Type|hashrate]] demand deduced from the actual observed [[Block Time|blocktime]] over the prior period. This process then continues across each subsequent period.

The mechanism works by adjusting system values such as [[Block Difficulty|difficulty]] for an upcoming period based on the [[Activity Deviation Metric|previous period of activity's deviation from some expectation or optimization]].

1. [[Block Difficulty|Difficulty]] set to achieve certain [[Block Time|blocktimes]] based on existing [[Hashrate Type|hashrate]]
2. More than expected [[miner]] [[Hashrate Type|hashrate]] deployed
3. Faster [[Block Time|blocktimes]]
4. Increase in system [[Block Difficulty|difficulty]]
5. Harder to [[Mining Wiring|mine a block]]
6. [[Block Time|Blocktimes]] slow toward desired rate

The same flow works in the reverse as well, when less than expected [[miner]] [[Hashrate Type|hashrate]] is deployed, [[Block Time|blocktimes]] slow, and [[Block Difficulty|difficulty]] must be adjusted downwards.

Changes in [[Hashrate Type|hashrate]] are driven by market demand. Simply put, [[Miner|miners]] will deploy more when they’re paid more. With this framing, we can see that mining processes and the [[Block Difficulty|difficulty]] adjustment are best understood as a reactive market supply and demand matching function.

**[[Quai Network]] makes [[Block Difficulty|difficulty]] adjustments on a rolling basis over a previous set of blocks (instead of in sequential periods), to best match the supply of [[Hashrate Type|hashrate]] and demand for network security.


## Scaffolding

Should rely on: 
[[Global State-Current Block Difficulty]]
[[Difficulty Period Parameter]]
[[Global State-Current Hash Difference]]

## Old Code

	    def difficulty(self,market):
	        self.diff = (self.diff * (self.diffPeriod - 1) + market.hashDiff)/self.diffPeriod
	        return self.diff