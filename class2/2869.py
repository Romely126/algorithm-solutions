a, b, v = map(int, input().split())

remain = v - a

days = remain // (a - b)

if remain % (a - b):
    days += 1

print(days + 1)