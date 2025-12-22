print('=' * 30)
print(f'{'BANCO':^30}')
print('=' * 30)
valor = int(input('Valor que deseja sacar? R$ '))
total = valor
cedula = 50
tot_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        tot_cedula += 1
    else:
        if tot_cedula > 0:
            print(f'Total de {tot_cedula} cédulas de R$:{cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot_cedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco!! Tenha um Bom dia!')