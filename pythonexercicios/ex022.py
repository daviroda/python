
nome = str(input('Digite o seu nome completo: ')).strip()
Upnome = nome.upper()
Lonome = nome.lower()
Quantcaracteries = len(nome)-nome.count(' ')
Primeironome = nome.split()[0]
Caracteriesprimeironome = len(Primeironome)

print("Analisando seu nome...")
print(f'Seu nome em maiúsculas é {Upnome}\n Seu nome em minúsculas é {Lonome}\n Seu nome tem ao todo {Quantcaracteries} letras \n Seu primeiro nome é {Primeironome} e tem {Caracteriesprimeironome} letras')