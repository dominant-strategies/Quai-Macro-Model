## Vesting & Locking

- Some context for the question is [here](https://github.com/BlockScience/Quai-Macro-Model/issues/6)
- Current questions around it are:
    - Confirming that the unlock schedule is going to be that there is 100% unlock right at the unlock time (as opposed to linear vesting)
    - Is it ok to not model initial allocations vesting over time (the tokens to founders and investors)? And if it does need to be modeled, is it going to be based on linear vesting?
    - Is there a choice of lockup that each miner is presented with, i.e. they choose 2 weeks vs. 3 months and what rate of return they will earn?

## Conversions

- Does the treasury ever hold balances or is everything passed straight through to minting/burning mechanisms?
- Are there any fees (constant or dynamic) that we should make sure is represented? 

## Mining

- How does the difficulty compare between different levels of blocks?
- Is there variance to difficulties realized and planned for? Is it always deterministic what reward someone will get from a block or can is vary even given the same difficulty?
- Do all instances of the prime, zone and region blocks need to get mined each time or are there situations in which a prime block only has partial filling from these levels?
- If a prime block has not been mined in X amount of time, does difficulty then adjust down or is it that once it eventually is mined the difficulty is adjusted downwards?