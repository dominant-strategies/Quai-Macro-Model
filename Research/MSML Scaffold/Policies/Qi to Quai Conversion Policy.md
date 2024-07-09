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