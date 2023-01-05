x, y, st, fn = map(int, input().split())
x1, y1, st1, fn1 = map(int, input().split())


ax1, ay1, ax2, ay2 = [x, y, x + st, y + fn]
bx1, by1, bx2, by2 = [x1, y1, x1 + st1, y1 + fn1]

xA = [ax1, ax2]
xB = [bx1, bx2]

yA = [ay1, ay2]
yB = [by1, by2]

if max(xA) < min(xB) or max(yA) < min(yB) or min(yA) > max(yB) or min(xA) > max(xB):
    print("NO")

elif max(xA) > min(xB) and min(xA) < min(xB):
    print("YES")
else:
    print("YES")
