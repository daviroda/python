nums_extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
                'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
                'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
                'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
                'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
localizar = nums_extenso[num]
print(f'Você digitou o número {localizar}')