## Description

Policy which determines what amount of Quai vs. Qi is taken as payment.
## Called By
1. [[Block Reward Policy]]
## Domain Spaces
1. [[Block Reward Options Space]]
## Followed By
1. [[Beta Estimation Policy]]
2. [[Mezzanine Wiring Passthrough]]
3. [[Mezzanine Wiring Passthrough]]
4. [[Mezzanine Wiring Passthrough]]
5. [[Mezzanine Wiring Passthrough]]
6. [[Mezzanine Wiring Passthrough]]
7. [[Mezzanine Wiring Passthrough]]
8. [[Mezzanine Wiring Passthrough]]
9. [[Mezzanine Wiring Passthrough]]
## Codomain Spaces
1. [[Mined Blocks Space 2]]
2. [[Qi Space]]
3. [[Quai Space]]
4. [[Mined Ratio Space]]
5. [[Qi Hash Space]]
6. [[Quai Hash Space]]
7. [[Qi Space]]
8. [[Quai Space]]
9. [[Unlock Schedule Entry Space]]
10. [[Mined Blocks Space 2]]
11. [[Mined Blocks Space 2]]
12. [[Block Difficulty Space]]
## Constraints
## Parameters Used
1. [[Probability of Rational Miners]]
## Metrics Used
1. [[Qi to Hash Metric]]
2. [[Quai to Hash Metric]]
## Policy Options
### 1. Deterministic Mining Payment Policy
#### Description
User chooses either all Qi or all Quai based on which is more valuable based on USD prices.
#### Logic
Compare the price of Qi times Qi amount to price of Quai times Quai amount and pick the larger sum. Then the values for each iteration loop are as follows:
1. Qi Space is equal to 0 or the Qi amount
2. Quai Space is equal to 0 or the Quai amount
3. Mined Ratio Space has 0 if Qi was chosen, 1 if Quai was chosen
4. Qi Hash Space has 0 if Quai was chosen, otherwise $QiToHashMetric(Qi)$
5. Quai Hash Space has 0 if Qi was chosen, otherwise $QuaiToHashMetric(Quai)$
6. The first space passed out before those 5 will be a copy of the domain space filled in with the options chosen by each miner

### 2. Logistic Probability Payment Policy
#### Description
In what follows:
$$
  c_i = 
  \begin{cases}
    1 & \text{if token 1 is chosen} \\
    0 & \text{if token 2 is chosen}.
  \end{cases}
$$

Miner choices $c_i$ are assumed to be independently distributed such that for a block at height $i$,
$$
  p_i = \Pr(c_i = 1 | r_{i1}, r_{i2}, d_i ) := \frac{1}{1 + \exp(- \pmb{\beta}'\mathbf x_i) },
$$
where $\mathbf x_i$ is a set of features and $\pmb \beta$ their associated weights. It may be that the first such feature is $1$, so that the first weight is an intercept/'bias' term. Note that the linear term $\pmb{\beta}' \mathbf x$ is consistent with an interpretation of the above as coming from a latent variable/random utility model of the miner.

Given the data set $z_k$, maximum likelihood estimation yields estimates $\hat{\pmb{\beta}}$.


### Objective: stability via indifference

The controller seeks to stabilize an imputed value of hashpower (difficulty) by adjusting the proposed block rewards so that the miner would have been _indifferent_ between receiving an award in _qi_ (token 1) or _quai_ (token 2). The interpretation of this is that _deviations from indifference reveals that one token is more valuable than the other_. In the case that one token (_qi_) is to reflect the value of hashpower (difficulty), indifference is a _reference_ or _focal_ point from which the value of hashpower may be observed from miner decisions.

Indifference is when $p_i = 0.5$. Given $\hat{\pmb{\beta}}$, it is clear that the _invariant surface_ of features satisfies
$$
  \hat{\pmb{\beta}}' \mathbf x \equiv 0.
$$

Refining this further requires a definition of the features $\mathbf x$.

### A simple example

The simplest example is where $\mathbf x_i = (1, x_i) := (1, d_i/\log_2(d_i))$. In this case the invariant surface above yields a value $d_i = d^\star$ such that
$$
  \frac{d^\star}{\log_2(d^\star)} = -\frac{\hat{\beta_0}}{\hat{\beta_1}}.
$$

This is the difficulty level that would have to obtain in order for a miner to be (on average) indifferent between selecting token 1 and token 2. In this case define $x^\star(\hat{\pmb{\beta}}) = d^\star / \log_2(d^\star)$ (we will sometimes drop the dependence of $x^\star$ upon $\hat{\pmb{\beta}}$ for brevity in what follows, but it is important always to recall that $x^\star$ is derived from the _estimation problem_ the controller performs in finding a miner's indifference point).

[It is worth noting here that provided $d_i > e$, $\frac{dx_i}{d(d_i)} > 0$, i.e. increasing difficulty $d_i$ will increase $x_i$ and hence increase $p_i$ from the logistic expression above. There is thus a weak restriction on $d_i$ under this approach.]
#### Logic
Get probabilities of Qi as the population beta vector by (1, d_i/\log_2(d_i))

### 3. Logistic Probability Payment Policy V2
#### Description
V1 but with three dimensions, adding in the ratio of difficulties for Qi over Quai
#### Logic


### 4. Logistic Probability Payment Policy V3
#### Description
V1 but with three dimensions, adding in the log of the ratio of difficulties for Qi over Quai
#### Logic


