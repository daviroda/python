from random import choice

pri_aluno = str(input('Qual é o primeiro aluno? '))
sec_aluno = str(input('Qual é o segundo aluno? '))
ter_aluno = str(input('Qual é o terceiro aluno? '))
quar_aluno = str(input('Qual é o quarto aluno? '))
lista_alunos = [pri_aluno, sec_aluno, ter_aluno, quar_aluno]
sorteio = choice(lista_alunos)
print(f'O aluno sorteado foi {sorteio}')