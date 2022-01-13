from colorama import init, Fore, Back, Style
init(autoreset=True)

print("="*15,"LOJAS G.A.B","="*15)

valorDaCompra = float(input("Qual o valor da compra? "))
print("Escolha as formas de pagamento")
print("[1]-A VISTA no DINHEIRO ou CHEQUE 10% de DESCONTO!\n[2]-A VISTA no CARTÃO DE CRÉDITO 5% de DESCONTO!\n[3]-Em 2x no CARTÃO!\n[4]-Em 3x ou MAIS com 20% de JUROS!")
escolhaDoCliente = int(input("Qual opção você deseja? "))

while escolhaDoCliente < 1 or escolhaDoCliente > 4:
    print(Fore.RED+"Opção invalida! Tente novamente!")
    escolhaDoCliente = int(input("Qual opção você deseja? "))

print("-" * 30)

if escolhaDoCliente == 1:
    novoValorDaCompra = valorDaCompra - (valorDaCompra * 10 / 100)

    print(f"Compra no valor de R${valorDaCompra:.2f}\nPagamento a vista no DINHEIRO ou DÉBITO 10% de DESCONTO!")
    print(f"Sub-Total: R${valorDaCompra:.2f} - 10%")
    print(f"Total: R${novoValorDaCompra:.2f}")

elif escolhaDoCliente == 2:
    novoValorDaCompra = valorDaCompra - (valorDaCompra * 5 / 100)

    print(f"Compra no valor de R${valorDaCompra:.2f}\nPagamento a VISTA no CARTÃO DE CRÉDITO 5% de DESCONTO!")
    print(f"Sub-Total: R${valorDaCompra:.2f} - 5%")
    print(f"Total: R${novoValorDaCompra:.2f}")

elif escolhaDoCliente == 3:
    parcelas = valorDaCompra / 2

    print(f"Compra no valor de R${valorDaCompra:.2f}\nPagamento em 2x no CARTÃO!")
    print(f"Sub-Total: R${valorDaCompra:.2f} em 2x de R${parcelas:.2f}")
    print(f"Total: R${valorDaCompra:.2f} em 2x de R${parcelas:.2f}")

elif escolhaDoCliente == 4:
    juros = valorDaCompra * 20 / 100
    valorDaCompra += juros
    parcelas = int(input("Quantas parcelas? ")) 
    novoValorDaCompra = (valorDaCompra / parcelas)

    print(f"Compra no valor de R${valorDaCompra-juros:.2f}\nPagamento em {parcelas}x no CARTÃO com 20% de JUROS!")
    print(f"Sub-Total: R${valorDaCompra-juros:.2f} em {parcelas}x de R${(valorDaCompra-juros)/parcelas:.2f} + 20% de JUROS")
    print(f"Total: R${valorDaCompra:.2f} em 5x de R${novoValorDaCompra:.2f}")
