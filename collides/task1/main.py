a, b, c = map(int, input().split())
a1, b1, c1 = map(int, input().split())

res = ["YES", "NO"]
print(res[(a - a1) ** 2 + (b - b1) ** 2 > (c + c1) ** 2])
