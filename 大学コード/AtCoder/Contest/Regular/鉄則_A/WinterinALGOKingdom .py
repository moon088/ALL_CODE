#A08 - Winter in ALGO Kingdom Winter in ALGO Kingdom 

'''
H, W, N = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]
Z = [[0]*(W) for _ in range(H)]

for i in range(N):
    a,b,c,d = A[i][0],A[i][1],A[i][2],A[i][3]
    for j in range(a-1, c):
        for k in range(b-1, d):
            Z[j][k] += 1

for row in Z:
    for column in row:
        print(column, end=' ')
    print()
    '''
    
H, W, N = map(int,input().split())

cells = [[ 0 for _ in range(W+2) ] for _ in range(H+2)]

for _ in range(N):
    A, B, C, D = map(int,input().split())
    cells[A][B] += 1
    cells[C+1][D+1] += 1
    cells[A][D+1] -= 1
    cells[C+1][B] -= 1



for y in range(1,H+1):
    for x in range(1,W+1):
        cells[y][x] = cells[y][x]-cells[y-1][x-1]+cells[y-1][x]+cells[y][x-1]

for y in range(1,H+1):
    for x in range(1,W+1):
        print(cells[y][x], end=" ")
    print()









