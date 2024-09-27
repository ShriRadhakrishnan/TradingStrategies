from config import *
from utils import *
from alpaca.trading.client import TradingClient



trading_client = TradingClient(API_KEY, SECRET_KEY)

account = trading_client.get_account()
positions = trading_client.get_all_positions()

#SOFT CAP OF 10% LOSS
SOFT_CAP = .1

#HARD CAP OF 15% LOSS
HARD_CAP = .15

#Price stop loss list
STOP_PRICE =[]


"""
Create a trailing stop loss
10% Loss from the highest value that has been seen for a sufficient amount of time, 15% max 

Keep tracking current price and every X time steps refresh price and accordingly update Stop Loss Value



"""

# if not positions:
#     exit(0)

for index, position in enumerate(positions):
    price = float(position.avg_entry_price)*100

    STOP_PRICE.append((price*(1-SOFT_CAP), price*(1-HARD_CAP)))





while positions:
    #GOES THROUUGH EVERY POSITION
    for index, position in enumerate(positions):




#write_positions('Text Information/positions.txt', positions, write_type='w')
#write_account('Text Information/account_info.txt', account, write_type='w')

