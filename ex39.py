from datetime import date

anoDeNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento
saldo = idade - 18

if idade < 18:
    saldo = 18 - idade
    anoDeAlistamento = anoAtual + saldo
    print(f"Com {idade} anos seu sera daqui a {saldo} anos!")
    print(f"Seu alistamento sera em {anoDeAlistamento}")


elif idade > 18:
    anoDeAlistamento = anoAtual - saldo
    print(f"Com {idade} anos você já devera ter se alistado a {saldo} anos ")
    print(f"Seu alistamento foi em {anoDeAlistamento}")
    

else:
    print(f"Com {idade} anos você deve se alistar IMEDIATAMENTE!")
