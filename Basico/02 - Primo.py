n = int(input())
if n<=1:
    print("nao")
else:
    primo = True
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and primo:
            print("nao")
            primo = False
    if primo: print("sim")