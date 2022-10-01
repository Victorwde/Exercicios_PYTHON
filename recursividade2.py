#0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 
def SF(qtd):
  PN = 0
  SN = 1
  for i in range(qtd):
    print(PN)
    R = PN + SN
    PN = SN
    SN=R
  return 

SF(10)