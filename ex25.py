nome = str(input("Digite o seu nome: ")).strip().lower()

if "silva" in nome:
    print("Seu nome tem SIM Silva!")

else:
    print("Seu nome NÃO tem Silva")

#Ou Assim
print("{}".format("silva" in nome))