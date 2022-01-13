numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite mais um numero: "))
numero3 = float(input("Digite só mais um numero: "))
maiorNum = 0
menorNum = 9999999999999999999999999
numeros = [numero1, numero2, numero3]

for numero in numeros:
    if numero > maiorNum:
        maiorNum = numero

    if numero < menorNum:
        menorNum = numero

print(30*"-")
print(f"O MAIOR numero é {maiorNum:.1f}\nE o MENOR é {menorNum:.1f}")
