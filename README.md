
# Finance Terminal




## Features

- A guide to each command of the terminal
- Access to every stock's price info in real time
- Ability to check a stock's price during a defined period of time
- Info about gold




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
- To get info about gold, type:

```bash
  goldinfo
```
- And finally, to exit the terminal, type:

```bash
  exit
```

## Future plans

 - Creating a terminal outside of vs code, only for the app
 - Ability to download prices of stocks (real time, or from a certain period)
 - Ability to "pin" certain stocks or metals so that when you open the application, you see them without giving any commands
 - Adding more metals to the application
 - Adding more usefull info (dividents, P/E ratio)
- Automating the fundamental analysis to a certain level
- Adding UI to the terminal using a library like "rich"
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

