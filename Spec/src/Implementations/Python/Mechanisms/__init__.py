from .Dummy import dummy_log_results_mechanism
from .MonetaryPolicy import (
    mint_qi_tokens_mechanism,
    mint_quai_token_mechanism,
    burn_qi_tokens_mechanism,
    burn_quai_tokens_mechanism,
)
from .Logs import (
    update_historical_converted_qi_mechanism,
    update_historical_converted_quai_mechanism,
)

mechanisms = {
    "DUMMY Log Results Mechanism": dummy_log_results_mechanism,
    "Mint Qi Tokens Mechanism": mint_qi_tokens_mechanism,
    "Mint Quai Tokens Mechanism": mint_quai_token_mechanism,
    "Burn Qi Tokens Mechanism": burn_qi_tokens_mechanism,
    "Burn Quai Tokens Mechanism": burn_quai_tokens_mechanism,
    "Update Historical Converted Qi Mechanism": update_historical_converted_qi_mechanism,
    "Update Historical Converted Quai Mechanism": update_historical_converted_quai_mechanism,
}
