valores = [[], []]
valor = 0
for c in range(1,8):
    valor = int((input(f'Digite o {c}° valor: ')))
    if valor % 2 == 0:
        valores[0].append([valor])
    elif valor % 2 == 1:
        valores[1].append([valor])
print('-=' *30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
