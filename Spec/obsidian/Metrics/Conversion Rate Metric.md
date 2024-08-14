Description: The ratio for converting for converting Qi to Quai.

The conversion rate $C^i$ is defined as the implied _spot rate_ from the proposals, i.e.
$$
  C^i := \frac{\partial R^i_{\text{Quai}}}{\partial R^i_{\text{Qi}}},
$$
and where
$$
  \frac{\partial R^i_{\text{Quai}}}{\partial R^i_{\text{Qi}}} = \left ( \frac{ k^i_{\text{Quai}} k^i_{\text{Qi}}   }{\ln(2) H^i} \right )= \left ( \frac{R^i_{\text{Quai}}}{R^i_{\text{Qi}}} \right ) \left ( \frac{1}{\ln \left ( H^i \right )} \right ).
$$

Type: [[Ratio Type]]

Symbol: None

## Logic
$$\left ( \frac{R^i_{\text{Quai}}}{R^i_{\text{Qi}}} \right ) \left ( \frac{1}{\ln \left ( H^i \right )} \right )$$

## Parameters Used

## Variables Used
1. [[Global State]].[[Global State-Block Difficulty|Block Difficulty]]

## Domain Spaces
## Metrics Used
1. [[Hash to Qi Metric]]
2. [[Hash to Quai Metric]]
