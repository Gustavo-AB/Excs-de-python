from fileinput import close
from lib.interface.interface import cabecalho
from time import sleep


def arquivoExixste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()

    except Exception as erro:
        return False
    
    else:
        return True

def criarArquivo(nome):
    arquivo = open(nome, 'wt+')
    arquivo.close()

def verPessoas(arq):
    cabecalho('PESSOAS CADASTRADAS')
    sleep(1)
    try:
        with open(arq, 'r') as arquivo:
            arquivoF = arquivo.readlines()
            

    except (TypeError, FileNotFoundError,):
        print('Erro na leitura do arquivo')

    else:
        for linha in arquivoF:
            dados = linha.split(';')
            fm = len(dados[0]) - 20
            es = '.'*fm
            print(f'{dados[0]:<30}{dados[1]:3>}')
        
    finally:
        arquivo.close()
        

def cadastrar(arq, nome, idade):
    with open(arq, 'a') as arquivo:
        arquivo.write(f'{nome};')
        arquivo.write(f'{idade} anos\n')

    arquivo.close()


def sair():
    cabecalho('SAINDO DO SISTEMA...')