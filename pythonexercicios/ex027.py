nome = str(input('Digite seu nome completo: ')).strip()
reformatNome = nome.split()
primeiroNome = reformatNome[0]
ultimoNome = reformatNome[len(reformatNome)-1]
print(f'Muito prazer em te conhecer!! \n Seu primeiro nome é {primeiroNome} \n Seu último nome é {ultimoNome}')
