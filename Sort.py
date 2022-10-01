def sort(L): 
	for I in range(len(L)): 
		for X in range(len(L)-1): 
			if L[X] > L[X + 1]: 
				L[X + 1], L[X] = L[X], L[X + 1] 
                
                    
V=[58,54,3,655,7,14,2,5,8,9]

print(V)
sort(V)
print(V)





'''def sort(L): 
  for I in range(len(L)): 
    houvetroca="N"
    for X in range(len(L)-1): 
      if L[X] > L[X + 1]: 
        L[X + 1], L[X] = L[X], L[X + 1] 
        houvetroca="S"
    print(L)
    if houvetroca=="N":
      break

V=[1,2,3,4,5,6,7,8,9,10]
print(V)
print("*************")
sort(V)'''