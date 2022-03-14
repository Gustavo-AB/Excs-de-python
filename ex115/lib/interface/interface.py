from time import sleep

def linha(tamanho=40):
    print('~'*tamanho)

def cabecalho(msg, tamanho=40):
    linha()
    print(f'{msg:^{tamanho}}')
    linha()

def interface():
    cabecalho('MENU PRINCIPAL')

    print(f'\033[33m1\033[m - \033[35mVer Pessoas Cadastradas\033[m ')
    print(f'\033[33m2\033[m - \033[35mCadastrar nova Pessoa\033[m ')
    print(f'\033[33m3\033[m - \033[35mSair do Sistema\033[m ')

    linha()

def escolhaOpc():
    while True:
        try:
            escolha = int(input('\033[33mSua escolha: \033[m'))

            if escolha > 3 or escolha < 1:
                print(f'\033[31mErro! Digite Apenas Uma das Opções Acima!')
                escolha  = 0
                continue

        except (TypeError, ValueError):
            print(f'\033[31mErro Digite Uma Opção Válida')
            continue

        else:
            return escolha

