print('10 PRIMEIROS TERMOS DE UMA PA')
print('=='*20)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termos = primeiro_termo
cont = 0
while cont <= 10:
    print(f'{termos} →', end=' ')
    termos += razao
    cont += 1
print('FIM!!')
