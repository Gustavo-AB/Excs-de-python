from lib.interface.interface import *
from lib.arquivom.arquivo import *
from time import sleep

arquivo = './ex115/cursoemvideo.txt'

if not arquivoExixste(arquivo):
    criarArquivo(arquivo)
    
while True:
    interface()
    escolha = escolhaOpc()
    
    if escolha == 1:
        verPessoas(arquivo)
        sleep(1)

    if escolha == 2:
        linha()
        while True:
            nome = str(input('Digite o nome: ')).strip()
            if nome == '':
                print('\033[31mO Nome Não Pode Ser Vazio!\033[m')
            elif nome.isdigit():
                print('\033[31mO Nome Não Pode Ser Um Número!\033[m')
            else:
                break
        sleep(0.5)
        while True:
            try:
                idade = int(input('Digite a idade: '))
            except (ValueError, TypeError):
                print('\033[31mValor de Idade Inválido!\033[m')
                continue
            else:
                break

        cadastrar(arquivo, nome, idade)
        sleep(1)
        print('\033[32mCadastro Realizado Com Sucesso!\033[m')
        sleep(0.5)

    if escolha == 3:
        sair()
        break
