from datetime import date

ano = int(input("Digite  um ano para saber se é bissesto ou não! 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    print(f"{ano} é SIM um ano bissesto!")

else:
    print(f"{ano} NÃO é um ano bissesto")
