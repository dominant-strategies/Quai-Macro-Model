
## Prior Code
	    def quaiPrice(self,supply): #qaui price per hash
	        self.quaiPriceVal = self.quaiPriceVal * (np.random.randn() * self.growth_rate + (1 - self.growth_bias))
	        # if supply.blockNum % 5000 == 0:
	        #     self.quaiPriceVal = self.quaiPriceVal * .9
	