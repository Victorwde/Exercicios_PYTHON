turma = []
flag = 1

while flag == 1:
    linha = []
    linha.append(input("Nome: "))
    linha.append(float(input("AV1: ")))
    linha.append(float(input("AV2:")))
    turma.append(linha)
    flag = int(input("Deseja adicionar mais um aluno ?(0-Não\1-Sim)\n"))
    print(turma)
for i in range(len(turma)):
    for j in range(len(turma[i])):
        print(turma[i][j])
