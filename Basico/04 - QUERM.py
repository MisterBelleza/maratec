n = int(input())
teste = 1
while n != 0:
    ent = list(enumerate([int(i) for i in input().split()]))
    for tupla in ent:
        if tupla[0]+1 == tupla[1]:
            resp = tupla[1]
            break
    print("Teste", teste)
    teste += 1
    print(resp)
    n = int(input())