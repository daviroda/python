dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos Km foram rodados? '))
conv = (dias * 60) + (km * 0.15)
print(f'Alugando {dias} dias e rodando {km} km, você necessita pagar de aluguel {conv:.2f} R$')