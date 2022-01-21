print("="*30)
print("Sequiencia de Fibbonahci")
print("="*30)

contador = 3
termos = int(input("Digite quantos termos voce quer mostrar: "))
termo1 = 0
termo2 = 1

print(f"{termo1} {termo2} ", end="")
while contador <= termos:
    termo3 = termo1 + termo2
    print(f"{termo3}", end=" ")
    termo1 = termo2
    termo2 = termo3
    contador += 1
