## Description

The policy which determines the amount of Quai or Qi exchanged.
## Called By
1. [[Conversions Boundary Action]]
## Domain Spaces
1. [[Conversion Space]]
## Followed By
1. [[Mint Qi Tokens Mechanism]]
2. [[Mint Quai Tokens Mechanism]]
3. [[Burn Qi Tokens Mechanism]]
4. [[Burn Quai Tokens Mechanism]]
5. [[Update Historical Converted Qi Mechanism]]
6. [[Update Historical Converted Quai Mechanism]]
## Codomain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Qi Space]]
4. [[Quai Space]]
5. [[Conversion Log Space]]
6. [[Conversion Log Space]]
## Constraints
## Parameters Used
1. [[Minimum Qi Conversion Amount]]
2. [[Minimum Quai Conversion Amount]]
## Metrics Used
1. [[Current Block Reward Ratio Metric]]
## Policy Options
### 1. Block Reward Ratio Conversion Policy
#### Description
The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].
#### Logic
If the asset is Quai, then return spaces for Quai as -TokenValue and 1/[[Current Block Reward Ratio Metric]] * TokenValue for Qi.
    Else return Qi as -Token Value and [[Current Block Reward Ratio Metric]] * TokenValue for Quai



## Old Code

	    def convertQiToQuai(self, qiAmount):
	        if qiAmount < self.amtMin or qiAmount > self.qi:
	            return 0
	        self.qi -= qiAmount
	        quaiAmt = self.quaiRewardVal/self.qiRewardVal * qiAmount
	        self.convertedQuai[-1] += quaiAmt
	        self.quaiHash[-1] += quaiAmt
	        #print("convertQiToQuai:", "qi", self.qi, "quai", self.quai, "block", self.blockNum, "qiAmount", qiAmount, "quaiAmount", quaiAmt)
	        return quaiAmt

## Old Code

	    def convertQuaiToQi(self, quaiAmount):
	        if quaiAmount < self.amtMin or quaiAmount > self.quai:
	            return 0
	        self.quai -= quaiAmount
	        qiAmt = self.qiRewardVal/self.quaiRewardVal * quaiAmount
	        self.convertedQi[-1] += qiAmt
	        self.qiHash[-1] += qiAmt
	        #print("convertQuaiToQi:", "qi", self.qi, "quai", self.quai, "block", self.blockNum, "qiAmount", qiAmt, "quaiAmount", quaiAmount)
	        return qiAmt