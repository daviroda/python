import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opcaoJogador = int(input('Qual é a sua jogada? '))
opcaoMaquina = random.randrange(0, 3)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("=-"*20)
print(f'O computador jogou {itens[opcaoMaquina]}')
print(f'O jogador jogou {itens[opcaoJogador]}')
print("=-"*20)
if opcaoJogador == 0: # Jogador jogou Pedra
    if opcaoMaquina == 1:
        print('COMPUTADOR VENCEU!!')
    elif opcaoMaquina == 2:
        print('JOGADOR VENCEU!!')
    elif opcaoMaquina == opcaoJogador:
        print('DEU EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')
elif opcaoJogador == 1: # Jogador jogou Papel
    if opcaoMaquina == 0:
        print('JOGADOR VENCEU!!')
    elif opcaoMaquina == 2:
        print('COMPUTADOR VENCEU!!')
    elif opcaoMaquina == opcaoJogador:
        print('DEU EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')
elif opcaoJogador == 2:  # Jogador jogou Tesoura
    if opcaoMaquina == 0:
        print('COMPUTADOR VENCEU!!')
    elif opcaoMaquina == 1:
        print('JOGADOR VENCEU!!')
    elif opcaoMaquina == opcaoJogador:
        print('DEU EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')
