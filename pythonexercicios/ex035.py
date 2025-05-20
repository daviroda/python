print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Comprimento do primeiro segmento: '))
r2 = float(input('Comprimento do segundo segmento: '))
r3 = float(input('Comprimento do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos {r1}, {r2}, {r3} FORMAM UM TRIÂNGULO!')
else:
    print(f'Os segmentos {r1}, {r2}, {r3} NÃO FORMAM UM TRIÂNGULO!')