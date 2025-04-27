distancia = float(input("Qual é a distância da sua viagem? "))
preço = distancia * 0.50 if distancia <=200 else distancia * 0.45
print(f'Você vai iniciar uma viagem de {distancia}Km \n E o preço da passagem será de R${preço:.2f}')