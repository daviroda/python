velocidade = float(input('Qual é a velocidade do seu veiculo? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"MULTADO!! Você excendeu o limite permitido que é de 80Km/h \n Você deve pagar uma multa de R${multa:.2f}!")
    print('Tenha um ótimo dia!! Dirija com segurança!')
else:
    print('Tenha um ótimo dia!! Dirija com segurança!')