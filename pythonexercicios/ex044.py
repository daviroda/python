print(f'====LOJAS DAVI====')
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO: 
[1] à vista dinheiro/cheque 
[2] à vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    precoDesconto10 = preco - (preco / 100 * 10)
    print(f'Sua compra de R${preco:.2f} vai custar R${precoDesconto10:.2f} no final')
elif opcao == 2:
    precoDesconto5 = preco - (preco / 100 * 5)
    print(f'Sua compra de R${preco:.2f} vai custar R${precoDesconto5:.2f} no final')
elif opcao == 3:
    divicaoValor = preco / 2
    print(f'A compra foi parcelada no cartão à 2x de R${divicaoValor:.2f} SEM JUROS \nSua compra terá o mesmo valor de R${preco:.2f}')
elif opcao == 4:
    quantParcelas = int(input('Quantas parcelas? '))
    juros = (preco / 100 * 20)
    precoFinal = preco + juros
    divicaoValor = precoFinal / quantParcelas
    print(f'Sua compra será parcelada em {quantParcelas}x de R${divicaoValor:.2f} COM JUROS \nSua compra de R${preco:.2f} vai custar R${precoFinal:.2f} no final.')
else:
    print('OPÇÃO INVÁLIDA de pagamento. tente novamente')
