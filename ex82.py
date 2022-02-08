numeros = list()
numeros_pares = list()
numeros_impares = list()

while True:
    numeros.append(int(input("Digite um numero: ")))
    continuar_ou_nao = str(input("Deseja continuar [S/N]? "))

    if continuar_ou_nao in "Nn":
        break

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

    else:
        numeros_impares.append(numero)

print(f"A lista completa é {numeros}")
print(f"A lista de numeros pares é {numeros_pares}")
print(f"A lista de numeros impares é {numeros_impares}")
