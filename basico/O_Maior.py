a,b,c = [int(i) for i in input().split()]
a = (a+b+abs(a-b))/2
a = (a+c+abs(a-c))/2
print("%d eh o maior" %a)
