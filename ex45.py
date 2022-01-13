from colorama import init, Back, Fore, Style
import  random 
from time import sleep
init(autoreset=True)

print("="*15,"JOKENPO!!!","="*15)
print("Suas opções: ")
print("[0]-Pedra\n[1]-Papel\n[2]-Tesoura")

escolhaDoJogador = int(input("Qual a sua escolha? "))
opcoes = ["Pedra", "Papel", "Tesoura"]
escolhaDoPc = random.randint(0, 2)

sleep(1)
print("-"*30)

if escolhaDoPc == 0:
    if escolhaDoJogador == 0:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.BLUE + "Essa rodada deu em empate")

    elif escolhaDoJogador == 1:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.GREEN + "Parabéns! Você ganhou!")

    elif escolhaDoJogador == 2:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.RED + "Infelizmente você perdeu!")

elif escolhaDoPc == 1:
    if escolhaDoJogador == 0:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.RED + "Infelizmente você perdeu!")

    elif escolhaDoJogador == 1:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.BLUE + "Essa rodada deu em empate")

    elif escolhaDoJogador == 2:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.GREEN + "Parabéns! Você ganhou!")

elif escolhaDoPc == 2:
    if escolhaDoJogador == 0:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.GREEN + "Parabéns! Você ganhou!")

    elif escolhaDoJogador == 1:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.RED + "Infelizmente você perdeu!")

    elif escolhaDoJogador == 2:
        print(f"Você escolheu {opcoes[escolhaDoJogador]}!")
        print(f"O computador escolheu {opcoes[escolhaDoPc]}!")
        print(Fore.BLUE + "Essa rodada deu em empate")

if escolhaDoJogador > 2:
    print("Essa opção não exixte!")
    print(Fore.RED + "Infelizmente você perdeu!")

print("-"*30)
