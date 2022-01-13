nome = str(input("Digite o seu nome completo: ")).strip()
print(f"Seu nome em maiusculo fica {nome.upper()}")
print(f"Seu nome em minuscula fica {nome.lower()}")
print("Seu nome tem {} letras!".format(len(nome) - nome.count(" ")))
primeiroNome = nome.split()
print(f"Seu primeiro nome é {primeiroNome[0]}, e tem {len(primeiroNome[0])}")

