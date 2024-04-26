#D
N,M = map(int,input().split())
Rerationship = [[] for _ in range(N+1)]
print(Rerationship)
fincount=0


    
def isMakeFriends(A,B):
    count=0
    for i in range(len(Rerationship[A])):
        C = Rerationship[A][i]
        if C != B and C not in Rerationship[B]:
           count+=1
    return count 


for i in range(M):
    A,B = map(int,input().split())
    Rerationship[A].append(B)
    Rerationship[B].append(A)
    print(Rerationship)
    fincount += isMakeFriends(A,B)
    fincount += isMakeFriends(B,A)
print(fincount)
    
