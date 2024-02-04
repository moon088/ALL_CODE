#C

N = int(input())
A = list(map(int, input().split()))

index_A=[]
for i in range(N):
    index_A.append([A[i],i+1])
index_A.sort()
#print(index_A)

def binary(a,L,R):
    #print(a,L,R)
    mid = (R+L)//2 
    #print(mid)
    if a == index_A[mid][0]:
        return mid
    if a < index_A[mid][0]:
        return binary(a,L,mid-1)
    else:
        return binary(a,mid+1,R)
    
sousa = -1
for i in range(N):
    #print(sousa,"---------")
    result = binary(sousa,0,N-1)
    print(index_A[result][1], end=" ")
    sousa = index_A[result][1]

