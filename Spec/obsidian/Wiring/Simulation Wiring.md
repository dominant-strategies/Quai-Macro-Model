## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Block Number"])
EES0 --- EE0
EES1(["Estimated Mining Beta Vector"])
EES1 --- EE0
EES2(["Historical Converted Qi"])
EES2 --- EE0
EES3(["Historical Converted Quai"])
EES3 --- EE0
EES4(["Historical Mined Ratio"])
EES4 --- EE0
EES5(["Historical Qi Hash"])
EES5 --- EE0
EES6(["K Qi"])
EES6 --- EE0
EES7(["K Quai"])
EES7 --- EE0
EES8(["Locked Qi Supply"])
EES8 --- EE0
EES9(["Locked Quai Supply"])
EES9 --- EE0
EES10(["Qi Price"])
EES10 --- EE0
EES11(["Qi Supply"])
EES11 --- EE0
EES12(["Qi Unlock Schedule"])
EES12 --- EE0
EES13(["Quai Price"])
EES13 --- EE0
EES14(["Quai Supply"])
EES14 --- EE0
EES15(["Quai Unlock Schedule"])
EES15 --- EE0
EES16(["Simulation History Log"])
EES16 --- EE0
end

subgraph X51["Simulation Wiring"]
direction TB
subgraph X4["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X3["Update Prices Mechanism"]
X3 --> EES13
X3 --> EES10
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
X7 --> EES11
X8["Mint Quai Tokens Mechanism"]
X8 --> EES14
X9["Burn Qi Tokens Mechanism"]
X9 --> EES11
X10["Burn Quai Tokens Mechanism"]
X10 --> EES14
X11["Update Historical Converted Qi Mechanism"]
X11 --> EES2
X12["Update Historical Converted Quai Mechanism"]
X12 --> EES3
X13["Update Locked Qi Mechanism"]
X13 --> EES8
X14["Update Locked Quai Mechanism"]
X14 --> EES8
X15["Append to Unlock Schedule Mechanism"]
X15 --> EES15
X15 --> EES12
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
subgraph X45["Mine Block Wiring"]
direction TB
X20["Mine Block Boundary Action"]
X21["Mining Policy"]
X22["Block Reward Policy"]
X23["Mining Payment Policy"]
subgraph X35["Mezzanine Mining Wiring"]
direction TB
subgraph X31["Controller Update Wiring"]
direction TB
X24["Beta Estimation Policy"]
X25["Controller Update Policy"]
subgraph X30["Controller Mechanisms"]
direction TB
X26["Set K Mechanism"]
X26 --> EES7
X26 --> EES6
X27["Set Estimated Beta Vector Mechanism"]
X27 --> EES1
X28[Domain]

direction LR
direction TB
X28 --"K Space"--> X26
X28 --"Beta Vector Space"--> X27
end
X24--"Mined Blocks Space 2
Beta Vector Space"---->X25
X25--"K Space
Beta Vector Space"---->X30
end
X32["Mezzanine Wiring Passthrough"]
X33[Domain]
X34[Codomain]
direction LR
direction TB
X33 --"Mined Blocks Space 2"--> X31
X33 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------> X32
X32 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"--> X34
end
subgraph X44["Mining Mechanisms"]
direction TB
X36["Increment Block Number Mechanism"]
X36 --> EES0
X37["Mint Qi Tokens Mechanism"]
X37 --> EES11
X38["Mint Quai Tokens Mechanism"]
X38 --> EES14
X39["Update Historical Mined Ratio Mechanism"]
X39 --> EES4
X40["Update Historical Qi Hash Mechanism"]
X40 --> EES5
X41["Update Historical Quai Hash Mechanism"]
X41 --> EES5
X42[Domain]

direction LR
direction TB
X42 --> X36
X42 --"Qi Space"--> X37
X42 --"Quai Space"--> X38
X42 --"Mined Ratio Space"--> X39
X42 --"Qi Hash Space"--> X40
X42 --"Quai Hash Space"--> X41
end
X20--"Pre-Mining Space"--->X21
X21--"Mined Blocks Space"--->X22
X22--"Block Reward Options Space"--->X23
X23--"Mined Blocks Space 2
Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"-------->X35
X35--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X44
end
subgraph X49["Unlock Tokens Wiring"]
direction TB
X46["Unlock Tokens Control Action"]
X47["Unlock Tokens Policy"]
X48["Unlock Tokens Mechanism"]
X48 --> EES9
X48 --> EES8
X48 --> EES15
X48 --> EES12
X46--->X47
X47--"Unlock Tokens Space"--->X48
end
X50["Log Simulation Data Mechanism"]
X50 --> EES16
X4--->X19
X19--->X45
X45--->X49
X49--->X50
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Conversions Wiring]]
3. [[Mine Block Wiring]]
4. [[Unlock Tokens Wiring]]
5. [[Log Simulation Data Mechanism]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Beta Estimation Policy]]
3. [[Block Reward Policy]]
4. [[Burn Qi Tokens Mechanism]]
5. [[Burn Quai Tokens Mechanism]]
6. [[Controller Update Policy]]
7. [[Conversions Boundary Action]]
8. [[Conversions Policy]]
9. [[Increment Block Number Mechanism]]
10. [[Log Simulation Data Mechanism]]
11. [[Mezzanine Wiring Passthrough]]
12. [[Mine Block Boundary Action]]
13. [[Mining Payment Policy]]
14. [[Mining Policy]]
15. [[Mint Qi Tokens Mechanism]]
16. [[Mint Quai Tokens Mechanism]]
17. [[Price Movements Boundary Action]]
18. [[Price Movements Policy]]
19. [[Set Estimated Beta Vector Mechanism]]
20. [[Set K Mechanism]]
21. [[Unlock Tokens Control Action]]
22. [[Unlock Tokens Mechanism]]
23. [[Unlock Tokens Policy]]
24. [[Update Historical Converted Qi Mechanism]]
25. [[Update Historical Converted Quai Mechanism]]
26. [[Update Historical Mined Ratio Mechanism]]
27. [[Update Historical Qi Hash Mechanism]]
28. [[Update Historical Quai Hash Mechanism]]
29. [[Update Locked Qi Mechanism]]
30. [[Update Locked Quai Mechanism]]
31. [[Update Prices Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Beta Vector Space]]
2. [[Block Reward Options Space]]
3. [[Conversion Log Space]]
4. [[Conversion Space]]
5. [[Empty Space]]
6. [[K Space]]
7. [[Mined Blocks Space]]
8. [[Mined Blocks Space 2]]
9. [[Mined Ratio Space]]
10. [[Pre-Mining Space]]
11. [[Price Movement Space]]
12. [[Price Space]]
13. [[Qi Hash Space]]
14. [[Qi Space]]
15. [[Quai Hash Space]]
16. [[Quai Space]]
17. [[Terminating Space]]
18. [[Unlock Schedule Entry Space]]
19. [[Unlock Tokens Space]]

## Parameters Used
1. [[Aggregate Hashpower Series]]
2. [[Asset Return Parameterization]]
3. [[Controller Alpha Parameter]]
4. [[Conversion Percentage Mu]]
5. [[Conversion Percentage Sigma]]
6. [[Difficulty Randomness Mu]]
7. [[Difficulty Randomness Sigma]]
8. [[Hashpower Cost Series]]
9. [[Initial Block Difficulty]]
10. [[Lockup Options]]
11. [[Minimum Qi Conversion Amount]]
12. [[Minimum Quai Conversion Amount]]
13. [[PID Parameterization]]
14. [[Price EWMA Lambda]]
15. [[Qi Price Movemement Sigma]]
16. [[Quai Price Movemement Sigma]]
17. [[Quai Reward Base Parameter]]
18. [[Speculator Percentage]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Estimated Mining Beta Vector|Estimated Mining Beta Vector]]
3. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
4. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
5. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
6. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
7. [[Global]].[[Global State-K Qi|K Qi]]
8. [[Global]].[[Global State-K Quai|K Quai]]
9. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
10. [[Global]].[[Global State-Locked Quai Supply|Locked Quai Supply]]
11. [[Global]].[[Global State-Qi Price|Qi Price]]
12. [[Global]].[[Global State-Qi Supply|Qi Supply]]
13. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
14. [[Global]].[[Global State-Quai Price|Quai Price]]
15. [[Global]].[[Global State-Quai Supply|Quai Supply]]
16. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
17. [[Global]].[[Global State-Simulation History Log|Simulation History Log]]

