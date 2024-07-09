[[Quai to Qi Conversion Policy]]
[[Qi to Quai Conversion Policy]]
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

	    def convertQiToQuai(self, qiAmount):
	        if qiAmount < self.amtMin or qiAmount > self.qi:
	            return 0
	        self.qi -= qiAmount
	        quaiAmt = self.quaiRewardVal/self.qiRewardVal * qiAmount
	        self.convertedQuai[-1] += quaiAmt
	        self.quaiHash[-1] += quaiAmt
	        #print("convertQiToQuai:", "qi", self.qi, "quai", self.quai, "block", self.blockNum, "qiAmount", qiAmount, "quaiAmount", quaiAmt)
	        return quaiAmt