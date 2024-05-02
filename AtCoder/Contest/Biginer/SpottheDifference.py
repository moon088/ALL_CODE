#B
import numpy as np

N = int(input())
A = np.empty((N,N), dtype=str)
B = np.empty((N,N), dtype=str)
for i in range(N):
    A[i]=list(input())    
for i in range(N):
    temp = list(input())
    for j in range(N):
        if A[i][j] != temp[j]:
            print(i+1,j+1)
            
    
