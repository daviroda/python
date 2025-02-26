largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
conv = area / 2**2
print(f'A altura da parede é: {altura}, a largura da parede é: {largura} a area da parede é: {area}, a quantidade de tinta necessária seria: {conv}')