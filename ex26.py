frase = str(input("Digite uma frase: ")).strip().lower()

print("A letra A aparece",frase.count("a"), "vezes na frase")
print("A letra A aparece pela PRIMEIRA vez na posição",frase.find("a")+1)
print("A letra A aparece pela ULTIMA vez na posicao",frase[-1].find("a")+len(frase))
#Ou assim
print("A letra A aparece pela ULTIMA vez na posicao",frase.rfind("a")+1)

