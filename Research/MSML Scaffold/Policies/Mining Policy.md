## Description

Policy for mining and how long it takes in terms of epochs and also the time epochs take.
## Called By
1. [[Mine Block Boundary Action]]
## Domain Spaces
1. [[Pre-Mining Space]]
## Followed By
1. [[Block Reward Policy]]
## Codomain Spaces
1. [[Mined Blocks Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Mining Policy V1
#### Description
A baseline mining policy
#### Logic
Until all blocks are mined the following while loop continues:
1. Given hashpower and the target mining time (parameter), see how many blocks can be mined. If prime block is mined cut the time at target time, otherwise compute the time taken for mining all the blocks.
2. Pass the time taken to difficulty adjustment which if time taken was < .8 of target time will increase difficulty, or if it was equal to target time will decrease difficulty. Block difficulties leftover still are adjusted by this amount.
The final returned object will have the epochs (only 1 if prime block is mined in the first epoch) as well as the final new difficulty after any adjustments

