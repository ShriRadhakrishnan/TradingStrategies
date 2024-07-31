from alpaca.data.live import StockDataStream, OptionDataStream, CryptoDataStream
from alpaca.data.requests import CryptoLatestQuoteRequest, StockLatestQuoteRequest, OptionLatestQuoteRequest
from config import *

stock_data_stream = StockDataStream(API_KEY, SECRET_KEY)

async def data_handler(data):
    print(data)

stock_data_stream.subscribe_quotes(data_handler, 'SPY')
stock_data_stream.run()