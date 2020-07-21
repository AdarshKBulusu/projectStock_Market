"""
name: robin_call.py
Robinhood_Connection_and_Buying_Selling
"""

import robin_stocks as rh 
import click

@click.group() 
def main():
    rh.login("email","password",store_session = True)
    click.echo(click.style("Robinhood Connection Established",fg = "blue",bold = True))
    #helper.rsi_buy()
    

@main.command(help = 'Gets a stock quote for one or more symbols')
@click.argument('symbols', nargs = -1)
def quote(symbols):
    quotes = rh.get_quotes(symbols)
    
    for quote in quotes:
        print("{} | ${} ".format(quote['symbol'],quote['ask_price']))


@main.command(help = 'Buying shares')
@click.argument('quantity',type = click.INT)
@click.argument('symbol',type = click.STRING)
@click.option('--limit',type = click.FLOAT)

def buy(quantity, symbol, limit):
    if limit is not None:#limit order 
        click.echo(click.style("Buying {} of {} at ${}".format(quantity,symbol,limit), fg = "green", bold = True))
        result = rh.order_buy_limit(symbol,quantity,limit)
        
    else:#market order
        click.echo(click.style("Buying {} of {} at market value".format(quantity,symbol), fg = "green", bold = True))
        result = rh.order_buy_market(symbol,quantity)
    
    print(result)

@main.command(help = 'Selling shares')
@click.argument('quantity',type = click.INT)
@click.argument('symbol',type = click.STRING)
@click.option('--limit',type = click.FLOAT)

def sell(quantity,symbol,limit):
    if limit is not None:
         click.echo(click.style("Selling {} of {} at ${}".format(quantity,symbol,limit), fg = "green", bold = True))
         result = rh.order_sell_limit(symbol,quantity,limit)
         
    else:
        click.echo(click.style("Selling {} of {} at market value".format(quantity,symbol), fg = "green", bold = True))
        result = rh.order_sell_market(symbol,quantity)
    
    
    
    if 'detail' in result:
        red_msg = click.style("ERROR",fg="red",blink = True,bold = True)
        print(red_msg)
    else:
        click.style(str(result),fg = "green",bold = True)
    

if __name__  == "__main__":
    main()
