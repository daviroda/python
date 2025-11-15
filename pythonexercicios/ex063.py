print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
number = int(input("Quantos termos você quer mostrar? "))
cont = 3
t1 = 0
t2 = 1
t3 = t1 + t2
print(f'{t1} → {t2}', end='')
while cont <= number:
    t3 = t1 + t2
    cont += 1
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
print(' → FIM')
