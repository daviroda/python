nome = str(input('Qual é seu nome? '))
if nome == 'Davi':
    print('Nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print(f'Nome normal {nome}')
print(f'Tenha um bom dia {nome}!!')