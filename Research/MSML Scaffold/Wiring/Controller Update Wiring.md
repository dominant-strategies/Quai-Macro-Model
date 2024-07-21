## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X3["Controller Update Wiring"]
direction TB
X1["Controller Update Control Action"]
X2["Controller Update Policy"]
X1--"Observable State Space"--->X2
end
```

## Description

Block Type: Stack Block
The wiring for the controller actions
## Components
1. [[Controller Update Control Action]]
2. [[Controller Update Policy]]

## All Blocks
1. [[Controller Update Control Action]]
2. [[Controller Update Policy]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Observable State Space]]

## Parameters Used

## Called By

## Calls

## All State Updates

