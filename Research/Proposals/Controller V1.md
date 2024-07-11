
## Control Surface

what can the controller actually control (eg what variables can it set, and on what time frame can it set them)?
$u \in U$

Actions:
1. [[Update K Quai Mechanism|Setting]] $k_{quai}$ 
	1. The variable of [[Global State - K Quai|kquai]] is set
	2. Timeframe of setting is TBD
2. [[Update K Qi Mechanism|Setting]] $k_{qi}$ 
	1. The variable of [[Global State - K Qi|kqi]] is set
	2. Timeframe of setting is TBD

Codomain:
[[Controller Output Space]]

$$U = \{kquai: CoefficientType, kqi: CoefficientType\}$$

## Observable States

what facts can the controller measure, read, or deterministically computed.
$y \in Y$

## State Space

what is the collection of phenomena of interest that appear within our model
$x \in X$
x can in our model contain information that we treat as private actors of physical in the world

## Observation Process

this is the modeled relationship between the phenomena of interest and the observables
$h: X \rightarrow Y$
it derives observations $y = h(x)$ from the current state

## Boundary Conditions

the set of inputs to the system dynamics which are taken by actors or processes not under our control
$v\in V$
think of this as the admissible action space for the users

## Laws of Motion

given the prior state, the control action and the user actions how the system state evolves
$f: X \times U \times V \rightarrow X$
also denoted $x^+ = f(x, u, v)

## Behavioral Policy

this is the process that generates the inputs $v\in V$
$b: X \rightarrow V$
this can be as simple as lookup tables and as complex as heterogenous multi-agent strategic behavior


## Control Policy

this is how we compute our control action $u$ from our observed data $y$
$g: Y \rightarrow U$