"""
name: rsi_buy_sell.py
robin_calls.py extension class

Work in Progress Do Not Plug In and Use
"""

import robin_stocks as rh
import numpy as np
import tulipy as ti
import os
import alpaca_trade_api as tradeapi
import time
#import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment(ticker):
    sia = SentimentIntensityAnalyzer()
    passage = ""
    for i in range(len(rh.stocks.get_news(ticker))):
        passage += str(rh.stocks.get_news(ticker)[i].get(ticker))
    print("Sentiment Score: " + str(sia.polarity_scores(passage)['compound']))
    
            
def login():
    rh.login("email","password",store_session = True)
    
def main(ticker):
    login() #logs into the program
    if macd(ticker):
        print("I want to buy 1 stock of {} under the MACD ".format(ticker))
    if rsi(ticker):
        print("I want to buy 1 stock of {} under the RSI ".format(ticker))
    
    
    
       
    
def macd(ticker):
    alist = []
    dfh = rh.get_historicals(ticker,'day','regular')
    for term in dfh:
        alist.append(float(term['close_price']))
        
    data = np.array(alist)
    macd, macd_signal, macd_histogram = ti.macd(data,12,26,9)
    macd_list = macd_histogram
    index = len(macd_list)
    if(index > 2):
        if macd_list[index - 1] > macd_list[index - 2] and macd_list[index - 2] > macd_list[index - 3]:
            return True
        else:
            return False
    else:
        return False



def rsi(ticker):
    rsiPeriod = 14
    close = []
    dfh = rh.get_historicals(ticker,'day','regular') # list of dictionaries
    for key in dfh:
        close.append(float(key['close_price']))

    data = np.array(close)
    if(len(close) > rsiPeriod):
        rsi_list = list((ti.rsi(data,rsiPeriod)))
        #print("Ticker: "+ticker)
        #print("Latest RSI value: {}".format(rsi_list[len(rsi_list) - 1]))
        #print("")
        if rsi_list[len(rsi_list) - 1] <= 31:
            #os.system('python robin_calls.py buy 1 '+ticker)
            #got_it = True
            return True
        
        
        if rsi_list[len(rsi_list) - 1] >= 69:
            #os.system('python robin_calls.py sell 1 '+ticker)
            #got_it = False
            return True
    
    return False
            


if __name__ == "__main__":
    api = tradeapi.REST(key_id = 'fromAlpaca',secret_key = 'fromAlpacas',base_url = 'https://paper-api.alpaca.markets',api_version = 'v2')
    clock = api.get_clock() # seperate API to check when the market is open
    login()
    while clock.is_open:
        main()
        time.sleep(10)
    
    print("The market is closed")
    for val in rh.account.build_holdings():
        print("Ticker: {}".format(val))
        print("#:{}".format((rh.account.build_holdings()[val]['quantity'][0])))
    
    #main('GNUS')
    sentiment('F')

    #for i in range(len(rh.markets.get_top_movers('up'))):
    #    print(rh.markets.get_top_movers('down')[i].get('symbol'))
    #    print(sentiment(rh.markets.get_top_movers('down')[i].get('symbol')))
    
   
            









