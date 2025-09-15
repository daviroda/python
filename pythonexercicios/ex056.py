guardar_idade = 0
nome_velho = ''
maiorid_masculino = 0
menor20f = 0
for c in range(1, 5):
    print(f'---- {c}ª PESSOA----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    if idade < 20 and sexo.strip() in 'Ff':
        menor20f += 1
    guardar_idade += idade
    if c == 1 and sexo.strip() in 'Mm':
        maiorid_masculino = idade
        nome_velho = nome
    if sexo.strip() in 'Mm' and idade > maiorid_masculino:
        maiorid_masculino = idade
        nome_velho = nome
media = guardar_idade / 4
print(f'A média de idade do grupo é de {media} anos \nO homem mais velho tem {maiorid_masculino} anos e se chama {nome_velho} \nAo todo são {menor20f} '
      f'mulheres '
      f'com menos de 20 anos')
