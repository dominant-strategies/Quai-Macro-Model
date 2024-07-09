## Model Additions

## To Process
	
	class Miner:
	    def __init__(self,marginalCost=0,costOfMoney=0.95):
	        self.marginalCost = marginalCost
	        self.costOfMoney = costOfMoney
	        self.hashDiff = 0
	        self.qi = 0
	        self.quai = 0
	    
	    def mine(self,tokenSupply,market):

	        takeQuai = market.quaiPriceVal < tokenSupply.quaiRewardVal * self.costOfMoney * self.marginalCost/tokenSupply.diff
	        takeQi = market.qiPriceVal < tokenSupply.qiRewardVal * self.marginalCost/tokenSupply.diff

	        if takeQuai and takeQi:
	            if tokenSupply.quaiRewardVal * self.costOfMoney > tokenSupply.qiRewardVal * market.quaiPerQiVal:
	                #print(tokenSupply.quaiRewardVal * self.costOfMoney, tokenSupply.qiRewardVal * market.quaiPerQiVal)
	                self.quai = tokenSupply.quaiRewardVal
	                self.qi = 0
	                return True
	            else:
	                self.quai = 0
	                self.qi = tokenSupply.qiRewardVal
	                return True
	        elif takeQuai:
	            self.quai = tokenSupply.quaiRewardVal
	            self.qi = 0
	            return True
	        elif takeQi:
	            self.quai = 0
	            self.qi = tokenSupply.qiRewardVal
	            return True
	        else:
	            self.quai = 0
	            self.qi = 0
	            return False

## Code

	import random as random
	    
	class Miner:
	    def __init__(self,marginalCost=0,costOfMoney=0.95):
	        self.marginalCost = marginalCost
	        self.costOfMoney = costOfMoney
	        self.hashDiff = 0
	        self.qi = 0
	        self.quai = 0
	    
	    def mine(self,tokenSupply,market):
	        #print("quaiRewardVal:",tokenSupply.quaiRewardVal,"qiRewardVal:",tokenSupply.qiRewardVal,"quaiPriceVal:",market.quaiPriceVal,"qiPriceVal:",market.qiPriceVal,"diff:",tokenSupply.diff,"costOfMoney:",self.costOfMoney,"marginalCost:",self.marginalCost)
	        takeQuai = market.quaiPriceVal < tokenSupply.quaiRewardVal * self.costOfMoney * self.marginalCost/tokenSupply.diff
	        #print("takeQuai:",takeQuai, market.quaiPriceVal, tokenSupply.quaiRewardVal * self.costOfMoney * self.marginalCost/tokenSupply.diff)
	        #print("quaiPriceVal:",market.quaiPriceVal,"quaiRewardVal:",tokenSupply.quaiRewardVal,"costOfMoney:",self.costOfMoney,"marginalCost:",self.marginalCost,"diff:",tokenSupply.diff)
	        takeQi = market.qiPriceVal < tokenSupply.qiRewardVal * self.marginalCost/tokenSupply.diff
	        #print("takeQi:", takeQi, market.qiPriceVal, tokenSupply.qiRewardVal * self.marginalCost/tokenSupply.diff)
	        if takeQuai and takeQi:
	            if tokenSupply.quaiRewardVal * self.costOfMoney > tokenSupply.qiRewardVal * market.quaiPerQiVal:
	                #print(tokenSupply.quaiRewardVal * self.costOfMoney, tokenSupply.qiRewardVal * market.quaiPerQiVal)
	                self.quai = tokenSupply.quaiRewardVal
	                self.qi = 0
	                return True
	            else:
	                self.quai = 0
	                self.qi = tokenSupply.qiRewardVal
	                return True
	        elif takeQuai:
	            self.quai = tokenSupply.quaiRewardVal
	            self.qi = 0
	            return True
	        elif takeQi:
	            self.quai = 0
	            self.qi = tokenSupply.qiRewardVal
	            return True
	        else:
	            self.quai = 0
	            self.qi = 0
	            return False