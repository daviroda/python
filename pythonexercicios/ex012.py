preco = int(input('Qual é o preço do produto? '))
novopreco = int(preco - 5 * preco / 100)
print(f'O produto tem o preço de {preco} e com um desconto de 5% você pagará: {novopreco}')