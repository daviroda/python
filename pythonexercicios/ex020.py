from random import shuffle

aluno1 = str(input('Primeiro aluno: '))
aluno02 = str(input('Segundo aluno: '))
aluno03 = str(input('Terceiro aluno: '))
aluno04 = str(input('Quarto aluno: '))
lista = [aluno1, aluno02, aluno03, aluno04]
ordem = shuffle(lista)
print(f'A ordem é {lista}')