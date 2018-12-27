import csv
import os
import statistics

from data_type import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_data(filename)
    query_data(data)


def print_header():
    print('------------------------------')
    print('----   Real App Yo     -------')
    print('------------------------------')
    print('\n')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'SacramentoRealEstateTransactions2008.csv')


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        purchases = []
        reader = csv.DictReader(fin)
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    return purchases


def query_data(data):
    #def query_data(data):  # list[Purchase]):

    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print(
        f"The most expensive house is ${high_purchase.price:,} with {high_purchase.beds} beds and {high_purchase.baths} baths")

    low_purchase = data[0]
    print(
        f"The least expensive house is ${low_purchase.price:,} with {low_purchase.beds} beds and {low_purchase.baths} baths")

    # average price house?
    # prices = list()  # []
    # for pur in data:
    #     prices.append(pur.price)

    prices = (
        p.price  # projection or items
        for p in data  # the set to process
    )

    ave_price = statistics.mean(prices)
    print(f"The average home price is ${int(ave_price):,}")

    # average price of 2 bedroom houses
    # prices = []
    # baths = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce(p, f'2-bedrooms, found {p.beds}') and p.beds == 2  # test / condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))
    print(f"Average 2-bedroom home is ${int(ave_price):,}, baths={round(ave_baths, 1)}, sq ft={round(ave_sqft, 1):,}")


def announce(item, msg):
    print(f"Pulling item {item} for {msg}")
    return item


if __name__ == '__main__':
    main()
