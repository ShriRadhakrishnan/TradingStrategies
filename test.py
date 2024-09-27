import time
from config import *
from utils import *
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import ClosePositionRequest


trading_client = TradingClient(API_KEY, SECRET_KEY)
account = trading_client.get_account()
positions = trading_client.get_all_positions()

print(trading_client.get_open_position(positions[0].asset_id))
