segmento1 = float(input("Primeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    if segmento1 == segmento2 and segmento1 == segmento3:
        print("É possivel formar um triangulo EQUILATERO!")

    elif segmento1 == segmento2 or segmento2 == segmento3 or segmento3 == segmento1:
        print("É possivel formar um triangulo ESCALENO!")

    elif segmento1 != segmento2 and segmento2 != segmento3 and segmento3 != segmento1:
        print("É possivel formar um triangulo ISOCELES!")

else: 
    print("Não é possivel formar um triangulo!")
