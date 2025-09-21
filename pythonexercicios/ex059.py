from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('-=-='*10)
    print('''    [1] somar 
    [2] multiplicar  
    [3] maior 
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção ? '))
    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma dos valores {primeiro_valor} + {segundo_valor} é {soma}')
    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f'O resultado de {primeiro_valor} X {segundo_valor} é {multiplicacao}')
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
        else:
            maior = segundo_valor
        print(f'Entre os valores {primeiro_valor} e {segundo_valor} ao maior valor {maior}')
    elif opcao == 4:
        print('Quais são os números novamente: ')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim do programa! Volte sempre!')
