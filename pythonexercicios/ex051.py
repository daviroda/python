print('=='*20)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=='*20)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termos = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, termos + razao, razao):
    print(c, end=' → ')
print('ACABOU')