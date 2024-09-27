from config import *
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key')

account = trading_client.get_account()