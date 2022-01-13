import math

angulo = float(input("Digite o angulo que voce deseja: "))


seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"Essas são as medidas do angulo {int(angulo)}, são\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")
