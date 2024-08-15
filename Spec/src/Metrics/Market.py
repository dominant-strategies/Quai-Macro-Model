metrics_market = []


metrics_market.append(
    {
        "type": "Ratio Type",
        "name": "Current Block Reward Ratio Metric",
        "description": r"""$$\frac{R_{Quai}}{R_{Qi}}$$""",
        "variables_used": [["Global State", "Block Difficulty"]],
        "parameters_used": [],
        "metrics_used": [
            "Hash to Qi Metric",
            "Hash to Quai Metric",
        ],
        "domain": [],
        "logic": r"$$\frac{R_{Quai}}{R_{Qi}}$$",
        "symbol": None,
    }
)

metrics_market.append(
    {
        "type": "Ratio Type",
        "name": "Conversion Rate Metric",
        "description": r"""The ratio for converting for converting Qi to Quai.

The conversion rate $C^i$ is defined as the implied _spot rate_ from the proposals, i.e.
$$
  C^i := \frac{\partial R^i_{\text{Quai}}}{\partial R^i_{\text{Qi}}},
$$
and where
$$
  \frac{\partial R^i_{\text{Quai}}}{\partial R^i_{\text{Qi}}} = \left ( \frac{ k^i_{\text{Quai}} k^i_{\text{Qi}}   }{\ln(2) H^i} \right )= \left ( \frac{R^i_{\text{Quai}}}{R^i_{\text{Qi}}} \right ) \left ( \frac{1}{\ln \left ( H^i \right )} \right ).
$$""",
        "variables_used": [
            ["Global State", "Block Difficulty"],
            ["Global State", "K Quai"],
            ["Global State", "K Qi"],
        ],
        "parameters_used": [],
        "metrics_used": [
            "Hash to Qi Metric",
            "Hash to Quai Metric",
        ],
        "domain": [],
        "logic": r"$$\left ( \frac{R^i_{\text{Quai}}}{R^i_{\text{Qi}}} \right ) \left ( \frac{1}{\ln \left ( H^i \right )} \right )$$",
        "symbol": None,
    }
)
