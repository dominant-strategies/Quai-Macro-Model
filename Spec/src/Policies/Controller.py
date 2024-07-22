controller_update_policy_option1 = {
    "name": "Linear Controller Policy",
    "description": "A controller that works in a linear fashion based upon the mined ratio.",
    "logic": r"""Inputs are:
- $\bar{M}$,Average for [[Global State-Historical Mined Ratio]].
- $\Sigma M$,Sum of [[Global State-Historical Mined Ratio]].
- PID values set with constants of P = 0.00000005, I = P\*0.0001, D = 0 (but commented out .05 value)
-  $\bar{M_{20-0}}$,Average of last 20 elements of the [[Global State-Historical Mined Ratio]].
- $\bar{M_{40-20}}$, The average of the last 40 to last 20 elements of [[Global State-Historical Mined Ratio]]

Calculations are:
- $\Delta_e$,the delta error = $\bar{M_{20-0}}$ - $\bar{M_{40-20}}$

Updates are:

$$\Delta k_{Quai} = -k_{Quai} \cdot (P*[.5-\bar{M}] + I\cdot \Sigma M + D \cdot \Delta_e)$$""",
}

controller_update_policy_option2 = {
    "name": "Hash Controller Policy",
    "description": "A controller that works based off of hash.",
    "logic": r"""Inputs are:
- $\bar{M}$,Average for [[Global State-Historical Mined Ratio]].
- $\Sigma H_{Quai}$, the sum of [[Global State-Historical Quai Hash]]
- $\Sigma H_{Qi}$, the sum of [[Global State-Historical Qi Hash]]
- B, the [[Global State-Current Block Difficulty|Current Block Difficulty]]
- $B_I$, the [[Initial Block Difficulty Parameter]]
- PID values set with constants of P = 0.0001, I = P\*0.001, D = P\*.02 (but commented out .05 value)
- $R_{Qi}$, the [[Current Qi Block Reward Stateful Metric]]
- $R_{Quai}$, the [[Current Quai Block Reward Stateful Metric]]

Functions are:
- $quaiToHash(x) -> \frac{R_{Qi}}{R_{Quai}} \cdot x \cdot k_{qi}$
- $qiToHash(x) ->  x \cdot k_{qi}$
- $proportionalGain(x)-> 1 + 4 x^2$

Calculations are:
- r, Ratio = $\bar{M}*2-1$ 
- h, Hash Ratio = $\frac{\text{quaiToHash}(\Sigma H_{Quai}) - \text{qiToHash}(\Sigma H_{Qi})}{\text{quaiToHash}(\Sigma H_{Quai}) + \text{qiToHash}(\Sigma H_{Qi})}$

Updates are:
$$\Delta k_{Quai} = k_{Quai} \cdot (\frac{log_2(B)}{log_2(B_I)} \cdot P \cdot proportionalGain(h)\cdot h)$$
""",
}

controller_update_policy = {
    "name": "Controller Update Policy",
    "description": "The policy which determines the update to the K Values.",
    "constraints": [],
    "policy_options": [
        controller_update_policy_option1,
        controller_update_policy_option2,
    ],
    "domain": [
        "Observable State Space",
    ],
    "codomain": ["K Space"],
    "parameters_used": ["PID Parameterization", "Initial Block Difficulty"],
    "metrics_used": ["Qi to Hash Metric", "Quai to Hash Metric"],
}

controller_policies = [controller_update_policy]