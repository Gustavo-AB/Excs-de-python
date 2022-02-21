def cabecalho(titulo, qnt=30):
    print("="*qnt)
    print(f'{titulo:^{qnt}}')
    print("="*qnt)

def divisor(qnt=30):
    print("-"*qnt)

def area(largura, comprimento):
    area = largura * comprimento

    print(f'A area de um terrenno {largura} x {comprimento} é de {area}m²')


cabecalho("Cálculo de Área")

largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))

divisor()

area(largura, comprimento)
