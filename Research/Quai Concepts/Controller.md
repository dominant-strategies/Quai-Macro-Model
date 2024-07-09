## I/O

- Input should be [[Controller Observability Stateful Metric]]
- Output should be setting $k_{quai}$, maybe setting $k_{qi}$
	- To be confirmed
## Requirements

- The controller should be robust over 6-9 orders of magnitude for things like supply
- If the aggregate flows are balanced than the [[controller]] is working

## Considerations
- If there is a potential for the [[Controller]] to be changing in the future, it should be projected out to ensure that users understand this may happen in the future (instead of it happening ad hoc)
- There should be a [[Schelling Point]] that is approached through [[Trade Tokens Wiring|arbitrage]]
## Design Questions

- What are we [[Stability Metrics|stabilizing]] and over what horizons?
- What is the desired [[Controller Equilibrium|equilibrium]]?

## Interventions Available

This is currently in as a question for the client and more clarity will be gleaned soon
### Quai - Qi Exchange Rate

### Quai Reward Scaler

- This is possibly not correct, but it looks like in the old code the reward value was proportional to the base2 log of difficulty times $2^{-(1+kquai)}$ where kquai was set by the controller

## TBD Spec Updates

- Errors can be tracked and added to the system but holding off on it until we get more clarity on controller shape
- Hash ratio and ratio as in the supply.py file can be added in as needed for tracking

## Old Code Implementations of Controllers

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

## Old Code Utility Functions

	    def proportionalGain(self, x):
	        return 1 + 4 * x ** 2



	    def derivativeHashRatio(self):
	        deltaErr = 0
	        for i in range(1, 20):
	            if len(self.history) > i + 40:
	                quaiSumNew = sum(item["convertedQuai"] for item in self.history[-i:])
	                qiSumNew = sum(item["convertedQi"] for item in self.history[-i:])
	                
	                quaiSumOld = sum(item["convertedQuai"] for item in self.history[-(i + 20):-i])


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