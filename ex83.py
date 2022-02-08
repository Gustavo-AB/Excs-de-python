expressao = str(input("Digite uma expressao: "))
pilha = list()

for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")

    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Expressao valida")

else:
    print("Expressao Invalida")
