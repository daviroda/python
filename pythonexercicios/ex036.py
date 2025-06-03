valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Salário do comprador? '))
anos = int(input('Em quantos anos pretende pagar o emprestimo? '))
prestacaoMensal = valorCasa / (anos * 12)
minimo = (salario * 30) / 100
if prestacaoMensal <= minimo:
    print(f'Para pagar uma casa de R${valorCasa:.2f} em {anos} anos a prestação será de R${prestacaoMensal:.2f}. Empréstimo CONCEDIDO!!')
elif prestacaoMensal > minimo:
    print(f'Para pagar uma casa de R${valorCasa:.2f} em {anos} anos a prestação será de R${prestacaoMensal:.2f}. Empréstimo NEGADO!!')