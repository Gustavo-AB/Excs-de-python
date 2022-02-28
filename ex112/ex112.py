from utilidadesCeV.moeda import moeda
from utilidadesCeV.dado import dado

valor = dado.leiaDinheiro("Digite um numero: ")
moeda.resumo(valor, 10, 10)
