from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient, OptionHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest, StockLatestQuoteRequest, OptionLatestQuoteRequest
from config import *



# no keys required.
crypto_client = CryptoHistoricalDataClient()
# keys required
stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
option_client = OptionHistoricalDataClient(API_KEY, SECRET_KEY)

latest_quote_request = StockLatestQuoteRequest(symbol_or_symbols='SPY')

latest_quote = stock_client.get_stock_latest_quote(latest_quote_request)
print(latest_quote)