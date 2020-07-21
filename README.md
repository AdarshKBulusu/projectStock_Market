# Stock Market Programs

### Python Packages Needed

1. robin_stocks
2. click
3. tulipy
4. os
5. time
6. alpaca_trade_api
7. time

**ROBIN_CALLS.py**

Group of functions to access Robin_Hood's unofficial API 

All functions are terminal commands as well. The functions are 

1. Quote - to get the current market price of one share of chosen share
2. Buy (default) - which buys one market share of a chosen stock.
You can also place a limit order and/or set the quantity of stock you would like to purchase. 
3. Sell (default) - whcih sells one of your owned market shares.
You cal also place the same limit option as well quantity

**RSI_BUY_SELL.py**

Includes code needed to buy and sell shares according to their RSI values 
This strategy typically makes small, but consistent, gains ;however,check your account restrictions to avoid being flagged as a Pattern Day Trade (PDT). 

Additionally, you must turn off 2-factor authentiction on your Robinhood account 
After adding your email and password to the login function, add your desired stocks and run through terminal or command line. 

Must be run through terminal because the ROBIN_CALLS.py is set to execute in a command line interface.

**SENTIMENT_MACD.py**

*Work in Progress*

Based off of the RSI_BUY_SELL.py attempts to use polarity score as a factor in determining wheter to purchase a stock. Additionally, works buy using the 
MACD indicator's (common techincal indicator) reversal line to place buy and sell orders. 

Must be run through terminal because it implements ROBIN_CALLS.py
Additionally,PDT rules apply
