## Description

Boundary action which determines the update of the current population beta.
## Called By

## Followed By
1. [[Update Population Beta Policy]]

## Constraints

## Codomain Spaces
1. [[Beta Vector Space]]

## Boundary Action Options:
### 1. Update Population Beta Boundary Action Signal
#### Description
Signal based approach that picks the current index of the block as the signal for population beta update
#### Logic
Return the population beta from PARAMS['Population Beta Signal'][state['Block Number']]

