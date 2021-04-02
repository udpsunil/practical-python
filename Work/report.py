# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        portfolio = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        return portfolio

if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    print(portfolio)
    print(sum(share*price for _, share, price in portfolio))