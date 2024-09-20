> [!info] Ported over from  https://hackmd.io/@blockscience/r1-WbLhiA

## Overall Summary

- The controller seeks to align:
    -  The value of energy (hashpower, difficulty) revealed by miner decisions regarding which token to receive as reward, with
    -  The proposed rewards associated with actual energy (hashpower, difficulty) use, as specified by the difficulty controller.
-  The controller performs this task by:
   1. *Learning* the relationship between difficulty and miner choice;
   2. *Deriving* an estimated value of difficulty from this relationship;
   3. *Aligning* this value to the protocol's actual difficulty (energy use) by adjusting proposed block rewards using the controller parameters $k_{qi}$ and $k_{quai}$.
- The controller assumes:
   1. A general model of miner behavior used in Economics and Econometrics;
   2. A representation of ecosystem difficulty from the difficulty controller as a proxy for energy use;
   3. An adjustment by the difficulty controller to induce miners to mine a block (by e.g. reducing hashpower). 

## The Miner Model

In what follows we specify a _model_ for miner behavior in which the decision of the miner at block height $i$ is a binary variable $C_i$ such that:
$$C_i = 
  \begin{cases}
    1 & \text{if token 1 is chosen} \\
    0 & \text{if token 2 is chosen}.
  \end{cases}$$

Miner choices $C_i$ are assumed to be, from the perspective of the controller, _stochastic_ as they are based upon private information held by the miner. [Econometric](https://en.wikipedia.org/wiki/Econometrics) analysis often encounters decision-making of this form, and there are underlying economic models of behavior (e.g. _latent variable_ or _random utility_ models--see Cameron, C. A. and P. K. Trivedi [2005], _[Microeconometrics: Methods and Applications](https://doi.org/10.1017/CBO9780511811241)_, Cambridge UP) that lead to a specific functional form for the distribution of $C_i$. Under this form, miner decisions are distributed such that for a block at height $i$,
$$p_i = \Pr(C_i = 1 | \mathbf u_k, D_i ) := \frac{1}{1 + \exp(- \pmb{\beta}'\mathbf x_i) },$$
where:
- $\mathbf u_k = (u_{k1},u_{k2})$ is vector of _controller update parameters_ from the last prime block, indexed by $k$,
- $D_i$ is the _difficulty_ of the block at block height $i$,
- $\mathbf x_i = (x_{i1}, \ldots, x_{iJ})$ is a vector of _features_ of length $J$, that may depend upon the block difficulty $D_i$ and the controller parameters $\mathbf u_k$, and
- $\pmb \beta = (\beta_1, \ldots, \beta_J)$ is a length $J$ vector of weights associated with each feature in $\mathbf x_i$.  

Here the vector $\pmb{\beta}$ is a _population_ parameter that is unknown to the controller, and may change over time.

### Rationality

We assume a weak form of rationality on the miner, which is that given two quantities $q_1$ and $q_2$ of the _same_ token, with $q_1 > q_2$, they will at least weakly prefer $q_1$ to $q_2$. 

We also know, from the specification of the proposed block rewards, that provided $D_i > e$,
$$\frac{d (r_{i1}/r_{i2})}{d D_i} >0,$$
i.e. relatively more of _qi_ is proposed when difficulty $D_i$ increases, since when $\mathbf u_k = (k_{qi}, k_{quai})$, 
$$\frac{r_{i1}}{r_{i2}} = \frac{u_{k1}D_i}{u_{k2}\log_2(D_i)} = \left ( \frac{u_{k1}}{u_{k2}} \right )\left ( \frac{D_i}{\log_2(D_i)} \right ). \qquad \qquad (\dagger)$$

Given the above, we would like to admit (but cannot _enforce_) that if relatively more _qi_ is proposed, then it is (weakly) more likely for the miner to accept _qi_. This is possible when:
1. The feature $\mathbf x_i$ is a function of $D_i$ such that $d \mathbf x_i / d D_i \geq 0$ component-wise, with at least one component, say $x_{i\hat j}$, such that the inequality is strict, and
2. The component of the population parameter $\pmb{\beta}$ associated with each such component $x_{i\hat j}$ is non-negative, i.e. $\beta_{\hat j} \geq 0$.

If this possibility is admitted, then 
$$\frac{d p_i}{d D_i} = p_i (1 - p_i) \sum_{j=1}^J  \beta_j\frac{\partial x_{ij}}{\partial D_i} \geq 0,$$
i.e. the higher the difficulty of a block, the (weakly) more likely it is for the miner to select _qi_ over _quai_ (all other things equal). A parsimonious specification of $\mathbf x_i$ providing this admissibility is presented below.

## Learning the Miner's Decision

Given a data set $\mathbf z_k$ made up of $n_k$ samples of pairs $(C_i, D_i)$ (this is the dataset collected since the last prime block $k$, up to and including the current prime block $k+1$), maximum likelihood estimation yields the controller's estimate $\pmb{\hat{\beta}}$ of the miner's decision population parameter vector $\pmb{\beta}$. This is [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) for binary classification. 

The estimate is the controller's best understanding of the impact of the features $\{\mathbf x_i\}_{i=1}^{n_k}$ on the distribution of miner decisions. Note that this learning is able to accommodate _changes_ in the population $\pmb{\beta}$, by learning the effects of such changes on observed miner decisions. Thus, the controller is able to continuously learn how miners value hashpower (difficulty) from its observations, and thus it is possible to (e.g.) use the testing framework to draw $\pmb{\beta}$ from a _distribution_ and examine the time taken for the controller to adjust to the new population value.

## The Controller's Objective: Stability via Indifference

The controller seeks to stabilize an imputed value of hashpower by adjusting the proposed block rewards so that the miner would have been _indifferent_ between receiving an award in _qi_ (token 1) or _quai_ (token 2). The interpretation of this is that _**deviations from indifference reveals that one token is more valuable than the other to a miner**_. In the case that one token (_qi_) is to reflect the value of hashpower, indifference between that token and a reference token (_quai_) is a _**focal point**_ from which the value of hashpower may be observed from miner decisions.

Given the above model for miner behavior, indifference is when $p_i = 0.5$, i.e. when the miner is equally likely to select _qi_ or _quai_ as the reward token type. Given $\pmb{\hat{\beta}}$, the miner's model imposes an _invariant surface_ that features must satisfy, i.e.
$$\pmb{\hat{\beta}}' \mathbf x_i = 0.$$

Refining this further requires a definition of the features $\mathbf x_i$.

### A Parsimonious Specification

A parsimonious specification is where each feature vector $\mathbf x_i$, $i = 1, \ldots, n_k$ has the form:
$$\mathbf x_i = (1, x_i) := (1, D_i/\log_2(D_i)).$$ 
Here the first feature is $1$ for every data point, so that the first weight $\beta_0$ is an intercept/'bias' term. The second feature is exactly the ratio of difficulties in equation $(\dagger)$ above. 

Using the above invariant surface, it is possible to derive a value $D_i = D^\star$ such that
$$\frac{D^\star}{\log_2(D^\star)} = -\frac{\hat{\beta_0}}{\hat{\beta_1}} =: x^\star(\pmb{\hat{\beta}}).$$

The value $D^\star$ is the difficulty level that would have to obtain in order for a miner to be (on average) indifferent between selecting token 1 and token 2 given $\pmb{\hat{\beta}}$, i.e. **given the controller's best understanding of miner behavior**. In what follows we will sometimes drop the dependence of $x^\star$ upon $\pmb{\hat{\beta}}$ for brevity, but it is important always to recall that $x^\star$ is derived from the _estimation problem_ the controller performs in finding a miner's indifference point.

Note that the miner's decision model requires that the estimates $\hat \beta_0 < 0$ and $\hat{\beta_1} > 0$, i.e. that the intercept/bias term is negative (the feature term $\hat{\beta_1}$ must be positive for the rationality reasons given above)--if this is not the case, then there exists _no_ difficulty level where miners are indifferent between _qi_ and _quai_ when $\mathbf x_i > 0$. By continuity this implies that one of the two tokens is always preferred, i.e. that $p_i > 0.5$ or that $p_i < 0.5$ _for any difficulty level_. Exploring controller update schemes for these edge cases that extend that presented below is an avenue for future research.

### The Loss Function

Although $D^\star$ is not part of $\mathbf z_k$ (or is v. unlikely to be), the form of the controller impact is known from relation $(\dagger)$, allowing the controller to treat $r_{i1}$ and $r_{i2}$ as _unspecified_ proposed block rewards $r_1$ and $r_2$, and to seek controller parameter values which (in a well-defined way) promote _stability_ by guiding the system toward a miner's indifference point.

Denote $r_{1}/r_{2}$ by a _parameter_ $R$. This and $(\dagger)$ define a second invariant surface that provides _those values of the control parameters that, when faced with difficulty $D^\star$, give reward ratio $R$_:
$$R u_2 = x^\star  u_1. \qquad \qquad (\ddagger)$$

The controller seeks to select $(u_1^\star, u_2^\star)$ to satisfy the following loss function defined by $(\ddagger)$:
$$\min_{u_1,u_2} \ell(x^\star, u_1, u_2; R) := R u_2 - x^\star u_1$$
such that $\ell(\cdot) \geq 0$.

Since the loss function is parameterized by $R$, a key question is what this value should be. As the latest available information of the proposed block rewards is $r_{1k}/r_{2k}$ for prime block $k$, this _could_ be used as an estimate of $R$. Alternatively, smoothing of values from $\mathbf z_k$, e.g. EWMA of the ratios $r_{1i}/r_{2i}$, could be used. An approach which treats the $R$ value as a pass-through of a "_gain_" from the difficulty controller is outlined in the "Gain as a Reward Ratio" section below.

As seen from $(\ddagger)$, either $u_1$ or $u_2$ may be set as a _numeraire_, reducing the required control space by one dimension, or allowing one of the parameters to be determined by other factors (such as the average difficulty, see the "Gain as a Control Variable" section below). This reduction is due to the simple form of $\mathbf x_i$ here, but more features will generally require additional restrictions on both $u_1$ and $u_2$ that must come from elsewhere (the dimension of the invariant surface grows in that case). 

### Gain

A _gain_ is required to ensure that the economic consequences of the controller "match up" with the difficulty adjustments that the difficulty controller performs. This gain may thus be dependent upon the average block difficulty $\bar D$ sourced from the difficulty controller, as this is a simple "summary statistic" of the difficulty 'trajectory' the difficulty controller is providing. The role of the gain is to set the scale of the proposed block rewards $r_1$ and $r_2$, adjusting that scale in response to changes in $\bar D$. (Note that although the average difficulty changes over time, for notational simplicity we denote by $\bar D$ the latest average block difficulty from the difficulty controller.)

#### Gain as a Control Variable

One supposition is to set $u_1 = g(\bar D)$ or $u_2 = g(\bar D)$ for some function $g$, i.e. to tie the control variable acting as a numeraire ($u_1$ or $u_2$) to this 'difficulty gain'. This is a 'black box' approach that does not change the overall controller methodology above (since only the ratio $u_1/u_2$ matters). However, it does not have a theoretical basis for its introduction, rather acting as an _ad hoc_ adjustment parameter.

It is likely that for controller stability at least $g'(\bar D) < 0$ (and perhaps $g''(\bar D) > 0$) everywhere, but this is not confirmed.

#### Gain as a Reward Ratio

An alternative that may provide more insight into scaling is to treat the unspecified parameter $R$ as a function of $\bar D$, allowing that to change in a consistent fashion relative to the difficulty controller. This has the advantage of 'closing the loop' on $R$ and providing an economically-relevant response to average difficulty $\bar D$. Since $R$ is meant to be an expression of a ratio of proposed block rewards, one may adopt the definition of $R(\bar D)$ as _the ratio of proposed block rewards that would have obtained_ if $\bar D$ had been the block difficulty under the previous controller parameters, i.e.:
$$R(\bar D) := \frac{u_{k1}}{u_{k2}}x(\bar D),$$
where $\mathbf u_k := (u_{k1}, u_{k2})$ is the vector of controller parameters from previous prime block $k$, and
$$x(\bar D) := \frac{\bar D}{\log_2(\bar D)},$$
i.e. that ratio of difficulties that would have obtained from difficulty level $\bar D$. (This has the same form as the feature specification for $x_i$ given above.)

Given this, the optimal controller parameter update for $u^\star_1$ from the loss function is (from $(\ddagger)$ above):
$$u_1^\star = \frac{u_2^\star}{u_{k2}}u_{k1}\frac{x(\bar D)}{x^\star(\pmb{\hat{\beta}})}.$$

If token 2 acts as a numeraire, then we may fix $u^\star_2 = u_{k2}$ (by extension, this sets $u_2$ to a single value $\bar u$). Letting $u_1^\star = u_{k1} + \Delta u_1$, this can be rearranged to yield the update "delta" for the controller paramter $u_1$:
$$\Delta u_1 = \left ( \frac{x(\bar D)}{x^\star(\pmb{\hat{\beta}})} - 1 \right )u_{k1}. \qquad \qquad (*)$$

This has an appealing interpretation for the controller: when the function of average difficulty $x(\bar D)$ is below the estimated value $x^\star(\pmb{\hat{\beta}})$, the controller parameter $u_1$ is adjusted proportionally downwards, so that the proposed block rewards, at the indifference difficulty level $D^\star$, move to reflect the block ratio $R(\bar D)$ for the average difficulty. **The controller is thus acting to _stabilize_ the block reward ratio around the miner's indifference, at the average difficulty of the system provided by the difficulty controller**. Similarly, when $x(\bar D) > x^\star(\pmb{\hat{\beta}})$ the controller parameter $u_1$ is adjusted upwards.

>[!info] Attenuation/Amplification
A manual "attenuation" parameter could also be added here, to adjust the sensitivity of $\Delta u_1$ to $x(\bar D)/x^\star(\pmb{\hat{\beta}})$. In that case $(*)$ above is slightly modified to
>$$\Delta u_1 = \alpha \left ( \frac{x(\bar D)}{x^\star(\pmb{\hat{\beta}})} - 1 \right )u_{k1}. \qquad \qquad (**)$$
> for an exogenous parameter $\alpha \in (0, \infty)$. Such attenuation may be used if other constraints must be met (e.g. conversions, secondary market operations etc.), or if the system's difficulty and/or preferences do not admit sufficient variability to avoid polar absorbing states (see [[#System Variability and Controller Performance]] below).
> ^123


### Using $u_2$ for Controller Updates

As the production Quai implementation will adjust $k_{quai}$ and leave $k_{qi}$ as numeraire, the above may be modified to provide the update rule in terms of $u_2$, with $u_1$ as numeraire. In that case we have from $(\ddagger)$:
$$u_2^\star = \frac{u_1^\star}{u_{k1}}u_{k2}\frac{x^\star(\pmb{\hat{\beta}})}{x(\bar D)},$$
and the controller update $\Delta u_2$ becomes
$$\Delta u_2 = \left ( \frac{x^\star(\pmb{\hat{\beta}})}{x(\bar D)} - 1 \right )u_{k2}, \qquad \qquad (*)$$
or with manual attenuation
$$\Delta u_2 = \alpha \left ( \frac{x^\star(\pmb{\hat{\beta}})}{x(\bar D)} - 1 \right )u_{k2}. \qquad \qquad (**)$$

### Controller Summary

The controller operates in the following way at prime block height $k+1$:
1. The controller receives data $\mathbf z_k$, $\mathbf u_k$ and $\bar D$;
1. The parameters $\pmb{\hat{\beta}}$ are estimated;
2. The quantity $x^\star(\pmb{\hat{\beta}})$ is computed;
3. The quantity $x(\bar D)$ is computed;
4. The controller computes e.g. $\Delta u_2$ and updates
$$u_{(k+1)2} = u_{k2} + \Delta u_2,$$
with $u_{k1} \equiv \bar u \: \forall k$ fixed from the beginning as numeraire.

## Miner Responsiveness

As designed, the controller operates under a _minimal_ set of assumptions regarding the behavior of the miner, especially with regard to how a miner may respond to features other than the ratio $x_i$ of difficulties.

If a model of miner behavior is _derived_ according to either a set of observable relationships, theoretical (posited) relationships, or both, and there is consensus that this model accurately represents actual miner behavior, then that model may be incorporated into the controller design by extending the feature vector $\mathbf{x}_i$ and rederiving the associated controller parameter updates.

Alternatively, different models of miner behavior may be treated within the parsimonious controller defined above. In that case there is _model misspecification_ in the sense that the controller operates with more limited information (i.e. a smaller feature vector) than that actually possessed by miners. This places the controller design problem within the _**robust control**_ paradigm. Although misspecified, the controller may be _calibrated_ to richer models of miner behavior to assess its ability to respond to shocks, to actual changes in user behavior resulting from controller parameter updates, or to other factors that are not explicitly included in the controller's "model of the world". Robust control in turn requires the derivation and examination of metrics that are used for _safety assessment_, i.e. to ensure that the controller operates as intended over a wide range of possible miner behaviors.

As an initial foray into robust control, several testing scenarios are included in the current engagement where 1) miner behavior experiences a large "preference shock" without misspecification, and 2) miner behavior includes an additional feature (the proposed block reward ratio, or a function thereof) so that the model is misspecified. It is interesting that in the latter case and indirect "feedback loop" is created from the controller's parameter updates and the miner's behavior, and so a criteria for controller success is that in light of such feedback the valuation of energy remains stable.

## System Variability and Controller Performance

The controller as specified should operate over a wide range of difficulties, and hence hashpower provided by miners. What is more crucial is to have sufficient variability in the average network difficulty and/or miner preferences to prevent the controller from saturating the proposed block reward ratio (in one direction or the other). For example, in a fixed, deterministic world with no preference changes and $x(\bar D) > x^\star(\hat \beta)$ always, from $(*)$ above the controller will adjust until the controller parameter $u_2$ ($k_{Quai}$) converges to zero (if the opposite inequality holds, the parameter will increase without bound).

The economic consequences of such an environment is that _learning cannot take place_, because there is insufficient variability in difficulty to map the effect of the feature vector $\mathbf x_i$ to miner decisions. To circumvent this, an additional attenuation/amplification 'tuning' using the $\alpha$ parameter from $(**)$ in the box "[[A Proposed Learning Controller for the Quai Network#^123|Attenuation/Amplification]]" above may be linked to e.g. difficulty variance, to ensure that the polar cases outlined above are avoided. This is a fruitful direction for future research.