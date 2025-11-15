flag = 999
numbers = contDigitacao = soma = 0
numbers = int(input('Digite um número [999 para parar]: '))
while numbers != flag:
    cont = numbers
    contDigitacao += 1
    soma += numbers
    numbers = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contDigitacao} números e a soma entre eles foi {soma}')
