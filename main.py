from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from config import *


trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

account = trading_client.get_account()

spy = trading_client.get_asset('SPY')

print(spy)
