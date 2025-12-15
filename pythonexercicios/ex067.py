while True:
    tabuada = int(input('Digite um numero para ver sua tabuada: '))
    if tabuada < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{tabuada} X {c} = {tabuada*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO!! Volte sempre')
