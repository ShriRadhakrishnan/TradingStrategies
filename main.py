from config import *
from utils import *
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import ClosePositionRequest



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


#ASSUME: ISN"T VERY VOLATILE
#INITIALIZING STOP LOSSES
for index, position in enumerate(positions):
    price = float(position.current_price)*100

    STOP_PRICE.append(price*(1-SOFT_CAP))


#Recalculate stop losses

def stop_loss():
    for index, position in enumerate(positions):

        current_price = float(position.current_price)*100
        print("CURRENT PRICE: ", current_price)

        print("STOP PRICE: ", STOP_PRICE[index])
        if current_price <= STOP_PRICE[index]:
            print("CLOSING POSITION")
            trading_client.close_position(position.symbol, ClosePositionRequest(percentage='100'))
            STOP_PRICE.pop(index)
            positions.pop(index)

        STOP_PRICE[index] = max((current_price) * (1-SOFT_CAP), STOP_PRICE[index])





#write_positions('Text Information/positions.txt', positions, write_type='w')
#write_account('Text Information/account_info.txt', account, write_type='w')

