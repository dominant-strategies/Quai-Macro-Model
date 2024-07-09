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