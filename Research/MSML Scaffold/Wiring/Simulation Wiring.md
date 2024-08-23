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
EES7(["Locked Qi Supply"])
EES7 --- EE0
EES8(["Qi Price"])
EES8 --- EE0
EES9(["Qi Supply"])
EES9 --- EE0
EES10(["Qi Unlock Schedule"])
EES10 --- EE0
EES11(["Quai Price"])
EES11 --- EE0
EES12(["Quai Supply"])
EES12 --- EE0
EES13(["Quai Unlock Schedule"])
EES13 --- EE0
EES14(["Simulation History Log"])
EES14 --- EE0
end

subgraph X39["Simulation Wiring"]
direction TB
subgraph X4["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X3["Update Prices Mechanism"]
X3 --> EES11
X3 --> EES8
X1--"Price Movement Space"--->X2
X2--"Price Space"--->X3
end
subgraph X19["Conversions Wiring"]
direction TB
X5["Conversions Boundary Action"]
X6["Conversions Policy"]
subgraph X18["Conversions Mechanisms Wiring"]
direction TB
X7["Mint Qi Tokens Mechanism"]
X7 --> EES9
X8["Mint Quai Tokens Mechanism"]
X8 --> EES12
X9["Burn Qi Tokens Mechanism"]
X9 --> EES9
X10["Burn Quai Tokens Mechanism"]
X10 --> EES12
X11["Update Historical Converted Qi Mechanism"]
X11 --> EES1
X12["Update Historical Converted Quai Mechanism"]
X12 --> EES2
X13["Update Locked Qi Mechanism"]
X13 --> EES7
X14["Update Locked Quai Mechanism"]
X14 --> EES7
X15["Append to Unlock Schedule Mechanism"]
X15 --> EES13
X15 --> EES10
X16[Domain]

direction LR
direction TB
X16 --"Qi Space"--> X7
X16 --"Quai Space"--> X8
X16 --"Qi Space"--> X9
X16 --"Quai Space"--> X10
X16 --"Conversion Log Space"--> X11
X16 --"Conversion Log Space"--> X12
X16 --"Qi Space"--> X13
X16 --"Quai Space"--> X14
X16 --"Unlock Schedule Entry Space"--> X15
end
X5--"Conversion Space"--->X6
X6--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space
Qi Space
Quai Space
Unlock Schedule Entry Space"----------->X18
end
subgraph X33["Mine Block Wiring"]
direction TB
X20["Mine Block Boundary Action"]
X21["Mining Policy"]
X22["Block Reward Policy"]
X23["Mining Payment Policy"]
subgraph X32["Mining Mechanisms"]
direction TB
X24["Increment Block Number Mechanism"]
X24 --> EES0
X25["Mint Qi Tokens Mechanism"]
X25 --> EES9
X26["Mint Quai Tokens Mechanism"]
X26 --> EES12
X27["Update Historical Mined Ratio Mechanism"]
X27 --> EES3
X28["Update Historical Qi Hash Mechanism"]
X28 --> EES4
X29["Update Historical Quai Hash Mechanism"]
X29 --> EES4
X30[Domain]

direction LR
direction TB
X30 --> X24
X30 --"Qi Space"--> X25
X30 --"Quai Space"--> X26
X30 --"Mined Ratio Space"--> X27
X30 --"Qi Hash Space"--> X28
X30 --"Quai Hash Space"--> X29
end
X20--"Pre-Mining Space"--->X21
X21--"Mined Blocks Space"--->X22
X22--"Block Reward Options Space"--->X23
X23--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X32
end
subgraph X37["Controller Update Wiring"]
direction TB
X34["Controller Update Control Action"]
X35["Controller Update Policy"]
X36["Set K Mechanism"]
X36 --> EES6
X36 --> EES5
X34--"Observable State Space"--->X35
X35--"K Space"--->X36
end
X38["Log Simulation Data Mechanism"]
X38 --> EES14
X4--->X19
X19--->X33
X33--->X37
X37--->X38
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
5. [[Log Simulation Data Mechanism]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Block Reward Policy]]
3. [[Burn Qi Tokens Mechanism]]
4. [[Burn Quai Tokens Mechanism]]
5. [[Controller Update Control Action]]
6. [[Controller Update Policy]]
7. [[Conversions Boundary Action]]
8. [[Conversions Policy]]
9. [[Increment Block Number Mechanism]]
10. [[Log Simulation Data Mechanism]]
11. [[Mine Block Boundary Action]]
12. [[Mining Payment Policy]]
13. [[Mining Policy]]
14. [[Mint Qi Tokens Mechanism]]
15. [[Mint Quai Tokens Mechanism]]
16. [[Price Movements Boundary Action]]
17. [[Price Movements Policy]]
18. [[Set K Mechanism]]
19. [[Update Historical Converted Qi Mechanism]]
20. [[Update Historical Converted Quai Mechanism]]
21. [[Update Historical Mined Ratio Mechanism]]
22. [[Update Historical Qi Hash Mechanism]]
23. [[Update Historical Quai Hash Mechanism]]
24. [[Update Locked Qi Mechanism]]
25. [[Update Locked Quai Mechanism]]
26. [[Update Prices Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Block Reward Options Space]]
2. [[Conversion Log Space]]
3. [[Conversion Space]]
4. [[Empty Space]]
5. [[K Space]]
6. [[Mined Blocks Space]]
7. [[Mined Ratio Space]]
8. [[Observable State Space]]
9. [[Pre-Mining Space]]
10. [[Price Movement Space]]
11. [[Price Space]]
12. [[Qi Hash Space]]
13. [[Qi Space]]
14. [[Quai Hash Space]]
15. [[Quai Space]]
16. [[Terminating Space]]
17. [[Unlock Schedule Entry Space]]

## Parameters Used
1. [[Aggregate Hashpower Series]]
2. [[Asset Return Parameterization]]
3. [[Conversion Percentage Mu]]
4. [[Conversion Percentage Sigma]]
5. [[Hashpower Cost Series]]
6. [[Initial Block Difficulty]]
7. [[Lockup Options]]
8. [[Minimum Qi Conversion Amount]]
9. [[Minimum Quai Conversion Amount]]
10. [[PID Parameterization]]
11. [[Price EWMA Lambda]]
12. [[Qi Price Movemement Sigma]]
13. [[Quai Price Movemement Sigma]]
14. [[Quai Reward Base Parameter]]
15. [[Speculator Percentage]]

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
8. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
9. [[Global]].[[Global State-Qi Price|Qi Price]]
10. [[Global]].[[Global State-Qi Supply|Qi Supply]]
11. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
12. [[Global]].[[Global State-Quai Price|Quai Price]]
13. [[Global]].[[Global State-Quai Supply|Quai Supply]]
14. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
15. [[Global]].[[Global State-Simulation History Log|Simulation History Log]]

