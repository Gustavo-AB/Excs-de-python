from random import randint

print("\033[32m=\033[m" * 30)
print(" "* 8, "Par ou Impar")
print("\033[32m=\033[m" * 30)

contador_de_vitorias = 0

while True:
    numero_jogador = int(input("Digite um numero: "))
    par_ou_impar_jogador = str(input("Par ou impar [P/I]? "))

    numero_pc = randint(0,10)
    resultado = numero_jogador + numero_pc

    if resultado % 2 == 0 and par_ou_impar_jogador in "Pp":
        print(f"{resultado} voce escolheu PAR entao \033[32mGanhou\033[m essa Rodada!")
        contador_de_vitorias += 1

    if resultado % 2 == 0 and par_ou_impar_jogador in "Ii":
        print(f"{resultado} voce escolheu PAR entao \033[31mPerdeu\033[m essa Rodada!")
        break
    print("...")
    if resultado % 2 > 0 and par_ou_impar_jogador in "Ii":
        print(f"{resultado} voce escolheu IMPAR entao \033[32mGanhou\033[m essa Rodada!")
        contador_de_vitorias += 1

    if resultado % 2 > 0 and par_ou_impar_jogador in "Pp":
        print(f"{resultado} voce escolheu IMPAR entao \033[31mPerdeu\033[m essa Rodada!")
        break
    print("Vamos jogar novamente!...")
    print("-"*30)

print("-"*30)   
print(f"Você ganhou {contador_de_vitorias} rodadas!")
