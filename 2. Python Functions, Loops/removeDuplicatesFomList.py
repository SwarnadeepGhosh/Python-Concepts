prices = [21, 1, 1, 5, 23, 21, 1, 4, 4, 4]
uniques = []

for price in prices:
    if price not in uniques:
        uniques.append(price)
print(prices)
print(uniques)