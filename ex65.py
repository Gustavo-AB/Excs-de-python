
numero = contador = menor_numero = maior_numero = media = 0
continuar_ou_nao = ""

while continuar_ou_nao != "n":
    numero = int(input("Digite um numero: "))
    continuar_ou_nao = str(input("Deseja continuar [S/N]?")).strip().lower()
    media += numero
    contador += 1
    
    if contador == 1:
        maior_numero = menor_numero = numero

    else:
        if numero > maior_numero:
            maior_numero = numero

        if numero < menor_numero:
            menor_numero = numero

media /= contador

print(f"Você digitou {contador} numeros, a media de todos eles é igual a {media:.2f}\nO maior numero digitado foi{maior_numero}\nE o menor foi {menor_numero}")
