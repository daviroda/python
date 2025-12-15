from random import randint
cont_vitorias = 0
while True:
    num = int(input('Digite um número: '))
    jogo_computador = randint(0, 11)
    soma = num + jogo_computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {num} e o computador {jogo_computador}. Total de {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont_vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont_vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont_vitorias} vezes')
