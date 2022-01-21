numero = int(input("Digite um numero: "))
contador = soma = 0
flag = 999

while numero != flag:
    soma += numero
    contador += 1
    numero = int(input("Digite mais um numero: (999 para finalizar)"))

print(f"Voce digitou {contador} numeros e a soma dos valores é igual a {soma}")
