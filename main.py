#IMPORTS
import yfinance as yf
import xfinance as xf
import logging
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QLineEdit

logging.getLogger('yfinance').setLevel(logging.CRITICAL)


# ==========================================
# 1. UI SETUP (The visible terminal)
# ==========================================
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Finance Terminal")
window.resize(800, 500)
window.setStyleSheet("background-color: black; color: #00FF00; font-family: Consolas;")

layout = QVBoxLayout(window)
layout.setContentsMargins(5, 5, 5, 5)

display_screen = QPlainTextEdit()
display_screen.setReadOnly(True)
display_screen.setStyleSheet("border: none;")
layout.addWidget(display_screen)

typing_bar = QLineEdit()
typing_bar.setStyleSheet("border: none;")
layout.addWidget(typing_bar)

# Helper function to push text to the GUI instead of the hidden background console
def to_screen(text):
    display_screen.appendPlainText(str(text))

# ==========================================
# 2. YOUR LOGIC ZONE
# ==========================================
# This function runs every time you press Enter
def command_processing():
    # Make these module-level so other handlers can read them
    global user_input, number_of_words, command, parameter, start_date, end_date
    # Grab the text and clear the bar
    user_input = typing_bar.text().strip()
    typing_bar.clear()

    if user_input == "":
        return

    number_of_words = len(user_input.split())
    to_screen(f"> {user_input}")

    # number of words determines how we split the input
    if number_of_words == 1:
        one_word_command()
    elif number_of_words == 2:
        two_word_command()
    elif number_of_words == 4:
        four_word_command()
    else:
        command = ""

    # command dispatch
    if command == "help":
        help()
        to_screen("")
    elif command == "get":
        get()
    elif command == "getrt":
        getrt()
    elif command == "exit":
        to_screen("Exiting the program.")
        app.quit()
    elif command == "balance_sheet":
        balance_sheet()
    elif command == "financials":
        financials()
    elif command == "ticker_info":
        ticker_info()
    elif command == "goldinfo":
        goldinfo()
    elif command == "silverinfo":
        silverinfo()
    elif command == "copperinfo":
        copperinfo()
    elif command == "palladiuminfo":
        palladiuminfo()
    elif command == "platinuminfo":
        platinuminfo()
    elif command == "news":
        news()
    elif command == "clear":
        clear()

    else:
        to_screen("Invalid command. Type 'help' to see the list of available commands.")




def one_word_command():
    global command
    command = user_input
    
def two_word_command():
    global command, parameter
    command_split = user_input.split() #splits the variable into a list of strings
    command, parameter = command_split[0], command_split[1] #assigns the splitted strings to variables
    parameter.capitalize()

def four_word_command():
    global command, parameter, start_date, end_date
    command_split = user_input.split() #splits the variable into a list of strings
    command, parameter ,start_date, end_date = command_split[0], command_split[1], command_split[2], command_split[3] #assigns the splitted strings to variables
    parameter.capitalize()
def help():
    to_screen("Available commands:")
    to_screen("get [ticker] [start_date] [end_date] - Get historical data for the specified ticker between the given dates")
    to_screen("getrt [ticker] - Get real-time price for the specified ticker")
    to_screen("goldinfo - Get the real time price of gold")
    to_screen("silverinfo - Get the real time price of silver")
    to_screen("copperinfo - Get the real time price of copper")
    to_screen("palladiuminfo - Get the real time price of palladium")
    to_screen("platinuminfo - Get the real time price of platinum")
    to_screen("balance_sheet [ticker] - Gives the balance sheet of a stock")
    to_screen("financials [ticker] - Gives the financials of a stock")
    to_screen("ticker_info [ticker] - Gives the company information of a stock")
    to_screen("exit - Exit the program")

def get():
    try:
        data = yf.download(parameter, start=start_date, end=end_date)
        to_screen(data.info())
        to_screen(data.head())
    except Exception as e:
        to_screen(f"Error, {parameter} is not a valid ticker symbol. Please try again")
def getrt():
    try:
        stock = yf.Ticker(parameter)
        price = stock.info['regularMarketPrice']
            
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol.")
            
    else:
        to_screen(f"Current price of {parameter}: {price}")

def balance_sheet():
    try:
        stock = yf.Ticker(parameter)
        balance_sheet = stock.balance_sheet
        to_screen(balance_sheet)
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again")

def financials():
    try:
        stock = yf.Ticker(parameter)
        financials = stock.financials
        to_screen(financials)
    except Exception as e:
        to_screen(f"Error: {parameter} is not a valid ticker symbol. Please try again")
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
    # Generic if/elif chain is handled inside `command_processing()` via the GUI
def clear():
    display_screen.clear()
    to_screen("Finance Terminal v1.0")
    to_screen("If you need help, type 'help' and press Enter to see the available commands.")
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
# ==========================================
# 3. START APP
# ==========================================
# Connect the Enter key to the generic function above
typing_bar.returnPressed.connect(command_processing)
to_screen("Finance Terminal v1.0")
to_screen("If you need help, type 'help' and press Enter to see the available commands.")

window.show()
typing_bar.setFocus()
sys.exit(app.exec())
