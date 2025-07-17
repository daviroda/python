frase = str(input("Digite uma frase: ")).strip().upper().split()
juntaFrase = ''.join(frase)
quantLetras = len(juntaFrase)
inversoFrase = ''
for letra in range(quantLetras -1, -1, -1):
    inversoFrase += juntaFrase[letra]
print(f'O inverso de {juntaFrase} é {inversoFrase}', end=' ')
if juntaFrase == inversoFrase:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase digitada não é um palíndromo!')
