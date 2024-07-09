## Model Additions

- [[Global State]]
	- [[Global State-Current Qi Block Reward]]
	- [[Global State-Current Quai Block Reward]]
	- [[Global State-Simulation History Log]]
	- [[Global State - Historical Mined Ratio]]
	- [[Global State - Block Number]]
	- [[Global State - Historical Qi Hash]]
	- [[Global State - Historical Quai Hash]]
- [[Update Simulation History Log Wiring]]
- [[Treasury State]]
	- [[Treasury State - Qi Holdings]]
	- [[Treasury State - Quai Holdings]]
- [[Increment Block Number Mechanism]]
- [[Update Historical Mined Ratio Mechanism]]
- [[Update Historical Qi Hash Mechanism]]
- [[Update Historical Quai Hash Mechanism]]

## To Process
	
	class TokenSupply:
	    def __init__(self,initDiff, initQuai,initKQuai,initQi,initKQi,duration,amtMin):
	        self.initDiff = initDiff
	        self.diff = initDiff
	        self.intErr = deque(maxlen=100)
	        self.duration = duration
	        self.convertedQi = deque(maxlen=duration)
	        self.convertedQuai = deque(maxlen=duration)
	        self.amtMin = amtMin
	        self.blockNum = 0
	        self.qiHash = deque(maxlen=duration)
	        self.quaiHash = deque(maxlen=duration)
	        self.hashRatio = 0
	        self.err = 0
	        self.diffPeriod = 10
	

	        self.qiHash.append(1)
	        self.quaiHash.append(1)
	        self.mined_ratio.append(0)
	        self.ratio = 0
	
	    def propose(self, market):
	        initQuai = self.quai
	        initQi = self.qi
	        #calculate new price params
	        self.diff = self.difficulty(market)
	        self.qiLocked = 0
	        self.quaiLocked = 0
	        self.qiRewardVal = self.qiReward()
	        self.quaiRewardVal = self.quaiReward()
	        self.quai += self.convertedQuai[-self.duration] if len(self.convertedQuai) >= self.duration else 0
	        self.qi += self.convertedQi[-self.duration] if len(self.convertedQi) >= self.duration else 0  
	        self.convertedQi.append(0)
	        self.convertedQuai.append(0)
	        self.mined_ratio.append(0)
	        self.qiHash.append(0)
	        self.quaiHash.append(0)
	        # if initQi - self.qi != 0 or initQuai - self.quai != 0:
	        #     print("propose:", "block", self.blockNum, "qiDiff", self.qi - initQi, "quaiDiff", self.quai - initQuai)
	    

	
	    def integratedHashRatio(self):
	        intHashErr = 0
	        for i in range(1, self.duration):
	                if len(self.history) > i + self.duration:
	                    quaiSum = sum(item["convertedQuai"] for item in self.history[-(i + self.duration):-i])
	                    qiSum = sum(item["convertedQi"] for item in self.history[-(i + self.duration):-i])
	
	                    quaiHash = self.quaiToHash(quaiSum)
	                    qiHash = self.qiToHash(qiSum)
	                    if (quaiHash + qiHash) != 0:
	                        intHashErr += (quaiHash - qiHash) / (quaiHash + qiHash)
	        return intHashErr
	    
	    def derivativeHashRatio(self):
	        deltaErr = 0
	        for i in range(1, 20):
	            if len(self.history) > i + 40:
	                quaiSumNew = sum(item["convertedQuai"] for item in self.history[-i:])
	                qiSumNew = sum(item["convertedQi"] for item in self.history[-i:])
	                
	                quaiSumOld = sum(item["convertedQuai"] for item in self.history[-(i + 20):-i])
	    
	    def proportionalGain(self, x):
	        return 1 + 4 * x ** 2
	
	    def difficulty(self,market):
	        self.diff = (self.diff * (self.diffPeriod - 1) + market.hashDiff)/self.diffPeriod
	        return self.diff
## Code
	import numpy as np
	import random as random
	import matplotlib.pyplot as plt
	from collections import deque
	
	class TokenSupply:
	    def __init__(self,initDiff, initQuai,initKQuai,initQi,initKQi,duration,amtMin):
	        self.quai = initQuai
	        self.qi = initQi
	        self.kqi = initKQi
	        self.kquai = initKQuai
	        self.history = []
	        self.initDiff = initDiff
	        self.diff = initDiff
	        self.mined_ratio = deque(maxlen=100)
	        self.intErr = deque(maxlen=100)
	        self.qiLocked = 0
	        self.quaiLocked = 0
	        self.duration = duration
	        self.qiRewardVal = 1 
	        self.quaiRewardVal = 1
	        self.convertedQi = deque(maxlen=duration)
	        self.convertedQuai = deque(maxlen=duration)
	        self.amtMin = amtMin
	        self.blockNum = 0
	        self.qiHash = deque(maxlen=duration)
	        self.quaiHash = deque(maxlen=duration)
	        self.hashRatio = 0
	        self.err = 0
	        self.diffPeriod = 10
	
	        self.P = 0.01
	        self.I = self.P*0#.05#.02
	        self.D = self.P*0.2
	        self.qiHash.append(1)
	        self.quaiHash.append(1)
	        self.mined_ratio.append(0)
	        self.ratio = 0
	
	    def propose(self, market):
	        initQuai = self.quai
	        initQi = self.qi
	        #calculate new price params
	        self.diff = self.difficulty(market)
	        self.qiLocked = 0
	        self.quaiLocked = 0
	        self.qiRewardVal = self.qiReward()
	        self.quaiRewardVal = self.quaiReward()
	        self.quai += self.convertedQuai[-self.duration] if len(self.convertedQuai) >= self.duration else 0
	        self.qi += self.convertedQi[-self.duration] if len(self.convertedQi) >= self.duration else 0  
	        self.convertedQi.append(0)
	        self.convertedQuai.append(0)
	        self.mined_ratio.append(0)
	        self.qiHash.append(0)
	        self.quaiHash.append(0)
	        # if initQi - self.qi != 0 or initQuai - self.quai != 0:
	        #     print("propose:", "block", self.blockNum, "qiDiff", self.qi - initQi, "quaiDiff", self.quai - initQuai)
	
	    def update(self, miner, market,mining,blockDeltaQi,blockDeltaQuai):
	        #print("update_init:", "quai", self.quai, "qi", self.qi, "block", self.blockNum)
	        #update supply numbers
	        self.quai += miner.quai
	        self.qi += miner.qi
	        self.blockNum += 1
	        if miner.quai != 0:
	            mined_token = 1
	            self.mined_ratio[-1] = 1
	        else:
	            mined_token = 0
	
	
	        #update the hash numbers
	        #print("quaiHash:", self.quaiHash[-1], "qiHash:", self.qiHash[-1], "quai:", self.quai, "qi:", self.qi, "block:", self.blockNum)
	        self.qiHash[-1] += self.qiToHash(miner.qi)
	        self.quaiHash[-1] += self.quaiToHash(miner.quai)
	
	        #print("update_end:", "quai", self.quai, "qi", self.qi, "block", self.blockNum)
	        #record history
	        self.history.append({
	            "block": self.blockNum,
	            "mined_token": mined_token,
	            "difficulty": self.diff,
	            "quai": self.quai,
	            "qi": self.qi,
	            "hashDiff": market.hashDiff,
	            "mined_ratio": self.ratio,
	            "kqaui": self.kquai,
	            "quaiPrice": market.quaiPriceVal,
	            "qiPrice": market.qiPriceVal,
	            "quaiPerQi": market.quaiPerQiVal,
	            "miners": mining,
	            "qiLocked": self.qiLocked,
	            "quaiLocked": self.quaiLocked,
	            "deltaQi": blockDeltaQi,
	            "deltaQuai": blockDeltaQuai,
	            "tradedQuai": blockDeltaQuai + self.history[-1]["tradedQuai"] if len(self.history) > 0 else blockDeltaQuai,
	            "convertedQi": sum(self.convertedQi),
	            "convertedQuai": sum(self.convertedQuai),
	            "marketFEV": market.currentFEVval,
	            "quaiHash": self.quaiHash[-1],
	            "qiHash": self.qiHash[-1],
	            "hashRatio": self.hashRatio,
	            "quaiHashSum": sum(self.quaiHash),
	            "qiHashSum": sum(self.qiHash),
	            "error": self.err,
	            "quaiRewardVal": self.quaiRewardVal/self.diff,
	            "qiRewardVal": self.qiRewardVal/self.diff,
	        })
	
	    def qiToHash(self, qiAmount):
	        if qiAmount <= 0:
	            return 0
	        return qiAmount*self.kqi
	    
	    def quaiToHash(self, quaiAmount):
	        if quaiAmount <= 0:
	            return 0
	        return self.qiRewardVal/self.quaiRewardVal * quaiAmount * self.kqi
	        #return 2**(2**(self.kquai) * quaiAmount)
	    
	    def qiReward(self):
	        self.qiRewardVal = self.diff/self.kqi
	        return self.qiRewardVal
	    
	    def linearController(self):
	        ratio = sum(self.mined_ratio)/len(self.mined_ratio)
	        self.ratio = ratio
	        P = 0.00000005
	        I = P*0.0001
	        D = P*0#.05
	
	        # Assuming self.mined_ratio is a deque
	        # Convert the relevant portions of the deque to lists for slicing
	        last_20_elements = list(self.mined_ratio)[-20:] if len(self.mined_ratio) > 20 else []
	        last_40_to_20_elements = list(self.mined_ratio)[-40:-20] if len(self.mined_ratio) > 40 else []
	
	        # Now you can subtract them if they are numbers or perform the intended operation
	        # Make sure to handle the case where last_40_to_20_elements is an empty list
	        deltaErr = sum(last_20_elements)/20 - sum(last_40_to_20_elements)/20 if last_40_to_20_elements else 0
	
	        #print("linearController:", "block", self.blockNum, "ratio", ratio, "kquai", self.kquai)
	        self.kquai -= self.kquai * (self.P * (0.5 - ratio) + sum(self.mined_ratio)*I + deltaErr*D)
	
	    def hashController(self):
	        ratio = sum(self.mined_ratio)/len(self.mined_ratio) * 2 - 1
	        self.ratio = ratio
	        P = 0.0001
	        I = P*0#.0001
	        D = P*0#.02
	
	        self.hashRatio = (self.quaiToHash(sum(self.quaiHash)) - self.qiToHash(sum(self.qiHash)))/(self.quaiToHash(sum(self.quaiHash)) + self.qiToHash(sum(self.qiHash)))#(self.duration * self.diff)# * (sum(self.quaiHash) + sum(self.qiHash))/(80000*100)
	
	        self.kquai += self.kquai * (np.log2(self.diff)/np.log2(self.initDiff) * P * self.proportionalGain(self.hashRatio) * self.hashRatio)# + self.integratedHashRatio()*I)
	
	    def integratedHashRatio(self):
	        intHashErr = 0
	        for i in range(1, self.duration):
	                if len(self.history) > i + self.duration:
	                    quaiSum = sum(item["convertedQuai"] for item in self.history[-(i + self.duration):-i])
	                    qiSum = sum(item["convertedQi"] for item in self.history[-(i + self.duration):-i])
	
	                    quaiHash = self.quaiToHash(quaiSum)
	                    qiHash = self.qiToHash(qiSum)
	                    if (quaiHash + qiHash) != 0:
	                        intHashErr += (quaiHash - qiHash) / (quaiHash + qiHash)
	        return intHashErr
	    
	    def derivativeHashRatio(self):
	        deltaErr = 0
	        for i in range(1, 20):
	            if len(self.history) > i + 40:
	                quaiSumNew = sum(item["convertedQuai"] for item in self.history[-i:])
	                qiSumNew = sum(item["convertedQi"] for item in self.history[-i:])
	                
	                quaiSumOld = sum(item["convertedQuai"] for item in self.history[-(i + 20):-i])
	    def quaiReward(self):
	               
	        self.hashController()
	        #self.linearController()
	        self.quaiRewardVal = 2 ** -(1 + self.kquai) * np.log2(self.diff)
	        return self.quaiRewardVal
	    
	    def proportionalGain(self, x):
	        return 1 + 4 * x ** 2
	
	    def difficulty(self,market):
	        self.diff = (self.diff * (self.diffPeriod - 1) + market.hashDiff)/self.diffPeriod
	        return self.diff
	    
	    def convertQiToQuai(self, qiAmount):
	        if qiAmount < self.amtMin or qiAmount > self.qi:
	            return 0
	        self.qi -= qiAmount
	        quaiAmt = self.quaiRewardVal/self.qiRewardVal * qiAmount
	        self.convertedQuai[-1] += quaiAmt
	        self.quaiHash[-1] += quaiAmt
	        #print("convertQiToQuai:", "qi", self.qi, "quai", self.quai, "block", self.blockNum, "qiAmount", qiAmount, "quaiAmount", quaiAmt)
	        return quaiAmt
	    
	    def convertQuaiToQi(self, quaiAmount):
	        if quaiAmount < self.amtMin or quaiAmount > self.quai:
	            return 0
	        self.quai -= quaiAmount
	        qiAmt = self.qiRewardVal/self.quaiRewardVal * quaiAmount
	        self.convertedQi[-1] += qiAmt
	        self.qiHash[-1] += qiAmt
	        #print("convertQuaiToQi:", "qi", self.qi, "quai", self.quai, "block", self.blockNum, "qiAmount", qiAmt, "quaiAmount", quaiAmount)
	        return qiAmt
	    
	    def qiPriceVal(self): #Do we need this function?
	        return 1/self.kqi