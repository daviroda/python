cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[34m{c}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisivel {cont} vezes')
if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!!')
