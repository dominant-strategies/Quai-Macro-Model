## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Block Number"])
EES0 --- EE0
EES1(["Historical Converted Qi"])
EES1 --- EE0
EES2(["Historical Converted Quai"])
EES2 --- EE0
EES3(["Historical Mined Ratio"])
EES3 --- EE0
EES4(["Historical Qi Hash"])
EES4 --- EE0
EES5(["K Qi"])
EES5 --- EE0
EES6(["K Quai"])
EES6 --- EE0
EES7(["Qi Supply"])
EES7 --- EE0
EES8(["Quai Supply"])
EES8 --- EE0
end

subgraph X34["Simulation Wiring"]
direction TB
subgraph X2["Price Movements Wiring"]
direction TB
X1["Placeholder"]
end
subgraph X14["Conversions Wiring"]
direction TB
X3["Conversions Boundary Action"]
X4["Conversions Policy"]
subgraph X13["Conversions Mechanisms Wiring"]
direction TB
X5["Mint Qi Tokens Mechanism"]
X5 --> EES7
X6["Mint Quai Tokens Mechanism"]
X6 --> EES8
X7["Burn Qi Tokens Mechanism"]
X7 --> EES7
X8["Burn Quai Tokens Mechanism"]
X8 --> EES8
X9["Update Historical Converted Qi Mechanism"]
X9 --> EES1
X10["Update Historical Converted Quai Mechanism"]
X10 --> EES2
X11[Domain]

direction LR
direction TB
X11 --"Qi Space"--> X5
X11 --"Quai Space"--> X6
X11 --"Qi Space"--> X7
X11 --"Quai Space"--> X8
X11 --"Conversion Log Space"--> X9
X11 --"Conversion Log Space"--> X10
end
X3--"Conversion Space"--->X4
X4--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space"-------->X13
end
subgraph X27["Mine Block Wiring"]
direction TB
X15["Mine Block Boundary Action"]
X16["Block Reward Policy"]
X17["Mining Payment Policy"]
subgraph X26["Mining Mechanisms"]
direction TB
X18["Increment Block Number Mechanism"]
X18 --> EES0
X19["Mint Qi Tokens Mechanism"]
X19 --> EES7
X20["Mint Quai Tokens Mechanism"]
X20 --> EES8
X21["Update Historical Mined Ratio Mechanism"]
X21 --> EES3
X22["Update Historical Qi Hash Mechanism"]
X22 --> EES4
X23["Update Historical Quai Hash Mechanism"]
X23 --> EES4
X24[Domain]

direction LR
direction TB
X24 --> X18
X24 --"Qi Space"--> X19
X24 --"Quai Space"--> X20
X24 --"Mined Ratio Space"--> X21
X24 --"Qi Hash Space"--> X22
X24 --"Quai Hash Space"--> X23
end
X15--"Block Difficulty Space"--->X16
X16--"Block Reward Options Space"--->X17
X17--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X26
end
subgraph X31["Controller Update Wiring"]
direction TB
X28["Controller Update Control Action"]
X29["Controller Update Policy"]
X30["Set K Mechanism"]
X30 --> EES6
X30 --> EES5
X28--"Observable State Space"--->X29
X29--"K Space"--->X30
end
subgraph X33["Log Simulation Wiring"]
direction TB
X32["Placeholder"]
end
X2--->X14
X14--->X27
X27--->X31
X31--->X33
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Conversions Wiring]]
3. [[Mine Block Wiring]]
4. [[Controller Update Wiring]]
5. [[Log Simulation Wiring]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Burn Qi Tokens Mechanism]]
3. [[Burn Quai Tokens Mechanism]]
4. [[Controller Update Control Action]]
5. [[Controller Update Policy]]
6. [[Conversions Boundary Action]]
7. [[Conversions Policy]]
8. [[Increment Block Number Mechanism]]
9. [[Mine Block Boundary Action]]
10. [[Mining Payment Policy]]
11. [[Mint Qi Tokens Mechanism]]
12. [[Mint Quai Tokens Mechanism]]
13. [[Placeholder]]
14. [[Set K Mechanism]]
15. [[Update Historical Converted Qi Mechanism]]
16. [[Update Historical Converted Quai Mechanism]]
17. [[Update Historical Mined Ratio Mechanism]]
18. [[Update Historical Qi Hash Mechanism]]
19. [[Update Historical Quai Hash Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Block Difficulty Space]]
2. [[Block Reward Options Space]]
3. [[Conversion Log Space]]
4. [[Conversion Space]]
5. [[Empty Space]]
6. [[K Space]]
7. [[Mined Ratio Space]]
8. [[Observable State Space]]
9. [[Qi Hash Space]]
10. [[Qi Space]]
11. [[Quai Hash Space]]
12. [[Quai Space]]
13. [[Terminating Space]]

## Parameters Used
1. [[Minimum Qi Conversion Amount]]
2. [[Minimum Quai Conversion Amount]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
3. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
4. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
5. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
6. [[Global]].[[Global State-K Qi|K Qi]]
7. [[Global]].[[Global State-K Quai|K Quai]]
8. [[Global]].[[Global State-Qi Supply|Qi Supply]]
9. [[Global]].[[Global State-Quai Supply|Quai Supply]]

