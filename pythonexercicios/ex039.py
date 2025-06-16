import datetime

sexo = input('Qual é o sexo(M: masculino & F: feminino)? ')
nascimento = int(input('Ano de nascimento: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - nascimento

if sexo == 'f':
    print('O sexo feminino não tem alistamento obrigatório \nMas se fosse do sexo masculino:')
elif sexo == 'm':
    print('O sexo masculino tem o alistamento obrigatório')
if idade < 18:
    saldo = 18 - idade
    anoAlistamento = anoAtual + saldo
    print(f'Com a idade de {idade} anos em {anoAtual}\nA pessoa DEVE SE ALISTAR em {saldo} anos \nSeu alistamento será em {anoAlistamento}')
elif idade > 18:
    saldo = idade - 18
    anoAlistamento = anoAtual - saldo
    print(f'Com a idade de {idade} anos em {anoAtual}\nA pessoa DEVERIA TER SE ALISTADO há {saldo} anos \nSeu alistamento foi em {anoAlistamento}')
else:
    print(f'Com a idade de {idade} anos em {anoAtual}\nA pessoa deve se alistar IMEDIATAMENTE!!')
