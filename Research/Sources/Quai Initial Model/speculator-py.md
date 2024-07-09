## Model Additions

## To Process

	    
	class Speculator:
	    def __init__(self, costOfMoney=0.95, futureExpectedValue=1.01, id=0, amtMin=0.0001, duration=50, type=0, liqBidSize=100,increment=0.01):

	        self.costOfMoney = costOfMoney
	        self.futureExpectedValue = futureExpectedValue
	        self.convertedQuai = deque(maxlen=duration)
	        self.convertedQi = deque(maxlen=duration)
	        self.history = []
	        self.id = id
	        self.amtMin = amtMin
	        self.maxBidSize = 100
	        self.type = type
	        self.liqBidSize = liqBidSize
	        self.increment = increment
	        self.duration=duration
	
	    def update(self):
	        self.quai += self.convertedQuai[-self.duration] if len(self.convertedQuai) > self.duration else 0
	        self.qi += self.convertedQi[-self.duration] if len(self.convertedQi) > self.duration else 0  
	        self.convertedQi.append(0)
	        self.convertedQuai.append(0)  
	
	    def bid(self,market,supply):
	        fev = self.futureExpectedValue + market.currentFEVval
	        #speculator can: buy qi, sell qi, buy quai, sell quai, or do nothing
	        if market.qiPriceVal > 1/supply.kqi:
	            if self.futureExpectedValue > 1:
	                if 1/self.futureExpectedValue * market.qiPriceVal > 1/supply.kqi and self.quai > self.amtMin:
	                    return 0, self.bidAmt(self.quai), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id #buy qi, quantity: # of Quai, price: Qi per Quai
	                elif self.qi > self.amtMin: 
	                    return 1, self.bidAmt(self.qi), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id #sell qi, quantity: # of Qi, price: Qi per hash
	            elif self.quai > self.amtMin:
	                return 0, self.bidAmt(self.quai), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id  #buy qi
	        else:
	            if self.futureExpectedValue < 1:
	                if 1/self.futureExpectedValue * market.qiPriceVal < 1/supply.kqi and self.qi > self.amtMin:
	                    return 1, self.bidAmt(self.qi), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id 
	                elif self.quai > self.amtMin: 
	                    return 0, self.bidAmt(self.quai), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id 
	            elif self.qi > self.amtMin:
	                return 1, self.bidAmt(self.qi), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id 
	        return 2, 0, 0, self.id
	    
	    #Symetric liquidity provider. This speculator will always put up the entire amount of their quai and qi for sale at 0.5-1% increments of the current market price with 10% in each step.
	    def liquid(self, market, supply, i):
	        increments = 10
	        if self.qi > 0 and i%2==0:
	            #print("liquid:", "qi", self.qi, "quai", self.quai, "block", supply.blockNum, "id", self.id)
	            #print("bidAmt qi:", min(self.liqBidSize,self.qi), "price:", 1/(supply.kqi * market.quaiPriceVal)*(1-i*self.increment), "id", self.id, "i", i)
	            return 1, min(self.liqBidSize,self.qi), 1/(supply.kqi * market.quaiPriceVal)*(1+i*self.increment), self.id
	        if self.quai > 0:
	            #print("liquid:", "qi", self.qi, "quai", self.quai, "block", supply.blockNum, "id", self.id)
	            #print("bidAmt quai:", min(self.liqBidSize,self.quai), "price:", 1/(supply.kqi * market.quaiPriceVal)*(1+i*self.increment), "id", self.id, "i", i)
	            return 0, min(self.liqBidSize,self.quai), 1/(supply.kqi * market.quaiPriceVal)*(1-i*self.increment), self.id
	                
	        return 2, 0, 0, self.id
	
	    def bidAmt(self, amt):
	        return min(amt,self.maxBidSize)
	    
	    def take(self, market, supply, speculators, num):
	        initQi = self.qi
	        initQuai = self.quai
	        soldQi = 0
	        soldQuai = 0
	        
	        fevQiPerQuai = self.futureExpectedValue/(supply.kqi * market.quaiPriceVal)
	        fevQiPerQuaiDiscounted = fevQiPerQuai * self.costOfMoney
	        eqQiPrice = 1/supply.kqi
	        #speculator can: buy qi, sell qi, buy quai, sell quai, or do nothing. The goal of the speculator is to maximize their hash
	        if market.qiPriceVal > eqQiPrice: #if the market value of qi is greater than the equilibrium price
	            if self.futureExpectedValue > 1: #if the future expected value of quai is greater than 1
	                if 1/self.futureExpectedValue * market.qiPriceVal > eqQiPrice: #if the market value of qi discounted by the future expected appreciation of quai is greater than the equilibrium price
	                    if self.quai > 0 and len(market.sellQi) > 0:
	                        bid = self.bidAmt(self.quai)
	                        soldQuai, boughtQi = market.spotBuyQi(bid, fevQiPerQuai,speculators, num, supply) #buy qi, quantity: # of Quai, price: Qi per Quai
	                        self.quai += soldQuai
	                        self.qi += boughtQi
	                        remainder = bid + soldQuai
	                        if remainder > 0 and fevQiPerQuaiDiscounted > eqQiPrice:
	                            #print("Convert1:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.quai -= remainder
	                            self.convertedQi[-1] = supply.convertQuaiToQi(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	                else: #if the market value of qi discounted by the future expected appreciation of quai is less than the equilibrium price1
	                    if self.qi > 0 and len(market.buyQi) > 0:
	                        bid = self.bidAmt(self.qi)
	                        soldQi, boughtQuai = market.spotSellQi(bid, fevQiPerQuai,speculators, num, supply) #sell qi, quantity: # of Qi, price: Qi per hash
	                        self.qi += soldQi
	                        self.quai += boughtQuai
	                        remainder = bid + soldQi
	                        if remainder > 0 and fevQiPerQuaiDiscounted < eqQiPrice:
	                            #print("Convert2:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.qi -= remainder
	                            self.convertedQuai[-1] = supply.convertQiToQuai(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	            else:
	                if self.quai > 0 and len(market.sellQi) > 0:
	                    bid = self.bidAmt(self.quai)
	                    soldQuai, boughtQi = market.spotBuyQi(bid, fevQiPerQuai,speculators, num, supply) #buy qi
	                    self.quai += soldQuai
	                    self.qi += boughtQi
	                    remainder = bid + soldQuai
	                    if remainder > 0:
	                        #print("Convert3:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                        self.quai -= remainder
	                        self.convertedQi[-1] = supply.convertQuaiToQi(remainder)
	                        #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	        else:            
	            if self.futureExpectedValue < 1:
	                if 1/self.futureExpectedValue * market.qiPriceVal < eqQiPrice:
	                    if self.qi > 0 and len(market.buyQi) > 0:
	                        bid = self.bidAmt(self.qi)
	                        soldQi, boughtQuai =  market.spotSellQi(bid, fevQiPerQuai,speculators, num, supply)
	                        self.qi += soldQi
	                        self.quai += boughtQuai
	                        remainder = bid + soldQi
	                        if remainder > 0 and fevQiPerQuaiDiscounted < eqQiPrice:
	                            #print("Convert4:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.qi -= remainder
	                            self.convertedQuai[-1] = supply.convertQiToQuai(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	                else: 
	                    if self.quai > 0 and len(market.sellQi) > 0:
	                        bid = self.bidAmt(self.quai)
	                        soldQuai, boughtQi = market.spotBuyQi(bid, fevQiPerQuai,speculators, num, supply)
	                        self.quai += soldQuai
	                        self.qi += boughtQi
	                        remainder = bid + soldQuai
	                        if remainder > 0 and fevQiPerQuaiDiscounted > eqQiPrice:   
	                            #print("Convert5:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.quai -= remainder
	                            self.convertedQi[-1] = supply.convertQuaiToQi(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	            else:
	                if self.qi > 0 and len(market.buyQi) > 0:
	                    bid = self.bidAmt(self.qi)
	                    soldQi, boughtQuai = market.spotSellQi(bid, fevQiPerQuai, speculators, num, supply)
	                    self.qi += soldQi
	                    self.quai += boughtQuai
	                    remainder = bid + soldQi
	                    if remainder > 0:
	                        #print("Convert6:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                        self.qi -= remainder
	                        self.convertedQuai[-1] = supply.convertQiToQuai(remainder)
	                        #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	                
	
	        #if soldQi != 0 or soldQuai != 0:
	            #print("take:", "qi", self.qi, "quai", self.quai, "block", num, "id", self.id)
	
	        market.book(speculators,supply)
	        return self.qi - initQi, self.quai - initQuai
	
	    def make(self, deltaQi, deltaQuai, num, market, supply, speculators):
	        if self.qi + deltaQi < 0 or self.quai + deltaQuai < 0:
	            #print("ERROR: make: qi", deltaQi,"quai", deltaQuai, "num:", num, "qi", self.qi, "quai", self.quai, "id", self.id)
	            #market.book(speculators,supply)
	            return False
	        self.qi += deltaQi
	        self.quai += deltaQuai
	        #print("make:", self.qi, self.quai, num, self.id)
	        return True
## Code

	import random as random
	from collections import deque
	    
	class Speculator:
	    def __init__(self, costOfMoney=0.95, futureExpectedValue=1.01, id=0, amtMin=0.0001, duration=50, type=0, liqBidSize=100,increment=0.01):
	        self.qi = 10000
	        self.quai = 10000
	        self.costOfMoney = costOfMoney
	        self.futureExpectedValue = futureExpectedValue
	        self.convertedQuai = deque(maxlen=duration)
	        self.convertedQi = deque(maxlen=duration)
	        self.history = []
	        self.id = id
	        self.amtMin = amtMin
	        self.maxBidSize = 100
	        self.type = type
	        self.liqBidSize = liqBidSize
	        self.increment = increment
	        self.duration=duration
	
	    def update(self):
	        self.quai += self.convertedQuai[-self.duration] if len(self.convertedQuai) > self.duration else 0
	        self.qi += self.convertedQi[-self.duration] if len(self.convertedQi) > self.duration else 0  
	        self.convertedQi.append(0)
	        self.convertedQuai.append(0)  
	
	    def bid(self,market,supply):
	        fev = self.futureExpectedValue + market.currentFEVval
	        #speculator can: buy qi, sell qi, buy quai, sell quai, or do nothing
	        if market.qiPriceVal > 1/supply.kqi:
	            if self.futureExpectedValue > 1:
	                if 1/self.futureExpectedValue * market.qiPriceVal > 1/supply.kqi and self.quai > self.amtMin:
	                    return 0, self.bidAmt(self.quai), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id #buy qi, quantity: # of Quai, price: Qi per Quai
	                elif self.qi > self.amtMin: 
	                    return 1, self.bidAmt(self.qi), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id #sell qi, quantity: # of Qi, price: Qi per hash
	            elif self.quai > self.amtMin:
	                return 0, self.bidAmt(self.quai), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id  #buy qi
	        else:
	            if self.futureExpectedValue < 1:
	                if 1/self.futureExpectedValue * market.qiPriceVal < 1/supply.kqi and self.qi > self.amtMin:
	                    return 1, self.bidAmt(self.qi), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id 
	                elif self.quai > self.amtMin: 
	                    return 0, self.bidAmt(self.quai), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id 
	            elif self.qi > self.amtMin:
	                return 1, self.bidAmt(self.qi), self.futureExpectedValue/(supply.kqi * market.quaiPriceVal),self.id 
	        return 2, 0, 0, self.id
	    
	    #Symetric liquidity provider. This speculator will always put up the entire amount of their quai and qi for sale at 0.5-1% increments of the current market price with 10% in each step.
	    def liquid(self, market, supply, i):
	        increments = 10
	        if self.qi > 0 and i%2==0:
	            #print("liquid:", "qi", self.qi, "quai", self.quai, "block", supply.blockNum, "id", self.id)
	            #print("bidAmt qi:", min(self.liqBidSize,self.qi), "price:", 1/(supply.kqi * market.quaiPriceVal)*(1-i*self.increment), "id", self.id, "i", i)
	            return 1, min(self.liqBidSize,self.qi), 1/(supply.kqi * market.quaiPriceVal)*(1+i*self.increment), self.id
	        if self.quai > 0:
	            #print("liquid:", "qi", self.qi, "quai", self.quai, "block", supply.blockNum, "id", self.id)
	            #print("bidAmt quai:", min(self.liqBidSize,self.quai), "price:", 1/(supply.kqi * market.quaiPriceVal)*(1+i*self.increment), "id", self.id, "i", i)
	            return 0, min(self.liqBidSize,self.quai), 1/(supply.kqi * market.quaiPriceVal)*(1-i*self.increment), self.id
	                
	        return 2, 0, 0, self.id
	
	    def bidAmt(self, amt):
	        return min(amt,self.maxBidSize)
	    
	    def take(self, market, supply, speculators, num):
	        initQi = self.qi
	        initQuai = self.quai
	        soldQi = 0
	        soldQuai = 0
	        
	        fevQiPerQuai = self.futureExpectedValue/(supply.kqi * market.quaiPriceVal)
	        fevQiPerQuaiDiscounted = fevQiPerQuai * self.costOfMoney
	        eqQiPrice = 1/supply.kqi
	        #speculator can: buy qi, sell qi, buy quai, sell quai, or do nothing. The goal of the speculator is to maximize their hash
	        if market.qiPriceVal > eqQiPrice: #if the market value of qi is greater than the equilibrium price
	            if self.futureExpectedValue > 1: #if the future expected value of quai is greater than 1
	                if 1/self.futureExpectedValue * market.qiPriceVal > eqQiPrice: #if the market value of qi discounted by the future expected appreciation of quai is greater than the equilibrium price
	                    if self.quai > 0 and len(market.sellQi) > 0:
	                        bid = self.bidAmt(self.quai)
	                        soldQuai, boughtQi = market.spotBuyQi(bid, fevQiPerQuai,speculators, num, supply) #buy qi, quantity: # of Quai, price: Qi per Quai
	                        self.quai += soldQuai
	                        self.qi += boughtQi
	                        remainder = bid + soldQuai
	                        if remainder > 0 and fevQiPerQuaiDiscounted > eqQiPrice:
	                            #print("Convert1:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.quai -= remainder
	                            self.convertedQi[-1] = supply.convertQuaiToQi(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	                else: #if the market value of qi discounted by the future expected appreciation of quai is less than the equilibrium price1
	                    if self.qi > 0 and len(market.buyQi) > 0:
	                        bid = self.bidAmt(self.qi)
	                        soldQi, boughtQuai = market.spotSellQi(bid, fevQiPerQuai,speculators, num, supply) #sell qi, quantity: # of Qi, price: Qi per hash
	                        self.qi += soldQi
	                        self.quai += boughtQuai
	                        remainder = bid + soldQi
	                        if remainder > 0 and fevQiPerQuaiDiscounted < eqQiPrice:
	                            #print("Convert2:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.qi -= remainder
	                            self.convertedQuai[-1] = supply.convertQiToQuai(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	            else:
	                if self.quai > 0 and len(market.sellQi) > 0:
	                    bid = self.bidAmt(self.quai)
	                    soldQuai, boughtQi = market.spotBuyQi(bid, fevQiPerQuai,speculators, num, supply) #buy qi
	                    self.quai += soldQuai
	                    self.qi += boughtQi
	                    remainder = bid + soldQuai
	                    if remainder > 0:
	                        #print("Convert3:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                        self.quai -= remainder
	                        self.convertedQi[-1] = supply.convertQuaiToQi(remainder)
	                        #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	        else:            
	            if self.futureExpectedValue < 1:
	                if 1/self.futureExpectedValue * market.qiPriceVal < eqQiPrice:
	                    if self.qi > 0 and len(market.buyQi) > 0:
	                        bid = self.bidAmt(self.qi)
	                        soldQi, boughtQuai =  market.spotSellQi(bid, fevQiPerQuai,speculators, num, supply)
	                        self.qi += soldQi
	                        self.quai += boughtQuai
	                        remainder = bid + soldQi
	                        if remainder > 0 and fevQiPerQuaiDiscounted < eqQiPrice:
	                            #print("Convert4:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.qi -= remainder
	                            self.convertedQuai[-1] = supply.convertQiToQuai(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	                else: 
	                    if self.quai > 0 and len(market.sellQi) > 0:
	                        bid = self.bidAmt(self.quai)
	                        soldQuai, boughtQi = market.spotBuyQi(bid, fevQiPerQuai,speculators, num, supply)
	                        self.quai += soldQuai
	                        self.qi += boughtQi
	                        remainder = bid + soldQuai
	                        if remainder > 0 and fevQiPerQuaiDiscounted > eqQiPrice:   
	                            #print("Convert5:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                            self.quai -= remainder
	                            self.convertedQi[-1] = supply.convertQuaiToQi(remainder)
	                            #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	            else:
	                if self.qi > 0 and len(market.buyQi) > 0:
	                    bid = self.bidAmt(self.qi)
	                    soldQi, boughtQuai = market.spotSellQi(bid, fevQiPerQuai, speculators, num, supply)
	                    self.qi += soldQi
	                    self.quai += boughtQuai
	                    remainder = bid + soldQi
	                    if remainder > 0:
	                        #print("Convert6:", "qi", self.qi, "quai", self.quai, "block", num, "remainder", remainder)
	                        self.qi -= remainder
	                        self.convertedQuai[-1] = supply.convertQiToQuai(remainder)
	                        #print("AfterConvert:", "qi", self.qi, "quai", self.quai)
	                
	
	        #if soldQi != 0 or soldQuai != 0:
	            #print("take:", "qi", self.qi, "quai", self.quai, "block", num, "id", self.id)
	
	        market.book(speculators,supply)
	        return self.qi - initQi, self.quai - initQuai
	
	    def make(self, deltaQi, deltaQuai, num, market, supply, speculators):
	        if self.qi + deltaQi < 0 or self.quai + deltaQuai < 0:
	            #print("ERROR: make: qi", deltaQi,"quai", deltaQuai, "num:", num, "qi", self.qi, "quai", self.quai, "id", self.id)
	            #market.book(speculators,supply)
	            return False
	        self.qi += deltaQi
	        self.quai += deltaQuai
	        #print("make:", self.qi, self.quai, num, self.id)
	        return True