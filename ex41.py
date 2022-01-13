from datetime import date

anoNascimento = int(input("Digite o ano de nascimento do atleta: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if anoNascimento < 10:
    print(f"Categoria MIRIN!")

elif anoNascimento < 15:
    print("Categoria INFANTIL!")

elif anoNascimento < 20:
    print("Categoria JUNIOR!")

elif anoNascimento < 26:
    print("Categoria SENIOR!")

else:
    print("Categoria MASTER!")
    
    