
numero = int(input("Digite o numero: "))
razao = int(input("Digite a razao: "))
contador = 0
termos = 10
while contador < termos:
    print(f"{numero}", end=" ")
    numero += razao
    contador += 1
    if contador == termos:
        termos += int(input("\nQuantos termos a mais voce deseja ver? "))
    if termos == 0:
        print("Acabou")
print(f"Progressao finalizada com {contador} termos mostrados")

