## Model Additions

- [[Quai Price Movement Wiring]]
- [[Qi Price Movement Wiring]]
- [[MSML Scaffold/State/Global State-Current Hash Difference]]
- [[Calculate Hash Difference Policy]]


## To Process


	class Market:
	    def __init__(self,initKQi,initDiff,numMiners,supply):
	        self.minerDiff = initDiff/numMiners
	        self.hashDiff = initDiff
	        self.growth_bias = 0.00056
	        self.growth_rate = 0.01
	        self.quaiPriceVal = 1/initKQi
	        self.qiPriceVal = 1/initKQi
	        self.quaiPerQiVal = 9
	        self.m = 1000
	        self.buyQi = []
	        self.sellQi = []
	        self.currentFEVval = 0.05
	    
	    def update(self,supply,mining):
	        self.calcHashDiff(mining,supply)
	        self.quaiPrice(supply)
	        self.qiPrice(supply)
	        self.quaiPerQi()
	        self.currentFEV(supply)
	
	    def calcHashDiff(self,mining, supply):
	        growth = 0.005
	        # Assuming self.blockNum is the current block number
	        try:
	            # Before calling calculate_moving_averages
	            # print(f"Type of supply.blockNum: {type(supply.blockNum)}")  # Just for debugging, remove or comment out later
	            # assert isinstance(supply.blockNum, int), "supply.blockNum must be an integer"
	
	            current_ma, prior_ma = self.calculate_moving_averages(supply.history, supply.blockNum, window_size=50, step_back=30)
	            # Comparison or further logic goes here
	            growth = (prior_ma / current_ma)
	            #print("growth:", growth,"block:", supply.blockNum, "current_ma:", current_ma, "prior_ma:", prior_ma)
	        except ValueError as e:
	            growth = 0.005
	
	        
	        self.minerDiff = (self.minerDiff*49 + self.minerDiff * growth)/50 #mining hash is growing proportional to the average long term quai price
	        self.hashDiff = self.minerDiff * len(mining)
	
	    def calculate_moving_averages(self,history, current_block, window_size=50, step_back=30):
	        """
	        Calculate moving averages for quaiPriceVal over a specified window size.
	        :param history: List of dictionaries containing block data.
	        :param current_block: The current block number for which to calculate the moving average.
	        :param window_size: The size of the window for the moving average.
	        :param step_back: The number of blocks to step back for comparison.
	        :return: The current moving average and the moving average from step_back blocks prior.
	        """
	        # Inside Market.calculate_moving_averages, right before the problematic line
	        # print(f"current_block: {current_block}, type: {type(current_block)}")
	        # print(f"window_size: {window_size}, type: {type(window_size)}")
	        # print(f"step_back: {step_back}, type: {type(step_back)}")
	
	        # Ensure there's enough data to calculate both moving averages
	        if current_block < window_size + step_back:
	            raise ValueError("Not enough data to calculate the moving averages.")
	        
	        # Calculate current moving average
	        current_window = [entry["quaiPrice"] for entry in history[current_block-window_size+1:current_block+1]]
	        current_moving_average = sum(current_window) / window_size
	        
	        # Calculate moving average from step_back blocks prior
	        prior_window = [entry["quaiPrice"] for entry in history[current_block-window_size-step_back+1:current_block-step_back+1]]
	        prior_moving_average = sum(prior_window) / window_size
	        
	        return current_moving_average, prior_moving_average

	
	    def marketCorrectQuaiPrice(self, supply):
	        if len(self.buyQi) > 0 and len(self.sellQi) > 0:
	            self.quaiPriceVal = 1/((self.buyQi[0]["priceQiPerQuai"] + self.sellQi[0]["priceQiPerQuai"])/2) * self.qiPriceVal
	            self.quaiPerQi()
	            #print("market corrected quai price", "quai/hash:", self.quaiPriceVal, "qi/hash:", self.qiPriceVal, "quai/qi:", self.quaiPerQiVal)
	        elif len(self.buyQi) > 0:
	            self.quaiPriceVal = 1/(self.buyQi[0]["priceQiPerQuai"]) * self.qiPriceVal
	            self.quaiPerQi()
	            #print("market corrected quai price", "quai/hash:", self.quaiPriceVal, "qi/hash:", self.qiPriceVal, "quai/qi:", self.quaiPerQiVal)
	        elif len(self.sellQi) > 0:
	            self.quaiPriceVal = 1/(self.sellQi[0]["priceQiPerQuai"]) * self.qiPriceVal
	            self.quaiPerQi()
	            #print("market corrected quai price", "quai/hash:", self.quaiPriceVal, "qi/hash:", self.qiPriceVal, "quai/qi:", self.quaiPerQiVal)
	
	    def qiPrice(self,supply): #qi price per hash
	        self.qiPriceVal = (1 + (np.random.randn() * 0.005))/supply.kqi #1% volatility in qi price
	
	        
	    def quaiPerQi(self): #quai per qi
	        self.quaiPerQiVal = self.quaiPriceVal/self.qiPriceVal
	    
	    def spotBuyQi(self, quantity, price ,speculators, num, supply): #price is qi per quai
	
	        quantityQi = 0
	        quantityQuai = 0
	        popped = []
	        #output quantity of qi at a input price
	        self.sellQi.sort(key=lambda x: x["priceQiPerQuai"])
	        
	        for sellQi in self.sellQi:
	            quaiAmount = sellQi["qiAmount"] / sellQi["priceQiPerQuai"]
	            qiAmount = sellQi["qiAmount"] 
	            id = sellQi["id"]
	            makerId =speculators[id].id
	            if sellQi["priceQiPerQuai"] < price:
	                break
	            else:
	                #print("sellQi Initial:",self.sellQi)
	                #print("price:",price,"quantity:",quantity)
	                if quaiAmount < quantity:
	                    quantity -= quaiAmount
	                    quantityQuai -= quaiAmount
	                    quantityQi += qiAmount
	                    #print("make input whole: qi", -qiAmount,"quai", quaiAmount, "num:", num, "id:", id)
	                    #print("speculator:", "id", makerId, "qi:", speculators[id].qi, "quai",speculators[id].quai)
	                    speculators[makerId].make(-qiAmount,quaiAmount, num, self, supply, speculators) 
	                    self.book(speculators,supply)
	                else:
	                    remainderQi = quantity * sellQi["priceQiPerQuai"]
	                    sellQi["qiAmount"] -= remainderQi
	                    quantityQuai -= quantity 
	                    quantityQi += remainderQi
	                    #print("make input partial: qi", -remainderQi,"quai", quantity, "num:", num, "id:", id)
	                    #print("speculator:", "id", speculators[id].id, "qi:", speculators[id].qi, "quai:",speculators[id].quai)
	                    speculators[makerId].make(-remainderQi, quantity, num, self, supply, speculators) 
	                    quantity = 0
	                    break
	        
	        self.book(speculators,supply)
	
	        #print("sellQi Final:",self.sellQi)
	        #print ("quantityQi:",quantityQi,"quantityQuai:",quantityQuai)
	        return quantityQuai, quantityQi
	    
	    def spotSellQi(self, quantity, price ,speculators, num, supply): #price quai per qi
	
	        quantityQuai = 0
	        quantityQi = 0
	        popped = []
	        #output quantity of qi at a input price
	        self.buyQi.sort(key=lambda x: x["priceQiPerQuai"],reverse=True)
	        for buyQi in self.buyQi:
	            quaiAmount = buyQi["quaiAmount"]
	            qiAmount = buyQi["quaiAmount"] * buyQi["priceQiPerQuai"]
	            id = buyQi["id"]
	            makerId =speculators[id].id
	
	            if buyQi["priceQiPerQuai"] > price:
	                break
	            else:
	                #print("buyQi Initial:",self.buyQi)
	                #print("price:",price,"quantity:",quantity) 
	                if qiAmount < quantity:
	                    quantity -= qiAmount
	                    quantityQi -= qiAmount
	                    quantityQuai += quaiAmount
	                    #print("make: qi", qiAmount,"quai",-quaiAmount , "num:", num, "id:", id)
	                    #print("speculator:", "id", makerId, "qi:", speculators[id].qi, "quai",speculators[id].quai)
	                    speculators[makerId].make(qiAmount, -quaiAmount, num, self, supply, speculators) 
	                    self.book(speculators,supply)
	                else:
	                    remainderQuai = quantity / buyQi["priceQiPerQuai"]
	                    buyQi["quaiAmount"] -= remainderQuai
	                    quantityQi -= quantity
	                    quantityQuai += remainderQuai
	                    #print("make: qi", -quantity,"quai", remainderQuai, "num:", num, "id:", id)
	                    #print("speculator:", "id", speculators[id].id, "qi:", speculators[id].qi, "quai",speculators[id].quai)
	                    speculators[makerId].make(quantity, -remainderQuai,  num, self, supply, speculators) 
	                    quantity = 0
	                    break
	
	        self.book(speculators,supply)
	        
	        #print("buyQi Final:",self.buyQi)
	        #print ("quantityQi:",quantityQi,"quantityQuai:",quantityQuai)
	        return quantityQi, quantityQuai
	    
	    def book(self, speculators, supply):
	        #flush the old book
	        self.buyQi = []
	        self.sellQi = []
	        #for each speculator, run speculate, return a price and quantity ie bid
	        for speculator in speculators:
	            if speculator.type == 0:
	                bidType, bidAmount, bidPrice, id = speculator.bid(self,supply)
	                if bidType == 0:
	                    self.buyQi.append({"quaiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                elif bidType == 1:
	                    self.sellQi.append({"qiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                else:
	                    continue
	            elif speculator.type == 1:
	                for i in range(20):
	                    bidType, bidAmount, bidPrice, id = speculator.liquid(self,supply, i)
	                    if bidType == 0:
	                        self.buyQi.append({"quaiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                    elif bidType == 1:
	                        self.sellQi.append({"qiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                    else:
	                        continue
	        
	        self.buyQi.sort(key=lambda x: x["priceQiPerQuai"],reverse=True)
	        self.sellQi.sort(key=lambda x: x["priceQiPerQuai"])    
	
	        cumulative_sum = 0
	        for buyQi in self.buyQi:
	            # Calculate cumulative amounts
	            cumulative_sum += buyQi["quaiAmount"]
	            buyQi["cumSum"] = cumulative_sum
	
	        cumulative_sum = 0
	        for sellQi in self.sellQi:
	            # Calculate cumulative amounts
	            cumulative_sum += sellQi["qiAmount"]
	            sellQi["cumSum"] = cumulative_sum

## Code

	import numpy as np
	import random as random
	import matplotlib.pyplot as plt
	
	class Market:
	    def __init__(self,initKQi,initDiff,numMiners,supply):
	        self.minerDiff = initDiff/numMiners
	        self.hashDiff = initDiff
	        self.growth_bias = 0.00056
	        self.growth_rate = 0.01
	        self.quaiPriceVal = 1/initKQi
	        self.qiPriceVal = 1/initKQi
	        self.quaiPerQiVal = 9
	        self.m = 1000
	        self.buyQi = []
	        self.sellQi = []
	        self.currentFEVval = 0.05
	    
	    def update(self,supply,mining):
	        self.calcHashDiff(mining,supply)
	        self.quaiPrice(supply)
	        self.qiPrice(supply)
	        self.quaiPerQi()
	        self.currentFEV(supply)
	
	    def calcHashDiff(self,mining, supply):
	        growth = 0.005
	        # Assuming self.blockNum is the current block number
	        try:
	            # Before calling calculate_moving_averages
	            # print(f"Type of supply.blockNum: {type(supply.blockNum)}")  # Just for debugging, remove or comment out later
	            # assert isinstance(supply.blockNum, int), "supply.blockNum must be an integer"
	
	            current_ma, prior_ma = self.calculate_moving_averages(supply.history, supply.blockNum, window_size=50, step_back=30)
	            # Comparison or further logic goes here
	            growth = (prior_ma / current_ma)
	            #print("growth:", growth,"block:", supply.blockNum, "current_ma:", current_ma, "prior_ma:", prior_ma)
	        except ValueError as e:
	            growth = 0.005
	
	        
	        self.minerDiff = (self.minerDiff*49 + self.minerDiff * growth)/50 #mining hash is growing proportional to the average long term quai price
	        self.hashDiff = self.minerDiff * len(mining)
	
	    def calculate_moving_averages(self,history, current_block, window_size=50, step_back=30):
	        """
	        Calculate moving averages for quaiPriceVal over a specified window size.
	        :param history: List of dictionaries containing block data.
	        :param current_block: The current block number for which to calculate the moving average.
	        :param window_size: The size of the window for the moving average.
	        :param step_back: The number of blocks to step back for comparison.
	        :return: The current moving average and the moving average from step_back blocks prior.
	        """
	        # Inside Market.calculate_moving_averages, right before the problematic line
	        # print(f"current_block: {current_block}, type: {type(current_block)}")
	        # print(f"window_size: {window_size}, type: {type(window_size)}")
	        # print(f"step_back: {step_back}, type: {type(step_back)}")
	
	        # Ensure there's enough data to calculate both moving averages
	        if current_block < window_size + step_back:
	            raise ValueError("Not enough data to calculate the moving averages.")
	        
	        # Calculate current moving average
	        current_window = [entry["quaiPrice"] for entry in history[current_block-window_size+1:current_block+1]]
	        current_moving_average = sum(current_window) / window_size
	        
	        # Calculate moving average from step_back blocks prior
	        prior_window = [entry["quaiPrice"] for entry in history[current_block-window_size-step_back+1:current_block-step_back+1]]
	        prior_moving_average = sum(prior_window) / window_size
	        
	        return current_moving_average, prior_moving_average
	
	    def quaiPrice(self,supply): #qaui price per hash
	        self.quaiPriceVal = self.quaiPriceVal * (np.random.randn() * self.growth_rate + (1 - self.growth_bias))
	        # if supply.blockNum % 5000 == 0:
	        #     self.quaiPriceVal = self.quaiPriceVal * .9
	
	    def marketCorrectQuaiPrice(self, supply):
	        if len(self.buyQi) > 0 and len(self.sellQi) > 0:
	            self.quaiPriceVal = 1/((self.buyQi[0]["priceQiPerQuai"] + self.sellQi[0]["priceQiPerQuai"])/2) * self.qiPriceVal
	            self.quaiPerQi()
	            #print("market corrected quai price", "quai/hash:", self.quaiPriceVal, "qi/hash:", self.qiPriceVal, "quai/qi:", self.quaiPerQiVal)
	        elif len(self.buyQi) > 0:
	            self.quaiPriceVal = 1/(self.buyQi[0]["priceQiPerQuai"]) * self.qiPriceVal
	            self.quaiPerQi()
	            #print("market corrected quai price", "quai/hash:", self.quaiPriceVal, "qi/hash:", self.qiPriceVal, "quai/qi:", self.quaiPerQiVal)
	        elif len(self.sellQi) > 0:
	            self.quaiPriceVal = 1/(self.sellQi[0]["priceQiPerQuai"]) * self.qiPriceVal
	            self.quaiPerQi()
	            #print("market corrected quai price", "quai/hash:", self.quaiPriceVal, "qi/hash:", self.qiPriceVal, "quai/qi:", self.quaiPerQiVal)
	
	        
	    def quaiPerQi(self): #quai per qi
	        self.quaiPerQiVal = self.quaiPriceVal/self.qiPriceVal
	
	    def currentFEV(self, supply):
	        # create the sign for a triangle wave
	        if (supply.blockNum  // 1000)%2 == 1:
	            sign = 1
	        else:
	            sign = -1
	
	        # create the triangle wave
	        self.currentFEVval += sign * 10/(1000 * 100) 
	        #print("fev:", fev)
	        return self.currentFEVval
	    
	    def spotBuyQi(self, quantity, price ,speculators, num, supply): #price is qi per quai
	
	        quantityQi = 0
	        quantityQuai = 0
	        popped = []
	        #output quantity of qi at a input price
	        self.sellQi.sort(key=lambda x: x["priceQiPerQuai"])
	        
	        for sellQi in self.sellQi:
	            quaiAmount = sellQi["qiAmount"] / sellQi["priceQiPerQuai"]
	            qiAmount = sellQi["qiAmount"] 
	            id = sellQi["id"]
	            makerId =speculators[id].id
	            if sellQi["priceQiPerQuai"] < price:
	                break
	            else:
	                #print("sellQi Initial:",self.sellQi)
	                #print("price:",price,"quantity:",quantity)
	                if quaiAmount < quantity:
	                    quantity -= quaiAmount
	                    quantityQuai -= quaiAmount
	                    quantityQi += qiAmount
	                    #print("make input whole: qi", -qiAmount,"quai", quaiAmount, "num:", num, "id:", id)
	                    #print("speculator:", "id", makerId, "qi:", speculators[id].qi, "quai",speculators[id].quai)
	                    speculators[makerId].make(-qiAmount,quaiAmount, num, self, supply, speculators) 
	                    self.book(speculators,supply)
	                else:
	                    remainderQi = quantity * sellQi["priceQiPerQuai"]
	                    sellQi["qiAmount"] -= remainderQi
	                    quantityQuai -= quantity 
	                    quantityQi += remainderQi
	                    #print("make input partial: qi", -remainderQi,"quai", quantity, "num:", num, "id:", id)
	                    #print("speculator:", "id", speculators[id].id, "qi:", speculators[id].qi, "quai:",speculators[id].quai)
	                    speculators[makerId].make(-remainderQi, quantity, num, self, supply, speculators) 
	                    quantity = 0
	                    break
	        
	        self.book(speculators,supply)
	
	        #print("sellQi Final:",self.sellQi)
	        #print ("quantityQi:",quantityQi,"quantityQuai:",quantityQuai)
	        return quantityQuai, quantityQi
	    
	    def spotSellQi(self, quantity, price ,speculators, num, supply): #price quai per qi
	
	        quantityQuai = 0
	        quantityQi = 0
	        popped = []
	        #output quantity of qi at a input price
	        self.buyQi.sort(key=lambda x: x["priceQiPerQuai"],reverse=True)
	        for buyQi in self.buyQi:
	            quaiAmount = buyQi["quaiAmount"]
	            qiAmount = buyQi["quaiAmount"] * buyQi["priceQiPerQuai"]
	            id = buyQi["id"]
	            makerId =speculators[id].id
	
	            if buyQi["priceQiPerQuai"] > price:
	                break
	            else:
	                #print("buyQi Initial:",self.buyQi)
	                #print("price:",price,"quantity:",quantity) 
	                if qiAmount < quantity:
	                    quantity -= qiAmount
	                    quantityQi -= qiAmount
	                    quantityQuai += quaiAmount
	                    #print("make: qi", qiAmount,"quai",-quaiAmount , "num:", num, "id:", id)
	                    #print("speculator:", "id", makerId, "qi:", speculators[id].qi, "quai",speculators[id].quai)
	                    speculators[makerId].make(qiAmount, -quaiAmount, num, self, supply, speculators) 
	                    self.book(speculators,supply)
	                else:
	                    remainderQuai = quantity / buyQi["priceQiPerQuai"]
	                    buyQi["quaiAmount"] -= remainderQuai
	                    quantityQi -= quantity
	                    quantityQuai += remainderQuai
	                    #print("make: qi", -quantity,"quai", remainderQuai, "num:", num, "id:", id)
	                    #print("speculator:", "id", speculators[id].id, "qi:", speculators[id].qi, "quai",speculators[id].quai)
	                    speculators[makerId].make(quantity, -remainderQuai,  num, self, supply, speculators) 
	                    quantity = 0
	                    break
	
	        self.book(speculators,supply)
	        
	        #print("buyQi Final:",self.buyQi)
	        #print ("quantityQi:",quantityQi,"quantityQuai:",quantityQuai)
	        return quantityQi, quantityQuai
	    
	    def book(self, speculators, supply):
	        #flush the old book
	        self.buyQi = []
	        self.sellQi = []
	        #for each speculator, run speculate, return a price and quantity ie bid
	        for speculator in speculators:
	            if speculator.type == 0:
	                bidType, bidAmount, bidPrice, id = speculator.bid(self,supply)
	                if bidType == 0:
	                    self.buyQi.append({"quaiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                elif bidType == 1:
	                    self.sellQi.append({"qiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                else:
	                    continue
	            elif speculator.type == 1:
	                for i in range(20):
	                    bidType, bidAmount, bidPrice, id = speculator.liquid(self,supply, i)
	                    if bidType == 0:
	                        self.buyQi.append({"quaiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                    elif bidType == 1:
	                        self.sellQi.append({"qiAmount": bidAmount, "priceQiPerQuai": bidPrice, "id": id, "cumSum": 0})
	                    else:
	                        continue
	        
	        self.buyQi.sort(key=lambda x: x["priceQiPerQuai"],reverse=True)
	        self.sellQi.sort(key=lambda x: x["priceQiPerQuai"])    
	
	        cumulative_sum = 0
	        for buyQi in self.buyQi:
	            # Calculate cumulative amounts
	            cumulative_sum += buyQi["quaiAmount"]
	            buyQi["cumSum"] = cumulative_sum
	
	        cumulative_sum = 0
	        for sellQi in self.sellQi:
	            # Calculate cumulative amounts
	            cumulative_sum += sellQi["qiAmount"]
	            sellQi["cumSum"] = cumulative_sum