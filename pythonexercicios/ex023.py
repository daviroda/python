num = int(input('Informe um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num //  100 % 10
milar = num // 1000 % 10
print(f'Analisando o número {num} \n Unidade: {unidade}, dezena: {dezena}, centena: {centena}, milhar: {milar}')