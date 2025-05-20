salario = float(input('Salario do funcionário R$:'))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
    print(f'Quem ganhava {salario:.2f} passa a ganhar {novoSalario:.2f} agora!!')
else:
    novoSalario = salario + (salario * 10 / 100)
    print(f'Quem ganhava {salario:.2f} passa a ganhar {novoSalario:.2f} agora!!')