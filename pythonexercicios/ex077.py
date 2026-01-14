palavras = ('APRENDER', 'PROGRAMAR',
            'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos vogais ', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra.lower()}', end=' ')
