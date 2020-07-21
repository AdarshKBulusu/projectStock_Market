"""
name: rsi_buy_sell.py
robin_calls.py extension class


to avoid being flagged as a Pattern Day Trader by Robinhood read the regulations before using this program
Additionally, set your own take-profit / stop-loss model
"""

import robin_stocks as rh
import numpy as np
import tulipy as ti
import os
import alpaca_trade_api as tradeapi
import time


rsiPeriod = 14

def main():
    rh.login("email","password",store_session = True)  #turn on 2-factor auth
    print("+++++++++++++++++++++++++++++++++++++")
    rsi_buy('ACB') #example of a couple of ticker symbols
    rsi_buy('CLF')
    rsi_buy('CCL')
    print("+++++++++++++++++++++++++++++++++++++")
    

def rsi_buy(ticker):
    my_list = rh.account.build_holdings()
    if my_list.get(ticker) == None :
        got_it =  False
        close = []
        dfh = rh.get_historicals(ticker,'day','regular') # list of dictionaries # gets the daily candlesticks
        for key in dfh:
            close.append(float(key['close_price']))
    
        data = np.array(close)
        if(len(close) > rsiPeriod):
            rsi_list = list(ti.rsi(data,rsiPeriod))
            print("Latest RSI value: {}".format(rsi_list[len(rsi_list) - 1]))
            print("")
            if rsi_list[len(rsi_list) - 1] <= 31 and not got_it: # sell the stock less than 32
                os.system('python robin_calls.py buy 1 '+ticker) #using the robin_calls module's terminal command from click group
                got_it = True
                
                
                if rsi_list[len(rsi_list) - 1] >= 69 and got_it: # buy the stock greater than 69
                os.system('python robin_calls.py sell 1 '+ticker)
                got_it = False
                
    else:
        close = []
        dfh = rh.get_historicals(ticker,'day','regular') # list of dictionaries
        for key in dfh:
            close.append(float(key['close_price']))
    
        data = np.array(close)
        rsi_list = list((ti.rsi(data,rsiPeriod)))
        print("Ticker: "+ticker)
        print("Latest RSI value: {}".format(rsi_list[len(rsi_list) - 1]))
        print("")
        print("Number of shares: " + my_list.get(ticker).get('quantity'))
        print("")
            

if __name__ == "__main__":
    api = tradeapi.REST(key_id = 'fromAlpacaAPI',secret_key = 'fromAlpacaAPI',base_url = 'https://paper-api.alpaca.markets',api_version = 'v2')
    clock = api.get_clock() # seperate API to check when the market is open
    
    rh.login("email","password",store_session = True)
    rh.cancel_all_stock_orders() #cancels all the orders that may have been remaining from the previous day 
    print("==================================")
    while clock.is_open:
        main()
        time.sleep(20)
    
    for val in rh.account.build_holdings():
        print("Ticker: {}".format(val))
        print("#:{}".format((rh.account.build_holdings()[val]['quantity'][0])))
    """
        gives the general update on what shares you own if the market is not open
    """
        
    
   
            
        
            
            
    
    
    
    











