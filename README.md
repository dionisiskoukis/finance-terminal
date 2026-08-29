# Finance Terminal


A desktop GUI application that provides a terminal-like interface for accessing real-time and historical financial data for stocks, commodities, and indices.

## Features

- **GUI Terminal**: A dedicated terminal window built with PySide6 for all financial commands.
- **Stock Data**: Access real-time prices and historical data for any stock ticker.
- **Financial Statements**: Retrieve annual and quarterly financial statements, including income statements, balance sheets, and cash flow.
- **Company Information**: Get detailed company profiles, including sector, industry, market cap, and P/E ratio analysis.
- **Market Insights**: Fetch analyst recommendations, price targets, major holders, insider transactions, and sustainability scores.
- **Commodities & Indices**: Check real-time prices for precious metals (Gold, Silver, etc.) and major market indices.
- **Corporate Actions**: View historical data on dividends, stock splits, and other corporate actions.
- **News Feed**: Get the latest news for a specified ticker.
- **Pinning**: Pin stocks to view their information automatically on startup.

## Getting Started

### Prerequisites

- Python 3.x
- Pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/dionisiskoukis/finance-terminal.git
    cd finance-terminal
    ```

2.  Install the required packages. The application will attempt to install missing dependencies, but you can also install them manually:
    ```bash
    pip install yfinance xfinance PySide6 "httpx[http2]"
    ```

### Running the Application

Execute the `main.py` script to launch the Finance Terminal:

```bash
python main.py
```

## Command Reference

Enter any of the following commands into the terminal window.

| Command | Parameters | Description |
| :--- | :--- | :--- |
| `help` | - | Displays the list of all available commands. |
| `get` | `[ticker] [start_date] [end_date]` | Fetches historical price data for a stock. (e.g., `get TSLA 2022-01-01 2023-01-01`) |
| `getrt` | `[ticker]` | Gets the real-time market price for a stock. |
| `afs` | `[ticker]` | Retrieves the annual financial statements (income, balance sheet, cash flow). |
| `qfs` | `[ticker]` | Retrieves the quarterly financial statements. |
| `ticker_info` | `[ticker]` | Shows company information, including P/E ratio analysis. |
| `news` | `[ticker]` | Gets the latest news related to the stock. |
| `major_holders`| `[ticker]` | Shows the major holders of the specified stock. |
| `inst_holders`| `[ticker]` | Shows the institutional holders of the specified stock. |
| `apt` | `[ticker]` | Displays analyst price targets for the stock. |
| `rec` | `[ticker]` | Shows buy/sell/hold recommendations from analysts. |
| `insider_transactions`| `[ticker]` | Shows recent insider transactions for the stock. |
| `sustainability`| `[ticker]` | Displays the company's sustainability (ESG) scores. |
| `hca` | `[ticker]` | Shows historical corporate actions (dividends, splits). |
| `options` | `[ticker]` | Shows available option expiry dates for the stock. |
| `pin` | `[ticker]` | Saves a ticker to `pinned_stocks.txt` to display its info on startup. |
| `unpin` | `[ticker]` | Removes a ticker from the pinned list. |
| `index_funds` | - | Shows the current prices of major index funds (S&P 500, Dow Jones, etc.). |
| `goldinfo` | - | Gets the real-time price of Gold. |
| `silverinfo` | - | Gets the real-time price of Silver. |
| `copperinfo` | - | Gets the real-time price of Copper. |
| `palladiuminfo`| - | Gets the real-time price of Palladium. |
| `platinuminfo`| - | Gets the real-time price of Platinum. |
| `clear` | - | Clears the terminal screen. |
| `licence` | - | Displays the software license information. |
| `exit` | - | Closes the application. |

## License

This project is licensed under the MIT License - see the [LICENCE](LICENCE) file for details.

