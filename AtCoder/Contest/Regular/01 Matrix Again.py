#A
N,M = map(int,input().split())
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
out=set()
s=set()
for i in range(M):
    A,B = map(int, input().split())
    out.add((A,B))
    s.add((A+B)%N)
#print(s)
#print((0-2)%7)
temp=0
while len(s) < M:
    s.add(temp)
    temp+=1
#print(s)        
print(N*M)
for total in s:
    for row in range(1,N+1):
        column = (total-row)%N
        if column == 0:
            column=N
        out.add((row,column))
        

for i in out:
    print(i[0],i[1])
#for i in out:
#    x=i[0]
#    y=i[1]
#    board[x][y]=1
#for i in range(1,N+1):
 #   for j in range(1,N+1):
#        print(board[i][j],end=" ")
#    print()
