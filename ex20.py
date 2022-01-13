from random import shuffle

primeiroAluno = str(input("Primeiro Aluno: "))
segundoAluno = str(input("Segundo Aluno: "))
terceiroAluno = str(input("Terceiro Aluno: "))
quartoAluno = str(input("Quarto Aluno: "))

alunoEscolhido = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(alunoEscolhido)

print(f"A ordem dos alunos sera essa:\n{alunoEscolhido}!")
