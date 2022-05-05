
def d1(x):
  S = int(x[0])*10 + int(x[1])*9 + int(x[2])*8 + int(x[3])*7 + int(x[4])*6 + int(x[5])*5 + int(x[6])*4 + int(x[7])*3 + int(x[8])*2
  if S%11==0 or S%11==1:
    return 0
  else:
    return 11-(S%11)

def d2(x):
  S = int(x[1])*10 + int(x[2])*9 + int(x[3])*8 + int(x[4])*7 + int(x[5])*6 + int(x[6])*5 + int(x[7])*4 + int(x[8])*3 + int(x[9])*2
  if S%11==0 or S%11==1:
    return 0
  else:
    return 11-(S%11)
    
def VCPF(x):
  if d1(x) == int(x[9]):
    if d2(x) == int(x[10]):
      return "Válido"
    else:
      return "ùltimo Inválido"
  else:
      return "penùltimo Inválido"
  
CPF=input("Digite seu CPF: ")
print(VCPF(CPF))