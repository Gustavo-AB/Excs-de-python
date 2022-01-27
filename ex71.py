print("-="*15)
print(" "*5, "Caixa Eletronico")
print("-="*15)

valor = int(input("Digite o valor que deseja sacar: "))

cedula50 = 0
cedula20 = 0
cedula10 = 0
moeda1 = 0

while True:
    if valor >= 50:
        valor -= 50
        cedula50 += 1

    elif valor >= 20:
        valor -= 20
        cedula20 += 1

    elif valor >= 10:
        valor -= 10
        cedula10 += 1

    elif valor >= 1:
        valor -= 1
        moeda1 += 1

    elif valor == 0:
        break

    

print(f"{cedula50} nota(s) de RS50")
print(f"{cedula20} nota(s) de RS20")
print(f"{cedula10} nota(s) de RS10")
print(f"{moeda1} moeda(s) de RS1")


'''
cedula50 = 0
cedula20 = 0
cedula10 = 0
moeda1 = 0

while True:
    if valor >= 50:
        valor -= 50
        cedula50 += 1

    elif valor >= 20:
        valor -= 20
        cedula20 += 1

    elif valor >= 10:
        valor -= 10
        cedula10 += 1

    elif valor >= 1:
        valor -= 1
        moeda1 += 1

    elif valor == 0:
        break

    

print(f"{cedula50} nota(s) de RS50")
print(f"{cedula20} nota(s) de RS20")
print(f"{cedula10} nota(s) de RS10")
print(f"{moeda1} moeda(s) de RS1")
'''