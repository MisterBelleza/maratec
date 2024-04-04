n_col, n_lin = [int(i) for i in input().split()]
matrix = []
maior_linha = 0
for i in range(n_col):
    linha = [int(i) for i in input().split()]
    matrix.append(linha)
    if sum(linha) > maior_linha:
        maior_linha = sum(linha)
maior_col = max([sum(col) for col in zip(*matrix)])
if maior_col > maior_linha:
    print(maior_col)
else: print(maior_linha)