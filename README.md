
# Finance Terminal

## Features
- A guide to each command of the terminal
- Access to every stock's price info in real time
- Ability to check a stock's price during a defined period of time
- Info about gold
- A terminal window specifically for these commands


## Basic Commands (demo)

- To find the instrucitons of the app type:

```bash
  help
```
- To get a stock's price during a specific period of time, type:

```bash
  get [stock_ticker] [starting_point] [ending_point]
```
Example:

```bash
  get TSLA 2020-01-01 2025-01-01
```
- To get a stock's real time value, type:

```bash
  getrt [stock_ticker]
```
Example:

```bash
  getrt TSLA
```
- To get the financials of a stock, type:

- To get info about gold, type:
```bash
   financials [stock_ticker]
```
Example:
```bash
  financials MSFT
```
- To get the balance sheet of a stock, type:
```bash
  balance_sheet [stock_ticker]
```
Example:
```bash
  balance_sheet AAPL
```
- To get info about gold
```bash
  goldinfo
```
- And finally, to exit the terminal, type:

```bash
  exit
```
## Updades
- Added new commands (financials, balance_sheet)
- Created a terminal specifically for this application
- Added any essential UI
- Added the pin command
- Added new metals

## Future plans

 - Ability to download prices of stocks (real time, or from a certain period)
 - Adding more usefull info (dividents, P/E ratio)
 - Automating the fundamental analysis to a certain level
## License

[MIT](https://choosealicense.com/licenses/mit/)

