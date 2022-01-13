numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: ")) 
numero6 = int(input("Digite o sexto numero: "))

numeros = [numero1, numero2, numero3, numero4, numero5, numero6]
soma = 0
quantidadeDenumerosPares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma += numero
        quantidadeDenumerosPares += 1

print(f"Você informou {quantidadeDenumerosPares} numeros pares e a soma de todos os eles é igual a {soma}!")

############# OU ASSIM ####################
soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input(f"Digite o {c} valor: "))
    if numero % 2 == 0:
        soma += numero
        contador += 1

print(f"Você informou {contador} numeros pares e a soma de todos os eles é igual a {soma}!")
