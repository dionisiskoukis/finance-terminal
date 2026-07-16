#Libraries
import yfinance as yf
import logging

global user_input
global number_of_words


def command_processing():
    global user_input, number_of_words
    user_input = input("Enter a command: ")
    number_of_words = len(user_input.split())

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
    print("Available commands:")
    print("get [ticker] [start_date] [end_date] - Get historical data for the specified ticker between the given dates")
    print("getrt [ticker] - Get real-time price for the specified ticker")
    print("exit - Exit the program")
    
def get():
    try:
        data = yf.download(parameter, start=start_date, end=end_date)
        print(data.info())
        print(data.head())
    except Exception as e:
        print(f"Error, {parameter} is not a valid ticker symbol. Please try again")
def getrt():
    try:
        stock = yf.Ticker(parameter)
        price = stock.info['regularMarketPrice']
            
    except Exception as e:
        print(f"Error: {parameter} is not a valid ticker symbol.")
            
    else:
        print(f"Current price of {parameter}: {price}")
def fundamentals():
    pass
def goldinfo():
    ticker = 'GC=F'
    stock = yf.Ticker(ticker)
    info = stock.info
    gold_price = stock.info['regularMarketPrice']
    print(f"Current price of Gold: {gold_price}")

# This completely silences yfinance's internal console printing
logging.getLogger('yfinance').setLevel(logging.CRITICAL)


#Welcome text
print("Welcome to our finance terminal")
print("If you havent used this tool before, please type 'help' to see the list of commands")
print("If you have used this tool before, have fun using it again!")




        
#main program
while True:
    command_processing()

    #number of words in the command determines how the input is processed
    if number_of_words == 1:
        one_word_command()
    elif number_of_words == 2:
        two_word_command()
    elif number_of_words == 4:
        four_word_command()
    else:
        command = ""


    #command processing
    if command == "help":
        help()
    elif command == "get":
       get()
    elif command == "getrt":
        getrt()
    elif command == "exit":
        print("Exiting the program.")
        break
    elif command == "fundamentals":
        fundamentals()
    elif command == "goldinfo":
        goldinfo()