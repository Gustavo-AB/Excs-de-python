numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite mai um numero: "))
numero4 = int(input("Digite o último numero: "))

numeros = (numero1, numero2, numero3, numero4)

print(f"O numero 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O numero 3 apareceu pela primeira vez na posicao {numeros.index(3)+1}")

else:
    print("O numero 3 não apareceu")
    
print(f"Numeros pares: ", end=" ")

for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=" ")

