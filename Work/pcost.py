# pcost.py
#
# Exercise 1.27

import sys


def get_no_and_cost(line):
    try:
        stock, no, cost = line.strip().split(',')
        cost = int(no) * float(cost)
    except ValueError:
        print(f"Warining: Couldn't parse the line {line}")
        return 0.0
    return cost


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as read_f:
        headers = next(read_f)
        total_cost = sum(get_no_and_cost(line) for line in read_f)
    return round(total_cost, 2)


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) == 2 else 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    # cost = portfolio_cost('Work/Data/missing.csv')
    print(f'Total cost {cost}')
