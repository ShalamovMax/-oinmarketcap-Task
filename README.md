# Coinmarketcap-Task
Task to Koshelek.ru

# Coinmarketcap-scraper

Historical data scraper for [coinmarketcap](https://coinmarketcap.com/) written in python 3.

## Dependencies
- bs4
- numpy
- pandas
- requests
- tqdm
```
pip install bs4 numpy pandas requests tqdm
```

## Usage
Scrape all historical data for all coins:
```
python scrape.py --outfile all.csv
```

Filter on date range and coins:
```
python scrape.py --outfile small.csv --start 2018-01-01 --end 2018-01-31 --symbols BTC ETH
```
