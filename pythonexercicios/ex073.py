clubes = ("Flamengo", "Palmeiras", "Cruzeiro",
          "Mirrasol", "Fluminense", "Botafogo",
          "Bahia", "São Paulo", "Grêmio",
          "Bragantino", "Atletico-MG", "Santos",
          "Corinthias", "Vasco da Gama", "EC vitória",
          "Internacional", "Ceára SC", "Fortaleza",
          "Juventude", "Sport Recife")
print('-=' *15)
print(f'Lista de Times: {clubes}')
print('-=' *15)
print(f'Os 5 primeiros são {clubes[0:5]}')
print('-=' *15)
print(f'Os 4 últimos são {clubes[-4:]}')
print('-=' *15)
print(f'Times em ordem alfabéticas: {sorted(clubes)}')
print('-=' *15)
print(f'O São Paulo está na {clubes.index('São Paulo')+1}º posição')
