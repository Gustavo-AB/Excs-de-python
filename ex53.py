palavra = str(input("Digite uma palavra ou frase: ")).strip().upper()
palavras = palavra.split()
palavrasJuntas = ''.join(palavras)

print('-'*30)
print(palavrasJuntas)

if palavrasJuntas[::-1] == palavrasJuntas:
    print(f"A palavra {palavra} ao contrario fica {palavrasJuntas[::-1]}")
    print("Portanto \033[32mÉ UM POLINDROMO\033[m")

else:
    print(f"A palavra {palavra} ao contrario fica {palavrasJuntas[::-1]}")
    print("Portanto \033[31mNÃO É UM POLINDROMO\033[m")

print('-'*30)
