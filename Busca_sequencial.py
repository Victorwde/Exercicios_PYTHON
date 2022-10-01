def busca_sequencial(x, seq):
    flag = 0
    posi = []
    for i in range(len(seq)):
        if seq[i] == x:
            flag = flag + 1
            posi.append(i)
    if flag != 0:
        return 'Existe na base de dados'+str(flag)+'e esta localizado na posição '+str(posi)
    return 'Não existe na base de dados'

V =[27,25,98,25,40,4,25,28,35] 
N =int(input('Digite o numero que procura: '))
print(busca_sequencial(N,V))





'''def busca_sequencial(x, seq):
    for i in range(len(seq)):
        if seq[i] == x:
            return 'Existe na base de dados e esta localizado na posição '+str(i)
    return 'Não existe na base de dados'

V =[27,25,98,25,40,4,25,28,35] 
N =int(input('Digite o numero que procura: '))
print(busca_sequencial(N,V))'''





'''def busca(x,seq):
    flag=0
    for i in range(len(seq)):
        if seq[i] == x:
            flag=flag+1
    if flag!=0:
        return "Existe(m) "+str(flag)+" ocorrencia(s)"
    else:    
        return "Não Existe" 

V=[27,25,98,25,40,4,5,28,4,35]
N=int(input("Digite o número que procura")
)
*************
def busca(x,seq):
    flag=0
    for i in range(len(seq)):
        if seq[i] == x:
            flag=flag+1
    if flag!=0:
        return "Existe(m) "+str(flag)+" ocorrencia(s)"
    else:    
        return "Não Existe" 

V=[27,25,98,25,40,4,5,28,4,35]
N=int(input("Digite o número que procura"))'''