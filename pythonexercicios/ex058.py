from random import randint
number_random = randint(0, 10)
print('Sou seu computador.. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
tentativas_total = 0
while not acertou:
    num_usuario = int(input('Qual é seu palpite? '))
    tentativas_total += 1
    if num_usuario == number_random:
        acertou = True
    else:
        if num_usuario < number_random:
            print('Mais... Tente mais uma vez.')
        elif num_usuario > number_random:
            print('Menos... Tente mais uma vez.')
print(f'Acertou! com {tentativas_total} tentativas. Parabéns!')
