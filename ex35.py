segmento1 = float(input("Segmento 1: "))
segmento2 = float(input("Segmento 2: "))
segmento3 = float(input("Segmento 3: "))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print("É possivel formar um triangulo")

else:
    print("Não é possivel formar um triangulo")

