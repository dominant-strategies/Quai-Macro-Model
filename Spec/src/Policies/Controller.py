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

controller_update_policy_option3 = {
    "name": "Reward Ratio Gain",
    "description": r"""### Gain

#### Gain as a control variable

A hypothesis from Aug 21st is that a _gain_ is required that is dependent upon the average block difficulty $D$, and an initial supposition was to set $u_2 = g(D)$ for some function $g$. 

The role of the gain is to set the scale of the proposed block rewards $r_1$ and $r_2$, adjusting that scale in response to changes in $D$. This is a 'black box' approach that does not change the approach above (since only the ration $u_1/u_2$ matters). However, it does not have a theoretical basis for its introduction, rather acting as an _ad hoc_ adjustment parameter.

It is likely that for controller stability at least $g'(D) < 0$ (and perhaps $g''(D) > 0$) everywhere, but this is not confirmed.

#### Gain as a reward ratio

An alternative that may provide more insight into scaling is to treat the unspecified parameter $R$ as a function of $D$, allowing that to change in an consistent fashion relative to the protocol. This has the advantage of 'closing the loop' on $R$ and providing a response to average difficulty $D$. Since $R$ is meant to be an expression of a ratio of proposed block rewards, one may adopt the definition of $R(D)$ as the ratio of proposed block rewards that _would have obtained_ if $D$ had been the block difficulty under the previous controller parameters, i.e.:
$$
  R(D) := \frac{u_{k1}}{u_{k2}}x(D),
$$
where $\mathbf u_k := (u_{k1}, u_{k2})$ is the vector of controller parameters from previous prime block $k$, and
$$
  x(D) := \frac{D}{\log_2(D)},
$$
i.e. that ratio of difficulties that would have obtained from difficulty level $D$.

Given this, the optimal controller parameter update for $u^\star_1$ from the loss function is (from above):
$$
  u_1^\star = \frac{u_2^\star}{u_{k2}}u_{k1}\frac{x(D)}{x^\star(\hat{\pmb{\beta}})}.
$$

If (as before) token 2 acts as a numeraire, then $u^\star_2 = u_{k2}$. Letting $u_1^\star = u_{k1} + \Delta u_1$, this can be rearranged to yield the update "delta" for the controller paramter $u_1$:
$$
  \Delta u_1 = \left ( \frac{x(D)}{x^\star(\hat{\pmb{\beta}})} - 1 \right )u_{k1}. \qquad \qquad (*)
$$

This has an appealing interpretation for the controller: when the function of average difficulty $x(D)$ falls below the estimated value $x^\star(\hat{\pmb{\beta}})$, the controller parameter $u_1$ is adjusted proportionally downwards, so that the proposed block rewards, at the indifference difficulty level $d^\star$, reflect the block ratio $R(D)$ for the average difficulty. **The controller is thus acting to _stabilize_ the block reward ratio around the average difficulty of the system**. Similarly, when $x(D) > x^\star(\hat{\pmb{\beta}})$ the controller parameter $u_1$ is adjusted upwards.

In this setup the control parameter $u_2$ retains its use as a numeraire, i.e. it is set to a constant $\bar u$ derived to satisfy initial condition requirements and remains unchanged thereafter.

:::info
A manual "attenuation" parameter could also be added here, to adjust the sensitivity of $\Delta u_1$ to $x(D)/x^\star(\hat{\pmb{\beta}})$. In that case $(*)$ above is slightly modified to
$$
  \Delta u_1 = \alpha \left ( \frac{x(D)}{x^\star(\hat{\pmb{\beta}})} - 1 \right )u_{k1}. \qquad \qquad (**)
$$
for an exogenous parameter $\alpha \in (0,1]$. It is not expected that this manual attenuation is required, but may be used if a slower convergence to the indifference point is desired.
:::



### State update

What is the response of the miner to the new controller state? Let the next (non-prime) block $i$ have difficulty $d_i$. If $d_i < d^\star$ then $x_i < x^\star$ and so $p_i$, the probability a miner accepts token 1, must be less than 1/2. We see that _the valuation of token 1 has decreased in expectation when difficulty has decreased, as it is the miner decision that conveys difficulty value_.

Similarly, if $d_i > d^\star$ then $x_i > x^\star$, and so $p_i > 1/2$, i.e. _the valuation of token 1 has increased in expectation when difficulty has increased_.

The interpretation links the valuation of difficulty to the value of the _qi_ token--in this case the _quai_ token acts as a _numeraire_.
""",
    "logic": """def reward_ratio_gain(state, params, spaces):
    # To be set to a parameter soon
    k_quai = state["K Quai"]
    alpha = 0.000001
    D = spaces[0]["Block Difficulty"]
    D = sum(D) / len(D)
    d1 = D
    d2 = log(D, params["Quai Reward Base Parameter"])
    x_d = d1 / d2
    x_b_star = -spaces[1]["Beta"][0] / spaces[1]["Beta"][1]
    k_quai += alpha * (x_d / x_b_star - 1) * k_quai
    spaces = [{"K Quai": k_quai, "K Qi": state["K Qi"]}, spaces[1]]
    return spaces""",
}

controller_update_policy = {
    "name": "Controller Update Policy",
    "description": "The policy which determines the update to the K Values.",
    "constraints": [],
    "policy_options": [
        controller_update_policy_option1,
        controller_update_policy_option2,
        controller_update_policy_option3,
    ],
    "domain": ["Mined Blocks Space 2", "Beta Vector Space"],
    "codomain": ["K Space", "Beta Vector Space"],
    "parameters_used": ["PID Parameterization", "Initial Block Difficulty"],
    "metrics_used": ["Qi to Hash Metric", "Quai to Hash Metric"],
}


beta_estimation_policy_option1 = {
    "name": "SGD Logistic Classifier Training",
    "description": "Simple SGD training with partial fit.",
    "logic": """X = [[1, x / log(x, params["Quai Reward Base Parameter"])] for x in spaces[0]["Block Difficulty"]]
Y = [x > 0 for x in spaces[0]["Quai Taken"]]

state["Logistic Classifier"].partial_fit(X, Y, classes=[0, 1])
betas = state["Logistic Classifier"].coef_[0]""",
}


beta_estimation_policy = {
    "name": "Beta Estimation Policy",
    "description": "The policy which determines the update to beta vector estimates.",
    "constraints": [],
    "policy_options": [beta_estimation_policy_option1],
    "domain": [
        "Mined Blocks Space 2",
    ],
    "codomain": ["Mined Blocks Space 2", "Beta Vector Space"],
    "parameters_used": [],
    "metrics_used": [],
}


controller_policies = [controller_update_policy, beta_estimation_policy]
