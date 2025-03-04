preco = float(input('Qual é o preço do produto? R$'))
novo_preco = preco - 5 * preco / 100
print(f'O produto tem o preço de {preco:.2f} e com um desconto de 5% você pagará: {novo_preco:.2f}R$')