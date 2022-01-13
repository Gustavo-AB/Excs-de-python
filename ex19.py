from random import choice

primeiroAluno = str(input("Primeiro Aluno: "))
segundoAluno = str(input("Segundo Aluno: "))
terceiroAluno = str(input("Terceiro Aluno: "))
quartoAluno = str(input("Quarto Aluno: "))

alunoEscolhido = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

print(f"O aluno escolhido foi {choice(alunoEscolhido)}!")
