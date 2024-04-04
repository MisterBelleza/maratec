n = int(input())
for i in range(n):
    a, b = [int(x) for x in input().split()]
    j = a // b
    if b * j < a:
        print(b * (j+1) - a)
    else:
        print(b * j - a)