import math

angulo = float(input("Digite o valor do ângulo em graus: "))

# Convertendo o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

# Calculando o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Exibindo os resultados
print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)
