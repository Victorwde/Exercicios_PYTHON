turma = []
flag = 1
while flag == 1:
    linha = []
    linha.append(input("Nome: "))
    linha.append(float(input("AV1: ")))
    linha.append(float(input("AV2: ")))
    turma.append(linha)
    flag = int(input("Deseja adicionar mais um aluno ?:(0-Não|1-Sim)\n"))
for i in range(len(turma)):
    print("Nome:",turma[i][0],"AV1:",turma[i][1],"AV2:",turma[i][2])
    print("MEDIA ==",turma[i][1]+turma[i][2]/2)