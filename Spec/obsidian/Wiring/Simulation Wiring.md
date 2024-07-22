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
EES7(["Qi Price"])
EES7 --- EE0
EES8(["Qi Supply"])
EES8 --- EE0
EES9(["Quai Price"])
EES9 --- EE0
EES10(["Quai Supply"])
EES10 --- EE0
end

subgraph X36["Simulation Wiring"]
direction TB
subgraph X4["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X3["Update Prices Mechanism"]
X3 --> EES9
X3 --> EES7
X1--"Price Movement Space"--->X2
X2--"Price Space"--->X3
end
subgraph X16["Conversions Wiring"]
direction TB
X5["Conversions Boundary Action"]
X6["Conversions Policy"]
subgraph X15["Conversions Mechanisms Wiring"]
direction TB
X7["Mint Qi Tokens Mechanism"]
X7 --> EES8
X8["Mint Quai Tokens Mechanism"]
X8 --> EES10
X9["Burn Qi Tokens Mechanism"]
X9 --> EES8
X10["Burn Quai Tokens Mechanism"]
X10 --> EES10
X11["Update Historical Converted Qi Mechanism"]
X11 --> EES1
X12["Update Historical Converted Quai Mechanism"]
X12 --> EES2
X13[Domain]

direction LR
direction TB
X13 --"Qi Space"--> X7
X13 --"Quai Space"--> X8
X13 --"Qi Space"--> X9
X13 --"Quai Space"--> X10
X13 --"Conversion Log Space"--> X11
X13 --"Conversion Log Space"--> X12
end
X5--"Conversion Space"--->X6
X6--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space"-------->X15
end
subgraph X29["Mine Block Wiring"]
direction TB
X17["Mine Block Boundary Action"]
X18["Block Reward Policy"]
X19["Mining Payment Policy"]
subgraph X28["Mining Mechanisms"]
direction TB
X20["Increment Block Number Mechanism"]
X20 --> EES0
X21["Mint Qi Tokens Mechanism"]
X21 --> EES8
X22["Mint Quai Tokens Mechanism"]
X22 --> EES10
X23["Update Historical Mined Ratio Mechanism"]
X23 --> EES3
X24["Update Historical Qi Hash Mechanism"]
X24 --> EES4
X25["Update Historical Quai Hash Mechanism"]
X25 --> EES4
X26[Domain]

direction LR
direction TB
X26 --> X20
X26 --"Qi Space"--> X21
X26 --"Quai Space"--> X22
X26 --"Mined Ratio Space"--> X23
X26 --"Qi Hash Space"--> X24
X26 --"Quai Hash Space"--> X25
end
X17--"Block Difficulty Space"--->X18
X18--"Block Reward Options Space"--->X19
X19--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X28
end
subgraph X33["Controller Update Wiring"]
direction TB
X30["Controller Update Control Action"]
X31["Controller Update Policy"]
X32["Set K Mechanism"]
X32 --> EES6
X32 --> EES5
X30--"Observable State Space"--->X31
X31--"K Space"--->X32
end
subgraph X35["Log Simulation Wiring"]
direction TB
X34["Placeholder"]
end
X4--->X16
X16--->X29
X29--->X33
X33--->X35
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
14. [[Price Movements Boundary Action]]
15. [[Price Movements Policy]]
16. [[Set K Mechanism]]
17. [[Update Historical Converted Qi Mechanism]]
18. [[Update Historical Converted Quai Mechanism]]
19. [[Update Historical Mined Ratio Mechanism]]
20. [[Update Historical Qi Hash Mechanism]]
21. [[Update Historical Quai Hash Mechanism]]
22. [[Update Prices Mechanism]]

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
9. [[Price Movement Space]]
10. [[Price Space]]
11. [[Qi Hash Space]]
12. [[Qi Space]]
13. [[Quai Hash Space]]
14. [[Quai Space]]
15. [[Terminating Space]]

## Parameters Used
1. [[Asset Return Parameterization]]
2. [[Initial Block Difficulty]]
3. [[Minimum Qi Conversion Amount]]
4. [[Minimum Quai Conversion Amount]]
5. [[PID Parameterization]]

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
8. [[Global]].[[Global State-Qi Price|Qi Price]]
9. [[Global]].[[Global State-Qi Supply|Qi Supply]]
10. [[Global]].[[Global State-Quai Price|Quai Price]]
11. [[Global]].[[Global State-Quai Supply|Quai Supply]]

