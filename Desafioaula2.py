import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
def raiz2(num,menor,maior): 
    media=(menor+maior)/2 
    rm=media*media 
    if rm==num: 
        return media 
    elif rm>num: 
        return raiz2(num,menor,media) 
    else: 
        return raiz2(num,media,maior)
def raiz(num,menor,maior): 
    r1=menor*menor 
    r2=maior*maior 
    if r1==num: 
        return menor 
    elif r2==num: 
        return maior 
    elif num>r1 and num<r2: 
        return raiz2(num,menor,maior) 
    else: 
        return raiz(num,menor+1,maior+1)
def RQ(N): 
    return raiz(N,0,1)

N = float(input("Digite o valor:"))
print(RQ(N))