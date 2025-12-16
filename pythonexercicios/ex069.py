maioridade = mulheres_menor_20 = homens = 0
while True:
    print('--'*30)
    print('CADASTRE UMA PESSOA')
    print('--'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulheres_menor_20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com amis de 18 anos: {maioridade} \nAo todo temos {homens} homens cadastrados \nE temos {mulheres_menor_20} mulheres com menos de 20 anos')
