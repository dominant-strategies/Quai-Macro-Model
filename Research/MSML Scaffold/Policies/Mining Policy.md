## Description

Policy for mining and how long it takes to mine as well as difficulty adjustment.
## Called By
1. [[Mine Block Boundary Action]]
## Domain Spaces
1. [[Pre-Mining Space]]
## Followed By
1. [[Block Reward Policy]]
## Codomain Spaces
1. [[Mined Blocks Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Mining Policy V1
#### Description
A baseline mining policy
#### Logic
1. Create a space with no attributes
2. Assign the "Block Difficulty" as the array of difficulties presented in the domain
3. Add an attribute for "Mining Time" which is the sum of block difficulties / the aggregate hashpower taken from the domain
4. Find the new block difficulty by first grabbing the target time as params["Target Time"] * n_blocks then doing
$$\begin{aligned}
& e=\text { Target }- \text { Realized }=\text { Target }-\left(t_n-t_{n-1}\right) \\
& \text { Diff }_n=\text { Diff }_{n-1}^* *\left(1+\frac{P^* e}{\text { Target }}\right)
\end{aligned}$$

Then in the mechanism, the difficulty adjustment get smoothed.

