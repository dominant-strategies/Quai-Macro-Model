## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X3["Mine Block Wiring"]
direction TB
X1["Mine Block Boundary Action"]
X2["Block Reward Policy"]
X1--"Block Difficulty Space"--->X2
end
```

## Description

Block Type: Stack Block
The wiring for mining a block
## Components
1. [[Mine Block Boundary Action]]
2. [[Block Reward Policy]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Mine Block Boundary Action]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Block Reward Options Space]]

## All Spaces Used
1. [[Block Difficulty Space]]
2. [[Block Reward Options Space]]

## Parameters Used

## Called By

## Calls

## All State Updates

