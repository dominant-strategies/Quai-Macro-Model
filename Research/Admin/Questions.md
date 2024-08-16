## Vesting & Locking

- Some context for the question is [here](https://github.com/BlockScience/Quai-Macro-Model/issues/6)
- Current questions around it are:
    - Is there a choice of lockup that each miner is presented with, i.e. they choose 2 weeks vs. 3 months and what rate of return they will earn?


## Mining

- How does the difficulty compare between different levels of blocks?
- Is there variance to difficulties realized and planned for? Is it always deterministic what reward someone will get from a block or can is vary even given the same difficulty?


## Internal Questions

- Are we OK excluding the growth of the network in terms of size for the MVP simulation model? And if not, how do we want to model it?
- Do we have any strong intuitions on a heuristic that would map nicely to aggregate hashpower? Do we want a linear model of some price of Qi/Quai or something more nuanced?
- To what extent do we want to be modeling prices still? I think at one point we talked about not modeling them at all, but we do have secondary market interactions through conversions, are we definitely thinking of removing them from the MVP model?
- Likewise question for peer-to-peer trading / participants. Are we fine to not model inidividual users with their balances at this point and instead opt just for total amount of Qi and Quai in circulation?
- We currently have [this issue](https://github.com/BlockScience/Quai-Macro-Model/issues/114) for mining impact on price movement
    - If we don't care about price we can drop it
    - If we do, we should talk about how we want it to impact movement. Do we add a distribution of price impact and scale it by amount minted?
    - Do we want anything related to market cap/dilution stuff?
- What behavioral model to we want to employ with relation to conversions that take place each epoch?
- Is $H^i$ meant to represent the global difficulty for setting the prime block difficulty (as well as the difficulties of subprime blocks based on multiples), or is it meant to represent the aggregate hash over all blocks in a prime block?