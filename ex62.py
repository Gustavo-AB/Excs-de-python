numero_da_pa = int(input("Digite qual vai ser o termo da PA: "))
razao_da_pa = int(input("Digite qual vai ser a Razao da PA: "))
pa = numero_da_pa
contador = 0

print(f"{numero_da_pa} -", end=" ")

while contador < 9:
    pa = numero_da_pa + razao_da_pa

    if contador < 8:
        print(f"{pa} -", end=" ")

    else:
        print(f"{pa} FIM")

    numero_da_pa += razao_da_pa
    contador += 1
