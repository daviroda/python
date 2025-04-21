from random import  randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
numUsuario = int(input('Digite um número de 0 a 5: ')) # Interage com o jogador e ele tenta adivinhar o número
numberRandom = randint(0, 5) # O computador randomiza o número
print('PROCESSANDO...')
sleep(2)
if numUsuario == numberRandom:
    print('Parabéns você ganhou do computador!!')
else:
    print(f'Owhh Você perdeu!! o numero era {numberRandom} e não {numUsuario}') # Condição feita para o Vencedor o usuario ou o computador
