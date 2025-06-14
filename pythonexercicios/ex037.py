num = int(input('Digite um número que deseja converter: '))
base = int(input('''Escolha uma das bases para a conversão:
[1] para binário
[2] para octal
[3] para hexadecimal
Qual base gostaria de converter?'''))
if base == 1:
    binario = bin(num)
    print(f'{num} convertido para {binario[2:]}')
elif base == 2:
    octal = oct(num)
    print(f'{num} convertido para {octal[2:]}')
elif base == 3:
    hexadecimal = hex(num)
    print(f'{num} convertido para {hexadecimal[2:]}')
else:
    print('Opção inválida. Tente novamente')