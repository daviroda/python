segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento3 + segmento1 and segmento3 < segmento2 + segmento1:
    if segmento1 == segmento2 == segmento3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')