> [!info] Ported over from https://hackmd.io/@blockscience/rybNg7BFC
(These notes reflect thinking as at the time of writing and are not necessarily indicative of the final proposed controller design.)

This is a high-level system overview of the Quai token valuation subsystem, helping to formulate the requirements of a controller of the _qi_-to-_quai_ exchange rate.

## Transactions

Transactions $T^i$ arrive between times $t_{i-1}$ and $t_i$ for a partition of time $[0,T]$ into $I$ subintervals indexed by $i$, called the block height. Transactions $T^i$ are bundled into a block $B^i$.

## Block Proving

A block $B^i$ is proven using proof-of-work (here denoted "Proof of Entropy Minima", PoEM), where a **block hash** $H^i$ must meet a _criterion_ $h_i$ to be proposed as proven, i.e. $h_i(H^i) = 1$ if the criterion is met and $0$ otherwise. The criterion may change over block height (hence the subscript on the criterion function $h_i$), or it may be fixed.

**Assumption**: In what follows, it is assumed that the block hash $H^i$ is a number--furthermore, for the formalization below it is useful to assume that $H^i \in \mathbb{R}_+$ $\forall i$.

## Block Reward

The miner who successfully meets the hash criteria _first_ earns a reward. Miners are allowed to select between two reward types, _quai_ or _qi_. The quantity of each that may be produced as a proposed reward is the output of a type-specific function $f_s$ that depends upon both the block hash $H^i$ and a parameter specific to each reward type, $k^i_s$:
$$
  R^i_s = f_s(H^i, k^i_s),
$$
with $s \in S := \{ \text{Quai}, \text{Qi} \}$. Note that the miner selects only _one_ type to receive their reward (see below).

**Assumption**: The _histories_ of:
1. The proposed block rewards of each type, i.e. $\mathcal R(i) := \{R^j_{\text{Quai}}, R^j_{\text{Qi}}\}_{j \leq i}$, and 
2. The block hashes, i.e. $\mathcal H(i) := \{H^j\}_{j \leq i}$, 

are assumed to be fully observable by all participants up through block height $i$.

## The Miner Decision

A miner may decide to invest resources to solving the PoEM problem, or may elect to not solve the problem. This decision depends upon the miner's resource costs and the difficulty hash $H^i$ at block height $i$, and takes place between times $t_{i-1}$ and $t_i$. Fully modeling this decision will require defining:
1. The time at which difficulty $H^i$ is revealed, and
2. The resource costs associated with a miner.

If _no_ miner elects to solve the problem then the associated block $B^i$ is _empty_. An empty block changes the resulting difficulty of the hash. 

**Assumption**: The result of an empty block is to _lower_ the difficulty of the PoEM problem, i.e. if block $B^i$ is empty, then $H^{i+1} < H^i$.

Note that if it is the case (as in the current specification) that
$$
  \frac{\partial R^i_s}{\partial H^i} > 0,
$$
i.e. that the proposed block reward is increasing in the difficulty of the problem, then the miner may still find it in their best interest to leave block $B^{i+1}$ empty as well, if the cost savings from the lowered difficulty is offset by the lowered proposed block reward. 

:::info
Thus, for it to be the case that _some_ miner finds it worthwhile to prove a non-empty block, a sufficient condition is that this miner's resource cost as a function of difficulty is _**convex**_, and that there exists a 'break-even' point in the difficulty (hash) where the miner is just indifferent between proving a non-empty block and not proving the block, when computing their expected return from proving.
:::

If this is so, then the difficulty of the problem will fall until the break-even point is passed, and there will be at least one successful miner proving a non-empty block.

Note that from the perspective of a controller, empty blocks do not convey information leading to any explicit change in the terms of trade or conversion rate between _qi_ and _quai_, as the decision to not prove a block is an _economic_ decision and depends upon the cost structure of the miner, which is assumed to be an idiosyncratic attribute of the miner population. As such, then, empty blocks should result in a "quiescent" period of controller updates, where the volatility of the process is low in the absence of a "signal" from miner behavior. This quiescence is a testable implication of any controller mechanism selected.

### A successful miner

We focus in what follows on _successful_ miners, i.e. those for whom it is at least as profitable as their next best alternative use of their resources to attempt to prove a block (in expected value terms), and in so attempting they are the first to solve the PoEM problem. 

A successful miner for block height $i$ may elect to receive their reward in _quai_ or _qi_, by comparing the proposed block rewards $R^i_{\text{Quai}}$ and $R^i_{\text{Qi}}$ given the difficulty hash $H^i$.

**Assumption**: A miner selects their reward type from $S = \{ \text{Quai}, \text{Qi} \}$ according to which type carries, for them, the higher reward $V_s$.  _How_  this value is determined is private information to the miner, but generally we assume rationality in a 'low-level' sense:
$$
\frac{\partial V_s}{\partial R^i_s} >0 \quad \forall i,s,
$$
i.e. that (all other things equal) miner preferences are monotonically increasing in token quantity. Note that this is _not_ the same as:
$$
  \frac{dV_s}{dR^i_s} > 0,
$$
as the latter includes not only $\frac{\partial V_s}{R^i_s}$ but also the effects of the increased reward in token $s$ on other factors influencing valuation--examples include (but may not be present, or may not be limited to) the token conversion rate, the secondary market exchange rate, the planning horizon etc. (Note that here and in what follows infinitesimal notation is adopted to make distinguishing between e.g. partial and total derivatives easy, but for implementation discrete 'delta' notation may also be used.)

To encapsulate the above we represent a successful miner's decision at block height $i$ with a _decision function_ $D^i$, where $D^i(R^i_\text{Quai}, R^i_{\text{Qi}}) \in S$. The **realized** block reward provided at that block height is then $R^i_{D^i}$. To facilitate notation in what follows, we adopt the notation $Y^i_s$ as the process which at every block height $i$ for token $s \in S$:
$$
  Y^i_s := 
\begin{cases}
  R^i_{D^i} & D^i = s, \\
  Y^{i-1}_s & \text{otherwise}.
\end{cases}
$$
This process thus tracks the actual block rewards of each token that are emitted each block height, i.e. those actually selected by miners, and for the other token tracks the _last block reward value_ that a miner selected for that token. This provides a useful representation of the miner's decision-making when selecting which token to receive as their block reward.


**Assumption**: The history of miner decisions $\mathcal D(i) := \{D^j\}_{j \leq i}$, and the history of actual block rewards  $\mathcal Y(i) := \{Y_{\text{Quai}}^j, Y^j_{\text{Qi}} \}_{j \leq i}$ , are observable by all participants up through block height $i$.

## Quai-to-Qi Protocol Conversion

Any network participant may exchange _qi_ for _quai_ at a conversion rate $C^i$ at block height $i$, which applies for times $t \in [t_{i-1},t_i]$. 

**Assumption**: The function $C$ defining the conversion rate depends upon the history of proposed block rewards through $i$,  $\mathcal R(i)$,
so that
$$
  C^i = C(\mathcal R(i)).
$$

:::info
For example, under Quai's [current proposed specification](https://docs.qu.ai/learn/tokenomics/token-dynamics/conversions) there is no explicit history dependence and the conversion rate is assumed to be equal to the protocol's  _proposed terms of trade_ from the proposed block rewards:
$$
  C^i := \frac{R^i_{\text{Quai}}}{R^i_\text{Qi}}.
$$
:::
Let the history of the conversion rate through block height $i$ be denoted $\mathcal C(i) := \{C^j\}_{j \leq i}$.
## Secondary Market

There may be a secondary market (or markets) that allows market participants to exchange _qi_ for _quai_ and vice-versa.

**Assumption**: There is a noisy 'representative' exchange rate at any time $t \in [0,T]$, denoted $p(t)$, from _qi_ to _quai_ that is itself a stochastic summary statistic of all secondary markets. The history of this representative exchange rate may or may not be observable by participants--for the controller below the history is observable but the random influences that impact $p(t)$ are not, and so an estimator must be formed.

## Controller

A _controller_ adjusts the values of $k_{\text{Quai}}$ and $k_{\text{Qi}}$ so that a performance metric or **loss function** $F$ is minimized. At block height $i$ the loss function _may_ depend upon the following:

:::info
1. The history of proposed block rewards through $i$, $\mathcal R(i)$;
3. The history of block hashes through $i$, $\mathcal H(i)$;
5. The history of miner decisions through $i$, $\mathcal D(i)$;
6. The history of a representative exchange rate **estimator** through $i$, $\mathcal P(i) := \{P^j\}_{j \leq i}$, where (for each $j$) $P^j$ is a _consistent estimator_ of the prices that occur between $t_{j-1}$ and $t_j$. An example would be e.g. a noisy simple window average,
$$
  P^j := \frac{1}{(t_j - t_{j-1})}\mathbb{E}^j \left ( \int_{t_{j-1}}^{t_j} p(t)dt \right ),
$$ 
or a time-weighted moving average (TWAP), etc. 
:::

Generally, at block height $i$ the controller selects block reward parameters $k^i_{\text{Quai}}$ and $k^i_{\text{Qi}}$ such that 
$$
  (k^i_{\text{Quai}}, k^i_{\text{Qi}}) \in \mathop{\arg\min}\limits_{k_{\text{Quai}},k_{\text{Qi}}}\: F \left ( \mathcal R(i), \mathcal H(i), \mathcal  P(i) \: | \: \mathcal D(i) \right ).
$$

**Assumption**: The estimated secondary market price history $\mathcal P(i)$ only has an impact through miner decisions, i.e. through their valuations $(V_{\text{Qi}}, V_{\text{Quai}})$. There does not exist a protocol-aware oracle of the secondary market price which can inform the controller.

Under this assumption, the problem is reduced to only protocol observables, i.e
$$
  (k^{i}_{\text{Quai}}, k^{i}_{\text{Qi}}) \in \mathop{\arg\min}\limits_{k_{\text{Quai}},k_{\text{Qi}}}\: F \left ( \mathcal R(i), \mathcal H(i) \: | \: \mathcal D(i) \right ),
$$
where the loss function no longer has an explicit dependence upon $\mathcal P(i)$.

Finally, it is useful to note that in this general setup, dependencies upon functions of e.g. proposed or actual block rewards have been suppressed--in particular, the conversion rate history $\mathcal C(i)$ and realized block reward history $\mathcal Y(i)$, as seen below, may be used as sufficient statistics in the loss function, but as they are defined by the proposed block reward history $\mathcal R(i)$ (and in the latter case, also the decision history $\mathcal D(i)$) they are not listed in the general form above. 

## Objective

The objective of the controller is to help ensure that the _qi_ token exhibits the properties of a stablecoin, reflecting (in some sense) the cost of energy. The cost of energy is proxied by the difficulty of the problem being solved, which is in turn represented by the hash ($H^i$ at block height $i$). A more difficult problem is assumed to be more costly in energy to solve, thus one requirement should be that given the conversion rate $C^i$ from _qi_ to _quai_ at block height $i$, 
$$
  \frac{d C^i}{d H^i} < 0,
$$
i.e. it should require more _qi_ to obtain the same quantity of _quai_ when energy is more costly.

This is verified if the following specifications of the block reward proposals (as given by the current specification) are used:
$$\begin{align}
  R^i_{\text{Qi}} &= f_{\text{Qi}} := \frac{1}{k^i_{\text{Qi}}}H^i, \\
   R^i_{\text{Quai}} &= f_{\text{Quai}} :=  k^i_{\text{Quai}}  \log_2(H^i),
\end{align}$$
where the conversion rate $C^i$ is defined as the implied _spot rate_ from the proposals, i.e.
$$
  C^i := \frac{\partial R^i_{\text{Quai}}}{\partial R^i_{\text{Qi}}},
$$
and where
$$
  \frac{\partial R^i_{\text{Quai}}}{\partial R^i_{\text{Qi}}} = \left ( \frac{ k^i_{\text{Quai}} k^i_{\text{Qi}}   }{\ln(2) H^i} \right )= \left ( \frac{R^i_{\text{Quai}}}{R^i_{\text{Qi}}} \right ) \left ( \frac{1}{\ln \left ( H^i \right )} \right ).
$$


### Tracking the terms of trade

Using the conversion rate, the loss function of the controller should penalize block-by-block deviations of the conversion rate from the protocol's imputed terms of trade. Note that the imputed terms of trade are  defined with respect to _realized_ block rewards, i.e. those tokens actually emitted by the protocol. To reflect this, define
$$
 \mathcal T(i) := \left \{ \frac{Y^j_{\text{Quai}}}{Y^j_\text{Qi}}\right \}_{j \leq i}
$$
as the history up to block height $i$ of the imputed terms of trade from realized miner decisions on which token to receive.

This ensures that the protocol's conversion from _qi_ to _quai_ (and vice-versa) can respond to miner preferences of receiving one or the other token, which encapsulates their valuations $(V_{\text{Qi}}, V_\text{Quai})$ and hence their assessment of e.g. the secondary market price history $\mathcal P(i)$, while reflecting the terms of trade as represented by the _qi_-to-_quai_ spot rate given by the history $\mathcal C^i$.

Let the measure of the deviation of the spot rate from the terms of trade be denoted by some function of the conversion rate and terms of trade histories, $m(\mathcal C(i), \mathcal T(i)) \geq 0$.

### Acting as a stablecoin

For _qi_ to act as a stablecoin the protocol must provide, in addition to a means of tracking the cost of energy (as above), a _predictable_ reflection of this cost. To achieve this requires adopting a measure of the _volatility_ of the resulting terms of trade process. The loss function should penalize large values of the variance of the history (treated as a time series process).

Let the measure of the volatility of the history be denoted by some function $\sigma(\mathcal T(i)) \geq 0$.

### A candidate loss function

A candidate loss function is thus:
$$
  F \left ( \mathcal R(i), \mathcal H(i)  \: | \: \mathcal D(i) \right ) := m(\mathcal C(i), \mathcal T(i)) + \frac{1}{2} \sigma^2(\mathcal{T(i)}).
$$

Note that finding the minimum of the loss function will not be as straightforward as finding an interior condition, since miner decisions are discrete.


