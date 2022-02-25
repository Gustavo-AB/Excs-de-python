def cabecalho():
    print(f'\033[35;49;7m~'*30)
    print(f'{"SISTEMA DE AJUDA PYHELP":^30}')
    print(f'~'*30+'\033[m')

def mostrarHelp(comando):
    return help(comando)



cores = {
    'verde': '\033[32m',
    'fim': '\033[m'
}

cor = (
    cores['verde'],
    cores['fim']
)

cabecalho()

while True:
    func_ou_libs = str(input(f"{cores['verde']}Funcao{cores['fim']} ou {cor[0]}biblioteca{cor[1]}: ")).strip().lower()

    if func_ou_libs == "fim":
        break

    else:
        mostrarHelp(func_ou_libs)
        cabecalho()

