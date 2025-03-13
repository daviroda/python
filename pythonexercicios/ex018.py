from math import sin, cos, tan, radians

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f"O ângulo de {ângulo} tem o SENO de {seno:.2f} \n "
      f"O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f} \n"
      f"O ângulo de {ângulo} tem o TANGENTE de {tangente:.2f}")