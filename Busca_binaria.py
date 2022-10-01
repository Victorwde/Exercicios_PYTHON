def pesquisa_binaria(A, item): 
	esquerda=0
	direita = len(A) - 1 
	while esquerda <= direita: 
		meio = (esquerda + direita) // 2 
		if A[meio] == item: 
			return meio 
		elif A[meio] > item: 
			direita = meio - 1 
		else: 
			esquerda = meio + 1 
	return "Não encontrado"

L=[1,5,6,9,17,25,27,60,98,99]
print(pesquisa_binaria(L,90))