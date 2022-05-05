def UFCPF(y):
    if y[8]=="1":
        return "DF, GO, MS, MT e TO"
    elif y[8]=="2":
        return "AC, AM, AP, PA, RO e RR"
    elif y[8]=="3":
        return "CE, MA e PI"
    elif y[8]=="4":
        return "AL, PB, PE, RN"
    elif y[8]=="5":
        return "BA e SE"
    elif y[8]=="6":
        return "MG"
    elif y[8]=="7":
        return "ES e RJ"
    elif y[8]=="8":
        return "SP"
    elif y[8]=="9":
        return "PR e SC"
    else:
        return "RS"

def d(x,ini,fim):
  sum=0
  mult=10
  for i in range(ini,fim):
    sum = sum + (int(x[i]) * mult)
    mult=mult-1
  if sum%11==0 or sum%11==1:
    return 0
  else:
    return 11-(sum%11)

def VCPF(x):
    if x[0]==x[1]==x[2]==x[3]==x[4]==x[5]==x[6]==x[7]==x[8]==x[9]==x[10]:
        return "Inválido por Números Iguais"
    else:
        if d(x,0,9) == int(x[9])and d(x,1,10) == int(x[10]):
            print(UFCPF(CPF))
            return "Válido"
        else:
            return "Inválido"
    


CPF=input("Digite seu CPF: ")
print(VCPF(CPF))
