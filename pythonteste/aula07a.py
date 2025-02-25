n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
potenciacao = n1 ** n2
print(f'A soma é {soma}, \n o produto é {multiplicacao} e a \n divisão é {divisao:.3f}', end=' ')
print(f'Divisão inteira {divisao_inteira} e potência {potenciacao}')