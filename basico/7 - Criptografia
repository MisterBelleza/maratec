n = int(input())
for i in range(n):
    l = [ord(x)+3 if x.isalpha() else ord(x) for x in input()]
    l.reverse()
    l = [chr(l[i]-1) if i>=len(l)//2 else chr(l[i]) for i in range(len(l))]
    print(''.join(l))
