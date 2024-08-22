## Description

A mechanism which slowly updates the difficulty over an adjustment period.
## Called By
## Domain Spaces
1. [[Block Difficulty Space]]
## Constraints
## Logic
(CurrentDifficulty * (Period-1) + NewDifficulty) / Period

## Updates

1. [[Global]].[[Global State-Block Difficulty|Block Difficulty]]
