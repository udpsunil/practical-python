# report.py
#
# Exercise 2.4
import csv
from os import O_APPEND

def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        portfolio = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        return portfolio

def read_portfolio_dict(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        portfolio = []
        for row in rows:
            holding = dict(zip(['name', 'shares', 'price'], [row[0], int(row[1]), float(row[2])]))
            portfolio.append(holding)
        return portfolio

def read_prices(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        prices = {}
        try:
            for row in rows:
                prices[row[0]] = float(row[1]) 
        except IndexError:
            print(f'Row {row} has bad entries')
        return prices

def compute_value_of_portfolio(portfolio_path, prices_path):
    portfolio = read_portfolio_dict('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    profit = 0
    for share_entry in portfolio:
        share = share_entry['name']
        total_shares = share_entry['shares']
        bought_prices = share_entry['price']
        current_price = prices[share] if share in prices else 0
        profit += total_shares * current_price - total_shares * bought_prices
    return profit


if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    print(portfolio)
    print(sum(share*price for _, share, price in portfolio))
    portfolio = read_portfolio_dict('Data/portfolio.csv')
    print(portfolio)
    print(sum(s['shares'] * s['price'] for s in portfolio))
    prices = read_prices('Data/prices.csv')
    print(prices)
    print(compute_value_of_portfolio('Data/portfolio.csv', 'Data/prices.csv'))