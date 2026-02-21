matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha][col] = int(input(f'Digite um valor para [{linha}, {col}]: '))
print('-='*30)
for linha in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[linha][col]:^5}]', end=' ')
    print()
