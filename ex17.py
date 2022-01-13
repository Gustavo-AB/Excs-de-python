from math import hypot

catetoOposto = float(input("Digite a medida do cateto oposto: "))
catetoAdjacente = float(input("Digite a medida do cateto adjacente: "))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f"A medida da hipotenusa equivale a {hipotenusa:.2f}!")
