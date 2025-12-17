total_gasto = cont_mais_1000 = menor_preco = cont = 0
nome_barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        cont_mais_1000 += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_barato = nome
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'FIM DO PROGRAMA')
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {cont_mais_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa {menor_preco}')
