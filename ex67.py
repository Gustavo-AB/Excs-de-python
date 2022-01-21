while True:
    numero = int(input("Deseja ver a tabuada de qual numero? "))
    if numero < 0:
        break

    for contador in range(1, 11):
        print(f"{numero} x {contador:2} = {numero*contador}")

print("Programa encerrado\nVolte sempre!")
