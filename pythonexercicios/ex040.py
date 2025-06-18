nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2} o aluno fica com a média de {media:.1f}')
if 6.9 > media >= 5:
    print(f'O aluno está de RECUPERAÇÃO')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está APROVADO')