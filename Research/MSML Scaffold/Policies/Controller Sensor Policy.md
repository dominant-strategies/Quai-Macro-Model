TBD - Policy for things like moving averages and prep of inputs

Old versions use the following

## Linear Controller
Inputs are:
- $\bar{M}$,Average for [[Global State - Historical Mined Ratio]].
- $\Sigma M$,Sum of [[Global State - Historical Mined Ratio]].
- PID values set with constants of P = 0.00000005, I = P\*0.0001, D = 0
-  $\bar{M_{20-0}}$,Average of last 20 elements of the [[Global State - Historical Mined Ratio]].
- $\bar{M_{40-20}}$, The average of the last 40 to last 20 elements of [[Global State - Historical Mined Ratio]]

Calculations are:
- $\Delta_e$,the delta error = $\bar{M_{20-0}}$ - $\bar{M_{40-20}}$

Updates are:

$$\Delta k_{Quai} = -k_{Quai} \cdot (P*[.5-\bar{M}] + I\cdot \Sigma M + D \cdot \Delta_e)$$