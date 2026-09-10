def leiaInt(num):
    while True:
        numero = input(num)
        if numero.isnumeric():
            return int(numero)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

# Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
