d = int(input())
a = d // 365
m = (d - a*365) // 30
d -= a*365 + m*30
print("%d ano(s)\n%d mes(es)\n%d dia(s)"%(a,m,d))
