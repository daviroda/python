# Função Área
def área(largura, comprimento):
     a = largura * comprimento
     print(f'A área de um terreno {largura}X{comprimento} é de {a}m².')

# Principal
print('Controle de Terrenos')
print('-' *40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
