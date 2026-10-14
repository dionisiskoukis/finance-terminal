# main.py
import logging
import sys
import yfinance as yf

# 1. Ensure Dependencies
import setup_env
setup_env.ensure_dependencies()

# 2. Setup the UI and Commands
from ui_components import app, window, typing_bar, to_screen, show_terminal_banner
import finance_commands as cmds

logging.getLogger('yfinance').setLevel(logging.CRITICAL)

# State Variables for the Parser
user_input = ""
number_of_words = 0
command = ""

def one_word_command():
    global command
    command = user_input
    
def two_word_command():
    global command
    command_split = user_input.split() 
    command = command_split[0]
    cmds.parameter = command_split[1].upper() # Maps directly to the commands module

def four_word_command():
    global command
    command_split = user_input.split() 
    command = command_split[0]
    cmds.parameter = command_split[1].upper() 
    cmds.start_date = command_split[2]
    cmds.end_date = command_split[3]

def command_processing():
    global user_input, number_of_words, command
    user_input = typing_bar.text().strip()
    typing_bar.clear()

    if user_input == "":
        return

    number_of_words = len(user_input.split())
    to_screen(f"> {user_input}")

    if number_of_words == 1:
        one_word_command()
    elif number_of_words == 2:
        two_word_command()
    elif number_of_words == 4:
        four_word_command()
    else:
        command = ""

    # Command Dispatcher
    if command == "help":
        cmds.help()
        to_screen("")
    elif command == "get":
        cmds.get()
    elif command == "getrt":
        cmds.getrt()
    elif command == "exit":
        to_screen("Exiting the program.")
        app.quit()
    elif command == "afs":
        cmds.annual_financial_statements()
    elif command == "qfs":
        cmds.quarterly_financial_statements()
    elif command == "ticker_info":
        cmds.ticker_info()
    elif command == "goldinfo":
        cmds.goldinfo()
    elif command == "silverinfo":
        cmds.silverinfo()
    elif command == "copperinfo":
        cmds.copperinfo()
    elif command == "palladiuminfo":
        cmds.palladiuminfo()
    elif command == "platinuminfo":
        cmds.platinuminfo()
    elif command == "news":
        cmds.news()
    elif command == "pin":
        cmds.pin()
    elif command == "unpin":
        cmds.unpin()
    elif command == "licence":
        cmds.licence()
    elif command == "options":
        cmds.options()
    elif command == "major_holders":
        cmds.major_holders()
    elif command == "inst_holders":
        cmds.institutional_holders()
    elif command == "apt":
        cmds.analysts_price_targets()
    elif command == "rec":
        cmds.recomendations()
    elif command == "hca":
        cmds.historical_corporate_actions()
    elif command == "clear":
        cmds.clear()
    elif command == "insider_transactions":
        cmds.insider_transactions()
    elif command == "sustainability":
        cmds.sustainability()
    elif command == "index_funds":
        cmds.index_funds()
    else:
        to_screen("Invalid command. Type 'help' to see the list of available commands.")

typing_bar.returnPressed.connect(command_processing)
show_terminal_banner()

# Pinned Stocks Routine
try:
    with open("pinned_stocks.txt", "r") as file:
        pinned_tickers = file.read().splitlines()
        
        for ticker in pinned_tickers:
            ticker = ticker.strip()
            if ticker: # Skips empty lines
                stock_info = yf.Ticker(ticker).info
                long_name = stock_info.get('longName', 'N/A')
                sector = stock_info.get('sector', 'N/A')
                industry = stock_info.get('industry', 'N/A')
                market_cap = stock_info.get('marketCap', 'N/A')
                pe_ratio = stock_info.get('trailingPE', 'N/A')
                
                to_screen("Info pinned from last session.")
                to_screen("longName: " + str(long_name))
                to_screen("sector: " + str(sector))
                to_screen("industry: " + str(industry))
                to_screen("marketCap: " + str(market_cap))
                to_screen("trailingPE: " + str(pe_ratio))
                to_screen(" ")
                
except FileNotFoundError:
    with open("pinned_stocks.txt", "w") as file:
        pass

window.show()
typing_bar.setFocus()
sys.exit(app.exec())
