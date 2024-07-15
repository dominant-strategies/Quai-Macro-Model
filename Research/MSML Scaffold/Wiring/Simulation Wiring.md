## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X7["Simulation Wiring"]
direction TB
subgraph X2["Advance Block Wiring"]
direction TB
X1["Placeholder"]
end
subgraph X4["Controller Update Wiring"]
direction TB
X3["Placeholder"]
end
subgraph X6["Log Simulation Wiring"]
direction TB
X5["Placeholder"]
end
X2--->X4
X4--->X6
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Advance Block Wiring]]
2. [[Controller Update Wiring]]
3. [[Log Simulation Wiring]]

## All Blocks
1. [[Placeholder]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]

## Parameters Used

## Called By

## Calls

## All State Updates

