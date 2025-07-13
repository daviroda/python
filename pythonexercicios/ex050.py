soma = 0
cont = 0
for c in range(1, 7):
    nums = int(input(f'Digite o {c} valor: '))
    if nums % 2 == 0:
        soma += nums
        cont += 1
print(f'A soma entre os {cont} NÚMEROS PARES são {soma}')