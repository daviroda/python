def ficha(jog='<desconhecido>', gol=0):
    print(f'O Jogador {jog} fez {gol} gols(s) no campeonato.')

# Programa principal
n = str(input("Nome do Joador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
