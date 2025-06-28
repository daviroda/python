peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
calculoIMC = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {calculoIMC:.2f}')
if calculoIMC < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= calculoIMC < 25:
    print('Você está no PESO IDEAL')
elif 25 <= calculoIMC < 30:
    print('Você está ACIMA DO PESO normal')
elif 30 <= calculoIMC < 40:
    print('Você está com OBESIDADE. CUIDADO!!')
else:
    print('Você está com OBSEIDADE MÓRBIDA. CUIDADO!!')
