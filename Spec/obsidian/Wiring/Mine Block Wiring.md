## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Aggregate Hashpower"])
EES0 --- EE0
EES1(["Block Difficulty"])
EES1 --- EE0
EES2(["Block Number"])
EES2 --- EE0
EES3(["Estimated Mining Beta Vector"])
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
EES9(["Mining Log"])
EES9 --- EE0
EES10(["Qi Supply"])
EES10 --- EE0
EES11(["Qi Unlock Schedule"])
EES11 --- EE0
EES12(["Quai Supply"])
EES12 --- EE0
EES13(["Quai Unlock Schedule"])
EES13 --- EE0
EES14(["Time"])
EES14 --- EE0
end

subgraph X33["Mine Block Wiring"]
direction TB
X1["Mine Block Boundary Action"]
X2["Mining Policy"]
X3["Block Reward Policy"]
X4["Mining Payment Policy"]
subgraph X16["Mezzanine Mining Wiring"]
direction TB
subgraph X12["Controller Update Wiring"]
direction TB
X5["Beta Estimation Policy"]
X6["Controller Update Policy"]
subgraph X11["Controller Mechanisms"]
direction TB
X7["Set K Mechanism"]
X7 --> EES7
X7 --> EES6
X8["Set Estimated Beta Vector Mechanism"]
X8 --> EES3
X9[Domain]

direction LR
direction TB
X9 --"K Space"--> X7
X9 --"Beta Vector Space"--> X8
end
X5--"Mined Blocks Space 2
Beta Vector Space"---->X6
X6--"K Space
Beta Vector Space"---->X11
end
X13["Mezzanine Wiring Passthrough"]
X14[Domain]
X15[Codomain]
direction LR
direction TB
X14 --"Mined Blocks Space 2"--> X12
X14 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2
Block Difficulty Space"------------> X13
X13 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2
Block Difficulty Space"--> X15
end
subgraph X32["Mining Mechanisms"]
direction TB
X17["Increment Block Number Mechanism"]
X17 --> EES2
X18["Mint Qi Tokens Mechanism"]
X18 --> EES10
X19["Mint Quai Tokens Mechanism"]
X19 --> EES12
X20["Update Historical Mined Ratio Mechanism"]
X20 --> EES4
X21["Update Historical Qi Hash Mechanism"]
X21 --> EES5
X22["Update Historical Quai Hash Mechanism"]
X22 --> EES5
X23["Update Locked Qi Mechanism"]
X23 --> EES8
X24["Update Locked Quai Mechanism"]
X24 --> EES8
X25["Append to Unlock Schedule Mechanism"]
X25 --> EES13
X25 --> EES11
X26["Increment Time Mechanism"]
X26 --> EES14
X27["Log Mined Blocks Mechanism"]
X27 --> EES9
X28["Update Hash Rate Mechanism"]
X28 --> EES0
X29["Update Block Difficulty Mechanism"]
X29 --> EES1
X30[Domain]

direction LR
direction TB
X30 --> X17
X30 --"Qi Space"--> X18
X30 --"Quai Space"--> X19
X30 --"Mined Ratio Space"--> X20
X30 --"Qi Hash Space"--> X21
X30 --"Quai Hash Space"--> X22
X30 --"Qi Space"--> X23
X30 --"Quai Space"--> X24
X30 --"Unlock Schedule Entry Space"--> X25
X30 --"Mined Blocks Space 2"--> X26
X30 --"Mined Blocks Space 2"--> X27
X30 --> X28
X30 --"Block Difficulty Space"--> X29
end
X1--"Pre-Mining Space"--->X2
X2--"Mined Blocks Space"--->X3
X3--"Block Reward Options Space"--->X4
X4--"Mined Blocks Space 2
Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2
Block Difficulty Space"-------------->X16
X16--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2
Block Difficulty Space"------------->X32
end
```

## Description

Block Type: Stack Block
"The wiring for mining a block.

For the decision between Qi and Quai, the idea is that there should be a Schelling point, if the miner is mining and Qi is an option, they will only look at Qi as making sense if the market price is above their production price.

If the demand for Qi is greater than the supply, there should be a profitable opportunity until market price approaches at which point amount of Qi is at equilibrium because the market price matches the production price.
## Components
1. [[Mine Block Boundary Action]]
2. [[Mining Policy]]
3. [[Block Reward Policy]]
4. [[Mining Payment Policy]]
5. [[Mezzanine Mining Wiring]]
6. [[Mining Mechanisms]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Beta Estimation Policy]]
3. [[Block Reward Policy]]
4. [[Controller Update Policy]]
5. [[Increment Block Number Mechanism]]
6. [[Increment Time Mechanism]]
7. [[Log Mined Blocks Mechanism]]
8. [[Mezzanine Wiring Passthrough]]
9. [[Mine Block Boundary Action]]
10. [[Mining Payment Policy]]
11. [[Mining Policy]]
12. [[Mint Qi Tokens Mechanism]]
13. [[Mint Quai Tokens Mechanism]]
14. [[Set Estimated Beta Vector Mechanism]]
15. [[Set K Mechanism]]
16. [[Update Block Difficulty Mechanism]]
17. [[Update Hash Rate Mechanism]]
18. [[Update Historical Mined Ratio Mechanism]]
19. [[Update Historical Qi Hash Mechanism]]
20. [[Update Historical Quai Hash Mechanism]]
21. [[Update Locked Qi Mechanism]]
22. [[Update Locked Quai Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Beta Vector Space]]
2. [[Block Difficulty Space]]
3. [[Block Reward Options Space]]
4. [[Empty Space]]
5. [[K Space]]
6. [[Mined Blocks Space]]
7. [[Mined Blocks Space 2]]
8. [[Mined Ratio Space]]
9. [[Pre-Mining Space]]
10. [[Qi Hash Space]]
11. [[Qi Space]]
12. [[Quai Hash Space]]
13. [[Quai Space]]
14. [[Terminating Space]]
15. [[Unlock Schedule Entry Space]]

## Parameters Used
1. [[Aggregate Hashpower Series]]
2. [[Controller Alpha Parameter]]
3. [[Difficulty Adjustment Period]]
4. [[Difficulty Randomness Mu]]
5. [[Difficulty Randomness Sigma]]
6. [[Initial Block Difficulty]]
7. [[Minimum K Qi]]
8. [[Minimum K Quai]]
9. [[PID Parameterization]]
10. [[Probability of Rational Miners]]
11. [[Quai Reward Base Parameter]]
12. [[State Update Skipping Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Aggregate Hashpower|Aggregate Hashpower]]
2. [[Global]].[[Global State-Block Difficulty|Block Difficulty]]
3. [[Global]].[[Global State-Block Number|Block Number]]
4. [[Global]].[[Global State-Estimated Mining Beta Vector|Estimated Mining Beta Vector]]
5. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
6. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
7. [[Global]].[[Global State-K Qi|K Qi]]
8. [[Global]].[[Global State-K Quai|K Quai]]
9. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
10. [[Global]].[[Global State-Mining Log|Mining Log]]
11. [[Global]].[[Global State-Qi Supply|Qi Supply]]
12. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
13. [[Global]].[[Global State-Quai Supply|Quai Supply]]
14. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
15. [[Global]].[[Global State-Time|Time]]

