import datetime
anoMaquina = datetime.datetime.now().year
maioridade = 0
menor = 0
for c in range(1, 8):
   anoNascimento =  int(input(f'Qual é o ano de nascimento da {c}° pessoa? '))
   idade = anoMaquina - anoNascimento
   if idade >= 18:
        maioridade += 1
   else:
        menor += 1
print(f'Ao todo tivemos {maioridade} pessoas maiores de idade \nE também tivemos {menor} pessoas menores de idade')
