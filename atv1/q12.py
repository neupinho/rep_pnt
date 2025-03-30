turmas = int(input("Quantidade de turmas: "))
total_alunos = 0

for i in range(turmas):
    alunos = int(input("Quantidade de alunos na turma " + str(i + 1) + ": "))
    total_alunos += alunos
    if alunos > 40:
        print("Turma", i + 1, "tem mais de 40 alunos!")
media = total_alunos / turmas
print("Média de alunos por turma:", media)
