# Crypto Price Tracker

A simple cryptocurrency tracker built with Python that displays real-time crypto market data using an external API.

## Features

- Track cryptocurrency prices in real-time
- Display market capitalization
- Show 24-hour price changes
- Colored terminal output
- Simple and beginner-friendly project structure

## Technologies Used

- Python
- Requests
- Colorama
- CoinGecko API

## Installation

Clone the repository:

```bash
git clone https://github.com/bonaarhousell/crypto-price-tracker.git
```

Move into the project folder:

```bash
cd crypto-price-tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The Project

```bash
python main.py
```

## Example Output

```txt
Bitcoin (BTC)
Price: $68,000
Market Cap: $1.3T
24h Change: +2.4%
```

## Project Structure

```txt
crypto-price-tracker/
│
├── api.py
├── config.py
├── display.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## What I Learned

- Working with APIs in Python
- JSON data handling
- Terminal formatting
- Virtual environments
- Git and GitHub workflow

## Future Improvements

- Add support for multiple cryptocurrencies
- Build a graphical interface
- Add price alerts
- Store historical price data
- Add charts and visualization

## Author

Muhammad Nur Muliadi