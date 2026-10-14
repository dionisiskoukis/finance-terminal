# finance_commands.py
import yfinance as yf
import xfinance as xf
from ui_components import to_screen, display_screen, show_terminal_banner

# Global variables (used by almost every function)
parameter = ""
start_date = ""
end_date = ""

def help():
    to_screen("Available commands:")
    to_screen("get [ticker] [start_date] [end_date] - Get historical data for the specified ticker between the given dates")
    to_screen("getrt [ticker] - Get real-time price for the specified ticker")
    to_screen("goldinfo - Get the real time price of gold")
    to_screen("silverinfo - Get the real time price of silver")
    to_screen("copperinfo - Get the real time price of copper")
    to_screen("palladiuminfo - Get the real time price of palladium")
    to_screen("platinuminfo - Get the real time price of platinum")
    to_screen("afs [ticker] - Gives the annual financial statements of a stock")
    to_screen("qfs [ticker] - Gives the quarterly financial statements of a stock")
    to_screen("ticker_info [ticker] - Gives the company information of a stock")
    to_screen("pin [ticker] - Save the ticker and display its current company information")
    to_screen("unpin [ticker] - Remove the ticker from the pinned list")
    to_screen("news [ticker] - Get the latest news for the specified ticker")
    to_screen("major_holders [ticker] - Shows the major holders of the specified ticker")
    to_screen("inst_holders [ticker] - Shows the institutional holders of the specified stock")
    to_screen("apt [ticker] - Shows the analysts's price recomendations of the specified ticker")
    to_screen("rec [ticker] - Shows te recomendations of the specified ticker")
    to_screen("insider_transactions [ticker] - Shows the insider transactions of the specified ticker")
    to_screen("sustainability [ticker] - Shows the sustainability information of the specified ticker")
    to_screen("hca [ticker] - Shows the historical corporate actions of the specified ticker")
    to_screen("index_funds - Shows the current prices of major index funds")
    to_screen("clear - Clear the terminal screen")
    to_screen("licence - Display the license information")
    to_screen("exit - Exit the program")

def get():
    try:
        data = yf.download(parameter, start=start_date, end=end_date)
        to_screen(data.info())
        to_screen(data.head())
    except Exception as e:
        to_screen(f"Error, {parameter} is not a valid ticker symbol. Please try again")

def fetch_realtime_price(ticker):
    # This function was AI generated only for testing purposes
    stock = yf.Ticker(ticker)
    price = stock.info.get('regularMarketPrice')
    
    if price is None:
        raise ValueError(f"No price data found for {ticker}")
        
    return price

def getrt():
    """UI wrapper for the terminal"""
    try:
        price = fetch_realtime_price(parameter)
        to_screen(f"Current price of {parameter}: {price}")
    except ValueError:
        to_screen(f"Error: {parameter} is not a valid ticker symbol.")
    except Exception as e:
        to_screen(f"Network or API Error: {e}")

def annual_financial_statements():
    try:
        stock = yf.Ticker(parameter)
        income_stmt = stock.income_stmt
        if income_stmt is not None and not income_stmt.empty:
            to_screen(f"Income statements for {parameter}:")
            to_screen(income_stmt)
        else:
            to_screen(f"No income statements found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")
    try:
        balance_sheet = stock.balance_sheet
        stock = yf.Ticker(parameter)
        income_stmt = stock.balance_sheet
        if balance_sheet is not None and not balance_sheet.empty:
            to_screen(f"Balance sheet for {parameter}:")
            to_screen(income_stmt)
        else:
            to_screen(f"No balance sheet found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")
    try:
        cash_flow = stock.cashflow
        stock = yf.Ticker(parameter)
        cashflow = stock.cashflow
        if cashflow is not None and not cashflow.empty:
            to_screen(f"Cash flow for {parameter}:")
            to_screen(cashflow)
        else:
            to_screen(f"No cash flow found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def quarterly_financial_statements(): 
    import sys
    import subprocess
    import xfinance as xf
    try:
        import h2
    except ImportError:
        to_screen("Network fix: Installing missing 'h2' package. Please wait a moment...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx[http2]", "h2"])
            to_screen("Installation complete! Proceeding...")
        except Exception as e:
            to_screen(f"Failed to auto-install h2: {e}")
            return
    try:
        stock = xf.Ticker(parameter)
    except Exception as e:
        to_screen(f"Error initializing Ticker {parameter}. Details: {e}")
        return
    try:
        income_stmt_q = stock.quarterly_income_stmt 
        if income_stmt_q is not None and not income_stmt_q.empty:
            to_screen(f"Quarterly income statements for {parameter}:")
            to_screen(income_stmt_q)
        else:
            to_screen(f"No quarterly income statements found for {parameter}.")
    except Exception as e:
        to_screen(f"Error retrieving quarterly income statements for {parameter}. Details: {e}")
    try:
        balance_sheet_q = stock.quarterly_balance_sheet 
        if balance_sheet_q is not None and not balance_sheet_q.empty:
            to_screen(f"Quarterly balance sheet for {parameter}:")
            to_screen(balance_sheet_q)
        else:
            to_screen(f"No quarterly balance sheet found for {parameter}.")
    except Exception as e:
        to_screen(f"Error retrieving quarterly balance sheet for {parameter}. Details: {e}")
    try:
        cashflow_q = stock.quarterly_cashflow 
        if cashflow_q is not None and not cashflow_q.empty:
            to_screen(f"Quarterly cash flow for {parameter}:")
            to_screen(cashflow_q)
        else:
            to_screen(f"No quarterly cash flow found for {parameter}.")
    except Exception as e:
        to_screen(f"Error retrieving quarterly cash flow for {parameter}. Details: {e}")

def goldinfo():
    ticker = 'GC=F'
    stock = yf.Ticker(ticker)
    gold_price = stock.info['regularMarketPrice']
    to_screen(f"Current price of Gold: {gold_price}")

def silverinfo():
    ticker = 'SI=F'
    stock = yf.Ticker(ticker)
    silver_price = stock.info['regularMarketPrice']
    to_screen(f"Current price of Silver: {silver_price}")

def copperinfo():
    ticker = 'HG=F'
    stock = yf.Ticker(ticker)
    copper_price = stock.info['regularMarketPrice']
    to_screen(f"Current price of Copper: {copper_price}")

def palladiuminfo():
    ticker = 'PA=F'
    stock = yf.Ticker(ticker)
    palladium_price = stock.info['regularMarketPrice']
    to_screen(f"Current price of Palladium: {palladium_price}")

def platinuminfo():
    ticker = 'PL=F'
    stock = yf.Ticker(ticker)
    platinum_price = stock.info['regularMarketPrice']
    to_screen(f"Current price of Platinum: {platinum_price}")

def ticker_info():
    try:
        stock = yf.Ticker(parameter)
        info = stock.info
        pe_ratio = info.get('trailingPE', 'N/A')
        to_screen(f"Company: {info['longName']}")
        to_screen(f"Sector: {info['sector']}")
        to_screen(f"Industry: {info['industry']}")
        to_screen(f"Market Cap: {info['marketCap']}")
        to_screen(f"P/E Ratio: {pe_ratio}")
        if pe_ratio != 'N/A':
            if pe_ratio <= 10:
                to_screen("The company is either undervalued (a bargain) or in financial trouble.")
            elif pe_ratio <= 25:
                to_screen("That's the average cost for most established companies")
                to_screen("The company has stable, steady growth expectations.")
            elif pe_ratio > 25:
                to_screen("Investors expect massive future growth, or the stock is a bubble.")
        else:
            to_screen("P/E ratio is not available for this company.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def clear():
    display_screen.clear()
    show_terminal_banner()

def news():
    try:
        stock = yf.Ticker(parameter)
        news_items = stock.news
        if len(news_items) != 0:
            to_screen(f"News for {parameter}:")
            to_screen(news_items)
        else:
            to_screen(f"No news found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def dwnld():
    pass  # Placeholder for future implementation of a download function

def pin():
    stock = yf.Ticker(parameter)
    try:
        stock_info = stock.info
        long_name = stock_info.get('longName', 'N/A')
        sector = stock_info.get('sector', 'N/A')
        industry = stock_info.get('industry', 'N/A')
        market_cap = stock_info.get('marketCap', 'N/A')
        pe_ratio = stock_info.get('trailingPE', 'N/A')
        
        with open("pinned_stocks.txt", "a") as file:
            file.write(parameter + "\n")
            
        to_screen(f"Ticker {parameter} has been pinned.")
        to_screen(f"Company: {long_name}")
        to_screen(f"Sector: {sector}")
        to_screen(f"Industry: {industry}")
        to_screen(f"Market Cap: {market_cap}")
        to_screen(f"P/E Ratio: {pe_ratio}")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def unpin():
    try:
        with open("pinned_stocks.txt", "r") as file:
            pinned_tickers = file.read().splitlines()
        
        if parameter in pinned_tickers:
            pinned_tickers.remove(parameter)
            with open("pinned_stocks.txt", "w") as file:
                for ticker in pinned_tickers:
                    file.write(ticker + "\n")
            to_screen(f"Ticker {parameter} has been unpinned.")
        else:
            to_screen(f"Ticker {parameter} is not pinned.")
    except Exception as e:
        to_screen(f"Error: Could not unpin {parameter}. Please try again.")

def licence():
    to_screen("Finance Terminal v1.0")
    to_screen("MIT License")
    to_screen("")
    to_screen("Copyright (c) 2026 dionisis koukis")
    to_screen("Permission is hereby granted, free of charge, to any person obtaining a copy")
    to_screen("of this software and associated documentation files (the Software), to deal")
    to_screen("in the Software without restriction, including without limitation the rights")
    to_screen("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell")
    to_screen("copies of the Software, and to permit persons to whom the Software is")
    to_screen("furnished to do so, subject to the following conditions:")
    to_screen("")
    to_screen("The above copyright notice and this permission notice shall be included in all")
    to_screen("copies or substantial portions of the Software.")
    to_screen("")
    to_screen("THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR")
    to_screen("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
    to_screen("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
    to_screen("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER")
    to_screen("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,")
    to_screen("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE")
    to_screen("SOFTWARE.")

def options():
    try:
        stock = yf.Ticker(parameter)
        options = stock.options
        if options:
            to_screen(f"Expiry dates for {parameter}:")
            to_screen(options)
        else:
            to_screen(f"No options found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def major_holders():
    try:
        stock = yf.Ticker(parameter)
        major_holders = stock.major_holders
        if major_holders is not None and not major_holders.empty:
            to_screen(f"Major holders for {parameter}:")
            to_screen(major_holders)
        else:
            to_screen(f"No major holders information found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def institutional_holders():
    try:
        stock = yf.Ticker(parameter)
        institutional_holders = stock.institutional_holders
        if institutional_holders is not None:
            to_screen(f"Institutional holders for {parameter}:")
            to_screen(institutional_holders)
        else:
            to_screen(f"No institutional holders information found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def analysts_price_targets():
    try:
        stock = yf.Ticker(parameter)
        analysts_price_targets = stock.analyst_price_targets
        if analysts_price_targets is not None and not analysts_price_targets.empty:
            to_screen(f"Analysts price targets for {parameter}:")
            to_screen(analysts_price_targets)
        else:
            to_screen(f"No analysts price targets found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def recomendations():
    try:
        stock = yf.Ticker(parameter)
        recommendations = stock.recommendations
        if recommendations is not None and not recommendations.empty:
            to_screen(f"Recommendations for {parameter}:")
            to_screen(recommendations)
        else:
            to_screen(f"No recommendations found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def insider_transactions():
    try:
        stock = yf.Ticker(parameter)
        insider_transactions = stock.insider_transactions
        if insider_transactions is not None and not insider_transactions.empty:
            to_screen(f"Insider transactions for {parameter}:")
            to_screen(insider_transactions)
        else:
            to_screen(f"No insider transactions found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def sustainability():
    try:
        stock = yf.Ticker(parameter)
        sustainability = stock.sustainability
        if sustainability is not None and not sustainability.empty:
            to_screen(f"Sustainability information for {parameter}:")
            to_screen(sustainability)
        else:
            to_screen(f"No sustainability information found for {parameter}.")
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")

def index_funds():
    index_funds = ["^GSPC", "^DJI", "^IXIC", "^VIX", "^OEX", "^NYA", "^RUT", "^FTSE", "^N225", "^HSI", "^SSEC", "^BSESN", "^BVSP"]
    for i in index_funds:
        try:
            stock = yf.Ticker(i)
            price = stock.info['regularMarketPrice']
            to_screen(f"Current price of {i}: {price}")
        except Exception as e:
            to_screen(f"Error: {i} is not a valid ticker symbol. Please try again.")

def historical_corporate_actions():
    try:
        stock = yf.Ticker(parameter)
        dividents = stock.dividends
        if dividents is not None and not dividents.empty:
            to_screen(f"Dividends for {parameter}:")
            to_screen(dividents)
        else:
            to_screen(f"No dividents found for {parameter}.")
    except Exception as e:
            to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")
    try:
        stock = yf.Ticker(parameter)
        splits = stock.splits
        if splits is not None and not splits.empty:
            to_screen(f"Splits for {parameter}:")
            to_screen(splits)
        else:
            to_screen(f"No splits found for {parameter}.")
    except Exception as e:
            to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")
    try:
        stock = yf.Ticker(parameter)
        actions = stock.actions
        if actions is not None and not actions.empty:
            to_screen(f"Actions for {parameter}:")
            to_screen(actions)
        else:
            to_screen(f"No actions found for {parameter}.")
    except Exception as e:
            to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again.")
