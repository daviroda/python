import datetime
from datetime import datetime

ano = int(input('Me diga um ano para analisar se ele é bissexto: Se querer pegar o ano atual digite 0:'))

if ano != 0:
    if (ano % 4 == 0) and (ano % 100 == 0) is (ano % 400 == 0):
        print(f'O ano {ano} É BISSEXTO')
    else:
        print(f'O ano {ano} NÃO É BISSEXTO')

if ano == 0:
    anoMaquina = datetime.now().year
    if (anoMaquina % 4 == 0) and (anoMaquina % 100 == 0) is (anoMaquina % 400 == 0):
        print(f'O ano {anoMaquina} É BISSEXTO')
    else:
        print(f'O ano {anoMaquina} NÃO É BISSEXTO')