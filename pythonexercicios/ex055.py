maior = float(0)
menor = float(0)
for p in range(1, 6):
    peso = float(input(f'Me diga o peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if  peso < menor:
            menor = peso
print(f'O maior KG foi {maior} \nO menor KG foi {menor}')