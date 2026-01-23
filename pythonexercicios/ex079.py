lst_nums = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lst_nums:
        lst_nums.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print('-='*30)
lst_nums.sort()
print(f'Você digitou os valores {lst_nums}')
