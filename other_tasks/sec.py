products = dict()
for _ in range(int(input())):
    name, price = input().split('\t')
    products[name] = int(price)
input()


def getOrder():
    total = 0
    while 1:
        order = input()
        if order == '.':
            return total, True
        elif order == '':
            if total == 0:
                continue
            else:
                return total, False
        else:
            name, count = order.split('\t')
            total += products[name] * int(count)


totals = list()
while 1:
    total = 0
    price, state = getOrder()
    total += price
    if total > 0:
        totals.append(total)

    if state:
        break

for i, price in enumerate(totals):
    print(f'{i + 1}) {price}')
print(f'Итого: {sum(totals)}')
