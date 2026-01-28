vals = []
while True:
    vals.append(int(input('Digite um valor: ')))
    cond = str(input('Deseja continuar[S/N]? '))
    if cond in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(vals)} elementos.')
vals.sort(reverse=True)
print(f'Os valores em ordem decrescente são {vals}')
if 5 in vals:
    print('O numero 5 faz parte da lista!')
else:
    print('O numero 5 não faz parte da lista!')
