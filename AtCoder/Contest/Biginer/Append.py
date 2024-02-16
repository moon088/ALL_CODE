#B - Append

Q = int(input())
A = []

for i in range(Q):
    num, x = map(int, input().split())
    if num == 1:
        A.extend([x])
        #print(A)
        
    else:
        index = len(A)-x
        print(A[index])
        




