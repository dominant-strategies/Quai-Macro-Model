## Description

Boundary action which determines the the aggregate hashpower as well as the blocks that need to be mined and their difficulties as well as lock up time for each.
## Called By

## Followed By
1. [[Mining Policy]]

## Constraints

## Codomain Spaces
1. [[Pre-Mining Space]]

## Boundary Action Options:
### 1. Mine Block Boundary Action V1
#### Description
Boundary action for determining the blocks to mine and aggregate hashpower.
#### Logic
1. Aggregate hashpower is a dummy assumption right now equal to 1000 * the Qi Price
    2. Prime blocks, region blocks and zone blocks are created based on network size and their difficulties equal the global difficulty times their difficulty multipliers from the parameters
    3. Noise is added to all the block difficulties as a multiplier from a lognormal distribution with mean 0 and standard deviation of .05
    4. A cumulative sum array is also created of difficulty for ease in computation for the simulation

### 2. Mine Block Boundary Action V2
#### Description
Boundary action for determining the blocks to mine and aggregate hashpower.
#### Logic
1. Aggregate hashpower is pulled from the [[Aggregate Hashpower Series]] parameter
    TBD

### 3. TEST Mine Block Boundary Action
#### Description
Testing function which pulls the aggereagete hashpower and then assigns deterministically the current difficulty to 16 blocks.
#### Logic


### 4. Mine Block Boundary Action V3
#### Description
Current working version of the boundary action for mining a block.
#### Logic
1. Aggregate hashpower is pulled from the [[Aggregate Hashpower Series]] parameter
    2. n_blocks = state["Number of Regions"] ** 2 * state["Zones per Region"] ** 2
    3. Difficulty for blocks is equal to current block difficulty times randomness parameters for block difficulty, total of n_blocks
    4. Randomly select the lockup horizon $H$ with equal probability from the lockup options for each mined block

