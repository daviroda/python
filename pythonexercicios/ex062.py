print("Gerador de PA")
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = primeiro
cont = 1
total = 0
extra = 10
while extra != 0:
    total = total + extra
    while cont <= total:
        print(f'{termos} →', end=' ')
        termos += razao
        cont += 1
    print('PAUSA')
    extra = int(input("Quantos termos você quer mostrar a mais? "))
print(f'Progressão finalizada com {total} termos mostrados.')
