distancia = float(input("Qual a distancia da sua viagem em Km? "))

if distancia <= 200:
    valor = distancia * 0.50
    print(f"O valor a pagar pela viagem é de R${valor:.2f}!")

else:
    valor = distancia * 0.45
    print(f"O valor a pagar pela viagem é de R${valor:.2f}!")