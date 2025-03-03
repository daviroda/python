reais = float(input('Quanto dinheiro você possui? R$'))
conv_dolar = reais / 5.91
conv_euro = reais / 6.15
print(f'Você possui {reais} R$, com a cotação a 5,91 você possui {conv_dolar:.2f} USD, e com a cotação em 6,15 você possui {conv_euro:.2f} EUR')