matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha][col] = int(input(f'Digite um valor para [{linha}, {col}]: '))
print('-='*30)
for linha in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[linha][col]:^5}]', end=' ')
        if matriz[linha][col] % 2 == 0:
            spar += matriz[linha][col]
    print()
print('-=' * 30)
print(f'A soma dos valores par é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][col]
print(f'A soma dos valores da terceira coluna é {scol}')
for col in range(0, 3):
    if col == 0:
        mai = matriz[1][col]
    elif matriz[1][col] > mai:
        mai = matriz[1][col]
print(f'O maior valor da segunda linha é {mai}.')
