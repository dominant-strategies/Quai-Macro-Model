## Description

Mechanism which takes care of unlocking of tokens
## Called By
1. [[Unlock Tokens Policy]]
## Domain Spaces
1. [[Unlock Tokens Space]]
## Constraints
## Logic
Reduce the locked tokens by the domain inputs and set the unlock schedule to the domain input

## Updates

1. [[Global]].[[Global State-Locked Quai Supply|Locked Quai Supply]]
2. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
3. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
4. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
