from math import hypot
cateto_oposto = float(input("Qual o comprimento docateto oposto?: "))
cateto_adjacente = float(input("Qual o comprimento do cateto adjacente?: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa é {hipotenusa:.2f}")