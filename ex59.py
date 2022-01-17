primeiro_valor = float(input("Digite o primeiro valor: "))
segundo_valor = float(input("Digite o segundo valor: "))
soma = 0
multiplicacao = 0
maior = 0

print("-"*30)
print("O que você deseja fazer?")
print("[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos números\n[5]-Sair do programa")
escolha = int(input("Qual a seu escolha? "))

while escolha != 5:
    print("-"*30)
    if escolha < 1 or escolha > 5:
        print("Escolha ínvalida! Tente novamente")
        escolha = int(input("Qual a seu escolha? "))
    
    else:
        if escolha == 1:
            soma = primeiro_valor + segundo_valor
            print(f"A soma de {primeiro_valor:.0f} e {segundo_valor:.0f} é {soma:.0f}")
            escolha = int(input("O que mais você deseja fazer? "))

        elif escolha == 2:
            multiplicacao = primeiro_valor * segundo_valor
            print(f"A multiplicação de {primeiro_valor:.0f} x {segundo_valor:.0f} é {multiplicacao:.0f}")
            escolha = int(input("O que mais você deseja fazer? "))

        elif escolha == 3:
            if primeiro_valor == segundo_valor:
                print("Os valores são iguais!")
                escolha = int(input("O que mais você deseja fazer? "))


            elif primeiro_valor > segundo_valor:
                maior = primeiro_valor
                print(f"O maior valor digitado foi {maior:.0F}!")
                escolha = int(input("O que mais você deseja fazer? "))

            else:
                maior = segundo_valor
                print(f"O maior valor digitado foi {maior:.0f}!")
                escolha = int(input("O que mais você deseja fazer? "))

        elif escolha == 4:
            primeiro_valor = float(input("Digite o primeiro novo valor: "))
            segundo_valor = float(input("Digite o segundo novo valor: "))
            print("O que você deseja fazer?")
            print("[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos números\n[5]-Sair do programa")
            escolha = int(input("O que você deseja fazer? "))

print("Finalizando o programa...")
print("Até breve!")