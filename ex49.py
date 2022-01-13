tabuada = int(input("Digite um numero para ver a  sua tabuada: "))

for contador in range(1, 11):
    print(f"{tabuada} x {contador:2} = {tabuada*contador}")
    contador += 1
