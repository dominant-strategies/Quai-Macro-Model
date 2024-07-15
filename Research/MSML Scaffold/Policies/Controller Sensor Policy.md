TBD - Policy for things like moving averages and prep of inputs

Old versions are below with inputs, calculations and update rule. Only the inputs are relevant for the policy but the calculations and updates are displayed to make the intuition more obvious.

## Linear Controller

Inputs are:
- $\bar{M}$,Average for [[MSML Scaffold/State/Global State-Historical Mined Ratio]].
- $\Sigma M$,Sum of [[MSML Scaffold/State/Global State-Historical Mined Ratio]].
- PID values set with constants of P = 0.00000005, I = P\*0.0001, D = 0 (but commented out .05 value)
-  $\bar{M_{20-0}}$,Average of last 20 elements of the [[MSML Scaffold/State/Global State-Historical Mined Ratio]].
- $\bar{M_{40-20}}$, The average of the last 40 to last 20 elements of [[MSML Scaffold/State/Global State-Historical Mined Ratio]]

Calculations (for reference only) are:
- $\Delta_e$,the delta error = $\bar{M_{20-0}}$ - $\bar{M_{40-20}}$

Updates are (for reference only):

$$\Delta k_{Quai} = -k_{Quai} \cdot (P*[.5-\bar{M}] + I\cdot \Sigma M + D \cdot \Delta_e)$$

## Hash Controller

Inputs are:
- $\bar{M}$,Average for [[MSML Scaffold/State/Global State-Historical Mined Ratio]].
- $\Sigma H_{Quai}$, the sum of [[MSML Scaffold/State/Global State-Historical Quai Hash]]
- $\Sigma H_{Qi}$, the sum of [[MSML Scaffold/State/Global State-Historical Qi Hash]]
- B, the [[Global State-Current Block Difficulty|Current Block Difficulty]]
- $B_I$, the [[Initial Block Difficulty Parameter]]
- PID values set with constants of P = 0.0001, I = P\*0.001, D = P\*.02 (but commented out .05 value)
- $R_{Qi}$, the [[Current Qi Block Reward Stateful Metric]]
- $R_{Quai}$, the [[Current Quai Block Reward Stateful Metric]]

Functions are (for reference only):
- $quaiToHash(x) -> \frac{R_{Qi}}{R_{Quai}} \cdot x \cdot k_{qi}$
- $qiToHash(x) ->  x \cdot k_{qi}$
- $proportionalGain(x)-> 1 + 4 x^2$

Calculations are (for reference only):
- r, Ratio = $\bar{M}*2-1$ 
- h, Hash Ratio = $\frac{\text{quaiToHash}(\Sigma H_{Quai}) - \text{qiToHash}(\Sigma H_{Qi})}{\text{quaiToHash}(\Sigma H_{Quai}) + \text{qiToHash}(\Sigma H_{Qi})}$

Updates are (for reference only):
$$\Delta k_{Quai} = k_{Quai} \cdot (\frac{log_2(B)}{log_2(B_I)} \cdot P \cdot proportionalGain(h)\cdot h)$$
