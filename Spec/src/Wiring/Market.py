market_wiring = []

market_wiring.append(
    {
        "name": "Price Movements Wiring",
        "components": ["Placeholder"],
        "description": "The wiring for movements on the price of Qi and Quai",
        "constraints": [],
        "type": "Stack",
    }
)

market_wiring.append(
    {
        "name": "Conversions Wiring",
        "components": ["Conversions Boundary Action"],
        "description": """While the [[Mining Payment Policy|election to receive block rewards in Quai or Qi is reserved for miners]], the ability to [[Conversions Wiring|convert Qi and Quai tokens is embedded natively in the protocol]], and is available to any [[Network Participant]] to utilize at any time. The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].

For example, if the current Quai block reward is 1 and the current Qi block reward is 2, any [[Network Participant]] would be able to [[Burn Qi Tokens Mechanism|burn Qi tokens]] to [[Mint Quai Tokens Mechanism|mint new Quai tokens]] at a rate of 2:1.

This mechanism allows for greater responsiveness in the [[Qi Supply Metric|supply of Qi]], allowing all [[Network Participant|network participants]], not just [[Miner|miners]], to participate in the ongoing [[Trade Tokens Wiring|arbitrage]] between [[Qi Demand]] and [[Qi Supply Metric|Qi supply]].""",
        "constraints": [],
        "type": "Stack",
    },
)
