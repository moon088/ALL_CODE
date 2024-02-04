#A15 - Compression

N = int(input())
A = list(map(int, input().split()))

added_ind = [(A[i], i) for i in range(len(A))]


added_ind.sort()
#print(added_ind)
j = 1

for i in range(len(added_ind)):
    if i == 0:
        added_ind[0] = added_ind[0] + (1,)
        j += 1
    elif added_ind[i][0] == added_ind[i-1][0]:
        added_ind[i] = added_ind[i] + (j-1,)
    else:
        added_ind[i] = added_ind[i] + (j,)
        j += 1
#print(added_ind)

B = [0]*len(A)
for i in range(len(A)):
    B[added_ind[i][1]] = added_ind[i][2] 
for i in range(len(B)):
    print(B[i], end = " ")


