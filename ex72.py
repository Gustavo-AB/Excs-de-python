numeros_extensos = (
    "zero", "um ", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)



while True:
    numero = int(input("Digite um numero: "))
    if numero >= 0 and numero <= 20:
        break

    print("Opcao invalida tente novamente")

print(f"Voce digitou o numero {numeros_extensos[numero]}!")

