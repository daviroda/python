import datetime

anoMaquina = datetime.datetime.now().year
anoNascimento = int(input('Qual é o ano de nascimento do atleta? '))
idade = anoMaquina - anoNascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print(f'Sua categoria é INFANTIL')
elif idade <= 19:
    print(f'Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('sua categoria é MASTER')
