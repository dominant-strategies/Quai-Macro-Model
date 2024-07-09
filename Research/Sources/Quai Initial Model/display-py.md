## Model Additions

## To Process
	
	def display(supply, initKQi):
	    #Print Results
	    plt.figure(figsize=(15,45))
	    plt.subplots_adjust(hspace=0.5,wspace=0.5)
	
	    panels = 21
	    # Difficulty Plot
	    plt.subplot(panels, 1, 1)
	    plt.plot([record["block"] for record in supply.history], [record["difficulty"] for record in supply.history], color="blue", label="Difficulty")
	    plt.plot([record["block"] for record in supply.history], [record["hashDiff"] for record in supply.history], color="orange", label="Hash Difficulty")
	    plt.yscale("log")
	    plt.title("Difficulty Over Block Number")
	    plt.ylabel("Difficulty")
	    plt.legend()
	
	    plt.subplot(panels, 1, 2)
	    plt.plot([record["block"] for record in supply.history], [record["quai"] for record in supply.history], color="red", label="Quai")
	    plt.title("Quai Over Block Number")
	    plt.ylabel("Quai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 3)
	    plt.plot([record["block"] for record in supply.history], [record["qi"] for record in supply.history], color="green", label="Qi")
	    plt.title("Qi Over Block Number")
	    plt.ylabel("Qi")
	    plt.legend()
	
	    plt.subplot(panels, 1, 4)
	    plt.plot([record["block"] for record in supply.history], [record["mined_token"] for record in supply.history], color="purple", label="Mined Token")
	    plt.title("Mined Token Over Block Number")
	    plt.ylabel("Mined Token")
	    plt.legend()
	
	    plt.subplot(panels, 1, 5)
	    plt.plot([record["block"] for record in supply.history], [record["mined_ratio"] for record in supply.history], color="orange", label="Mined Ratio")
	    plt.title("Mined Ratio Over Block Number")
	    plt.ylabel("Mined Ratio")
	    plt.legend()
	
	    plt.subplot(panels, 1, 6)
	    plt.plot([record["block"] for record in supply.history], [record["kqaui"] for record in supply.history], color="blue", label="KQuai")
	    plt.title("KQuai Over Block Number")
	    plt.ylabel("KQuai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 7)
	    plt.plot([record["block"] for record in supply.history], [record["quaiPrice"] for record in supply.history], color="red", label="Quai Price")
	    plt.plot([record["block"] for record in supply.history], [record["quaiRewardVal"] for record in supply.history], color="green", label="Quai Reward Price")
	    plt.yscale("log")
	    plt.title("Quai Price Over Block Number")
	    plt.ylabel("Quai Price")
	    plt.legend()
	
	    plt.subplot(panels, 1, 8)
	    plt.plot([record["block"] for record in supply.history], [record["qiPrice"] for record in supply.history], color="green", label="Qi Price")
	    plt.title("Qi Price Over Block Number")
	    plt.ylabel("Qi Price")
	    plt.legend()
	
	    plt.subplot(panels, 1, 9)
	    plt.plot([record["block"] for record in supply.history], [record["miners"] for record in supply.history], color="purple", label="Miners")
	    plt.title("Miners Over Block Number")
	    plt.ylabel("Miners")
	    plt.legend()
	
	    plt.subplot(panels, 1, 10)
	    plt.plot([record["block"] for record in supply.history], [record["deltaQi"] for record in supply.history], color="green", label="Traded Qi")
	    plt.title("Traded Qi Over Block Number")
	    plt.ylabel("Traded Qi")
	    plt.legend()
	
	    plt.subplot(panels, 1, 11)
	    plt.plot([record["block"] for record in supply.history], [record["deltaQuai"] for record in supply.history], color="purple", label="Traded Quai")
	    plt.title("Traded Quai Over Block Number")
	    plt.ylabel("Traded Quai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 12)
	    plt.plot([record["block"] for record in supply.history], [record["convertedQi"] for record in supply.history], color="blue", label="Converted Qi")
	    plt.title("Converted Qi Over Block Number")
	    plt.ylabel("Converted Qi")
	    plt.legend()
	
	    plt.subplot(panels, 1, 13)
	    plt.plot([record["block"] for record in supply.history], [record["convertedQuai"] for record in supply.history], color="red", label="Converted Quai")
	    plt.yscale("log")
	    plt.title("Converted Quai Over Block Number")
	    plt.ylabel("Converted Quai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 14)
	    plt.plot([record["block"] for record in supply.history], [record["marketFEV"] for record in supply.history], color="green", label="marketFEV")
	    plt.title("Market FEV Over Block Number")
	    plt.ylabel("Market FEV")
	    plt.legend()
	
	    plt.subplot(panels, 1, 15)
	    plt.plot([record["block"] for record in supply.history], [record["quaiHash"] for record in supply.history], color="purple", label="Quai Hash")
	    plt.title("Quai Hash Over Block Number")
	    plt.ylabel("Quai Hash")
	    plt.legend()
	
	    plt.subplot(panels, 1, 16)
	    plt.plot([record["block"] for record in supply.history], [record["qiHash"] for record in supply.history], color="blue", label="Qi Hash")
	    plt.title("Qi Hash Over Block Number")
	    plt.ylabel("Qi Hash")
	    plt.legend()
	
	    plt.subplot(panels, 1, 17)
	    plt.plot([record["block"] for record in supply.history], [record["hashRatio"] for record in supply.history], color="red", label="Hash Ratio")
	    plt.plot([record["block"] for record in supply.history], [record["mined_ratio"] for record in supply.history], color="orange", label="Mined Ratio")
	    #plt.yscale("log")
	    plt.title("Hash Ratio Over Block Number")
	    plt.ylabel("Hash Ratio")
	    plt.legend()
	
	    plt.subplot(panels, 1, 18)
	    plt.plot([record["block"] for record in supply.history], [record["mined_ratio"] for record in supply.history], color="green", label="mined_ratio")
	    plt.title("Mined Ratio Over Block Number")
	    plt.ylabel("Mined Ratio")
	    plt.legend()
	
	    plt.subplot(panels, 1, 19)
	    plt.plot([record["block"] for record in supply.history], [record["quaiHashSum"] for record in supply.history], color="purple", label="Quai Hash Sum")
	    plt.title("Quai Hash Sum Over Block Number")
	    plt.ylabel("Quai Hash Sum")
	    plt.legend()
	
	    plt.subplot(panels, 1, 20)
	    plt.plot([record["block"] for record in supply.history], [record["qiHashSum"] for record in supply.history], color="blue", label="Qi Hash Sum")
	    plt.title("Qi Hash Sum Over Block Number")
	    plt.ylabel("Qi Hash Sum")
	    plt.legend()
	
	    plt.subplot(panels, 1, 21)
	    plt.plot([record["block"] for record in supply.history], [record["error"] for record in supply.history], color="red", label="Error")
	    plt.title("Error Over Block Number")
	    plt.ylabel("Error")
	    plt.legend()
	
	
	
	def plot_book(market):
	    # Extracting bid amount and bid price for buyQi and sellQi
	    if len(market.buyQi) > 0:
	        buyQi_bid_amounts, buyQi_bid_prices = zip(*[(item["cumSum"], item["priceQiPerQuai"]) for item in market.buyQi])
	        plt.plot(buyQi_bid_prices, buyQi_bid_amounts, color='blue', label='Buy Qi')
	        plt.fill_between(buyQi_bid_prices, 0, buyQi_bid_amounts, color='blue', alpha=0.3)
	
	    if len(market.sellQi) > 0:
	        sellQi_bid_amounts, sellQi_bid_prices = zip(*[(item["cumSum"], item["priceQiPerQuai"]) for item in market.sellQi])
	        plt.plot(sellQi_bid_prices, sellQi_bid_amounts, color='red', label='Sell Qi')
	        plt.fill_between(sellQi_bid_prices, 0, sellQi_bid_amounts, color='red', alpha=0.3)
	
	    # Adding labels and title
	    plt.xlabel('Bid Price')
	    plt.ylabel('Bid Amount')
	    plt.title('Bid Price vs Bid Amount for BuyQi and SellQi')
	    plt.legend()
	
	    # Display the plot
	    plt.show()

## Code

	import matplotlib.pyplot as plt
	
	def display(supply, initKQi):
	    #Print Results
	    plt.figure(figsize=(15,45))
	    plt.subplots_adjust(hspace=0.5,wspace=0.5)
	
	    panels = 21
	    # Difficulty Plot
	    plt.subplot(panels, 1, 1)
	    plt.plot([record["block"] for record in supply.history], [record["difficulty"] for record in supply.history], color="blue", label="Difficulty")
	    plt.plot([record["block"] for record in supply.history], [record["hashDiff"] for record in supply.history], color="orange", label="Hash Difficulty")
	    plt.yscale("log")
	    plt.title("Difficulty Over Block Number")
	    plt.ylabel("Difficulty")
	    plt.legend()
	
	    plt.subplot(panels, 1, 2)
	    plt.plot([record["block"] for record in supply.history], [record["quai"] for record in supply.history], color="red", label="Quai")
	    plt.title("Quai Over Block Number")
	    plt.ylabel("Quai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 3)
	    plt.plot([record["block"] for record in supply.history], [record["qi"] for record in supply.history], color="green", label="Qi")
	    plt.title("Qi Over Block Number")
	    plt.ylabel("Qi")
	    plt.legend()
	
	    plt.subplot(panels, 1, 4)
	    plt.plot([record["block"] for record in supply.history], [record["mined_token"] for record in supply.history], color="purple", label="Mined Token")
	    plt.title("Mined Token Over Block Number")
	    plt.ylabel("Mined Token")
	    plt.legend()
	
	    plt.subplot(panels, 1, 5)
	    plt.plot([record["block"] for record in supply.history], [record["mined_ratio"] for record in supply.history], color="orange", label="Mined Ratio")
	    plt.title("Mined Ratio Over Block Number")
	    plt.ylabel("Mined Ratio")
	    plt.legend()
	
	    plt.subplot(panels, 1, 6)
	    plt.plot([record["block"] for record in supply.history], [record["kqaui"] for record in supply.history], color="blue", label="KQuai")
	    plt.title("KQuai Over Block Number")
	    plt.ylabel("KQuai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 7)
	    plt.plot([record["block"] for record in supply.history], [record["quaiPrice"] for record in supply.history], color="red", label="Quai Price")
	    plt.plot([record["block"] for record in supply.history], [record["quaiRewardVal"] for record in supply.history], color="green", label="Quai Reward Price")
	    plt.yscale("log")
	    plt.title("Quai Price Over Block Number")
	    plt.ylabel("Quai Price")
	    plt.legend()
	
	    plt.subplot(panels, 1, 8)
	    plt.plot([record["block"] for record in supply.history], [record["qiPrice"] for record in supply.history], color="green", label="Qi Price")
	    plt.title("Qi Price Over Block Number")
	    plt.ylabel("Qi Price")
	    plt.legend()
	
	    plt.subplot(panels, 1, 9)
	    plt.plot([record["block"] for record in supply.history], [record["miners"] for record in supply.history], color="purple", label="Miners")
	    plt.title("Miners Over Block Number")
	    plt.ylabel("Miners")
	    plt.legend()
	
	    plt.subplot(panels, 1, 10)
	    plt.plot([record["block"] for record in supply.history], [record["deltaQi"] for record in supply.history], color="green", label="Traded Qi")
	    plt.title("Traded Qi Over Block Number")
	    plt.ylabel("Traded Qi")
	    plt.legend()
	
	    plt.subplot(panels, 1, 11)
	    plt.plot([record["block"] for record in supply.history], [record["deltaQuai"] for record in supply.history], color="purple", label="Traded Quai")
	    plt.title("Traded Quai Over Block Number")
	    plt.ylabel("Traded Quai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 12)
	    plt.plot([record["block"] for record in supply.history], [record["convertedQi"] for record in supply.history], color="blue", label="Converted Qi")
	    plt.title("Converted Qi Over Block Number")
	    plt.ylabel("Converted Qi")
	    plt.legend()
	
	    plt.subplot(panels, 1, 13)
	    plt.plot([record["block"] for record in supply.history], [record["convertedQuai"] for record in supply.history], color="red", label="Converted Quai")
	    plt.yscale("log")
	    plt.title("Converted Quai Over Block Number")
	    plt.ylabel("Converted Quai")
	    plt.legend()
	
	    plt.subplot(panels, 1, 14)
	    plt.plot([record["block"] for record in supply.history], [record["marketFEV"] for record in supply.history], color="green", label="marketFEV")
	    plt.title("Market FEV Over Block Number")
	    plt.ylabel("Market FEV")
	    plt.legend()
	
	    plt.subplot(panels, 1, 15)
	    plt.plot([record["block"] for record in supply.history], [record["quaiHash"] for record in supply.history], color="purple", label="Quai Hash")
	    plt.title("Quai Hash Over Block Number")
	    plt.ylabel("Quai Hash")
	    plt.legend()
	
	    plt.subplot(panels, 1, 16)
	    plt.plot([record["block"] for record in supply.history], [record["qiHash"] for record in supply.history], color="blue", label="Qi Hash")
	    plt.title("Qi Hash Over Block Number")
	    plt.ylabel("Qi Hash")
	    plt.legend()
	
	    plt.subplot(panels, 1, 17)
	    plt.plot([record["block"] for record in supply.history], [record["hashRatio"] for record in supply.history], color="red", label="Hash Ratio")
	    plt.plot([record["block"] for record in supply.history], [record["mined_ratio"] for record in supply.history], color="orange", label="Mined Ratio")
	    #plt.yscale("log")
	    plt.title("Hash Ratio Over Block Number")
	    plt.ylabel("Hash Ratio")
	    plt.legend()
	
	    plt.subplot(panels, 1, 18)
	    plt.plot([record["block"] for record in supply.history], [record["mined_ratio"] for record in supply.history], color="green", label="mined_ratio")
	    plt.title("Mined Ratio Over Block Number")
	    plt.ylabel("Mined Ratio")
	    plt.legend()
	
	    plt.subplot(panels, 1, 19)
	    plt.plot([record["block"] for record in supply.history], [record["quaiHashSum"] for record in supply.history], color="purple", label="Quai Hash Sum")
	    plt.title("Quai Hash Sum Over Block Number")
	    plt.ylabel("Quai Hash Sum")
	    plt.legend()
	
	    plt.subplot(panels, 1, 20)
	    plt.plot([record["block"] for record in supply.history], [record["qiHashSum"] for record in supply.history], color="blue", label="Qi Hash Sum")
	    plt.title("Qi Hash Sum Over Block Number")
	    plt.ylabel("Qi Hash Sum")
	    plt.legend()
	
	    plt.subplot(panels, 1, 21)
	    plt.plot([record["block"] for record in supply.history], [record["error"] for record in supply.history], color="red", label="Error")
	    plt.title("Error Over Block Number")
	    plt.ylabel("Error")
	    plt.legend()
	
	
	
	def plot_book(market):
	    # Extracting bid amount and bid price for buyQi and sellQi
	    if len(market.buyQi) > 0:
	        buyQi_bid_amounts, buyQi_bid_prices = zip(*[(item["cumSum"], item["priceQiPerQuai"]) for item in market.buyQi])
	        plt.plot(buyQi_bid_prices, buyQi_bid_amounts, color='blue', label='Buy Qi')
	        plt.fill_between(buyQi_bid_prices, 0, buyQi_bid_amounts, color='blue', alpha=0.3)
	
	    if len(market.sellQi) > 0:
	        sellQi_bid_amounts, sellQi_bid_prices = zip(*[(item["cumSum"], item["priceQiPerQuai"]) for item in market.sellQi])
	        plt.plot(sellQi_bid_prices, sellQi_bid_amounts, color='red', label='Sell Qi')
	        plt.fill_between(sellQi_bid_prices, 0, sellQi_bid_amounts, color='red', alpha=0.3)
	
	    # Adding labels and title
	    plt.xlabel('Bid Price')
	    plt.ylabel('Bid Amount')
	    plt.title('Bid Price vs Bid Amount for BuyQi and SellQi')
	    plt.legend()
	
	    # Display the plot
	    plt.show()