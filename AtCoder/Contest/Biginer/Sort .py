#C

N = int(input())
A = list(map(int,input().split()))
i=0
count=0
memory = []
while True:
    if i == N:
        break
    if A[i] != i+1:
        temp = A[A[i]-1]
        memory = memory + [[temp, A[i]]] 
        #print(memory)
        A[A[i]-1] = A[i]
        A[i] = temp
        count+=1
    else:
        i+=1
        
print(count)
for i in memory:
    print(i[0],i[1])


