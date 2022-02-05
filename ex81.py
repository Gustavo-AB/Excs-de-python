numeros = list()
contador = 0

while True:
    numeros.append(int(input("Digite um valor: ")))
    contador += 1
    continuar_ou_nao = str(input("Deseja continuar [S/N]? "))

    if continuar_ou_nao in "Nn":
        break

print(f"Ao todo foram {contador} numeros digitados!")
numeros.sort(reverse=True)
print(f"A lista em ordem decrescente fica assim {numeros}")

if numeros.count(5) >= 1:
    print("O valor 5 faz parte da lista!")
      
else:
    print("O valor 5 não faz parte da lista! ")
