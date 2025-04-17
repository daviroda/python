Cidade = str(input('Qual cidade você mora? ')).strip().lower()
reformat = Cidade.split()
Verificação = 'santo' in reformat[0]
print(f'{Verificação}')