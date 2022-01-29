valores = list()
continuar = None

while True:
    numero = int(input("Digite um valor: "))

    if numero not in valores:
        valores.append(numero)

    else:
        print("Valores repetidos não serão adicionados!")

    continuar = str(input("Deseja continuar [S/N]? ")).strip().lower()

    if continuar in "Nn":
        break

print(f"Você digitou os valores {sorted(valores)}")
