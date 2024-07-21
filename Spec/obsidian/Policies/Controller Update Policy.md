## Description

The policy which determines the update to the K Values.
## Called By
1. [[Controller Update Control Action]]
## Domain Spaces
1. [[Observable State Space]]
## Followed By
1. [[Set K Mechanism]]
## Codomain Spaces
1. [[K Space]]
## Constraints
## Parameters Used
1. [[PID Parameterization]]
## Metrics Used
## Policy Options
### 1. Linear Controller Policy
#### Description
A controller that works in a linear fashion based upon the mined ratio.
#### Logic
Inputs are:
- $\bar{M}$,Average for [[Global State-Historical Mined Ratio]].
- $\Sigma M$,Sum of [[Global State-Historical Mined Ratio]].
- PID values set with constants of P = 0.00000005, I = P\*0.0001, D = 0 (but commented out .05 value)
-  $\bar{M_{20-0}}$,Average of last 20 elements of the [[Global State-Historical Mined Ratio]].
- $\bar{M_{40-20}}$, The average of the last 40 to last 20 elements of [[Global State-Historical Mined Ratio]]

Calculations (for reference only) are:
- $\Delta_e$,the delta error = $\bar{M_{20-0}}$ - $\bar{M_{40-20}}$

Updates are (for reference only):

$$\Delta k_{Quai} = -k_{Quai} \cdot (P*[.5-\bar{M}] + I\cdot \Sigma M + D \cdot \Delta_e)$$

