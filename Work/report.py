# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        folio = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            folio.append(holding)
        return folio


def read_portfolio_dict(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        folio = []
        for row in rows:
            holding = dict(zip(['name', 'shares', 'price'], [row[0], int(row[1]), float(row[2])]))
            folio.append(holding)
        return folio


def read_prices(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        prices_dict = {}
        try:
            for row in rows:
                prices_dict[row[0]] = float(row[1])
        except IndexError:
            print(f'Row {row} has bad entries')
        return prices_dict


def compute_value_of_portfolio(portfolio_path, prices_path):
    folio = read_portfolio_dict(portfolio_path)
    prices_dict = read_prices(prices_path)
    profit = 0
    print('{name:>16s} {share:>16s} {price:>16s} {change:>16s}'.format(name="Name", share="Shares", price="Price",
                                                                       change="Change"))
    print(16*"-", 16*"-", 16*"-", 16*"-")
    for share_entry in folio:
        share = share_entry['name']
        total_shares = share_entry['shares']
        bought_prices = share_entry['price']
        current_price = prices_dict[share] if share in prices_dict else 0
        print(f'{share:>16s} {total_shares:>16d} {bought_prices:>16.2f} {bought_prices - current_price:>16.2f}')
        profit += total_shares * current_price - total_shares * bought_prices
    return profit


if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    print(portfolio)
    print(sum(share * price for _, share, price in portfolio))
    portfolio = read_portfolio_dict('Data/portfolio.csv')
    print(portfolio)
    print(sum(s['shares'] * s['price'] for s in portfolio))
    prices = read_prices('Data/prices.csv')
    print(prices)
    print(compute_value_of_portfolio('Data/portfolio.csv', 'Data/prices.csv'))
