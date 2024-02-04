#D
N  = int(input())

S=[[None for x in range(N)] for y in range(N)]
P = []  #p1p2  [[x1,y1],[x2,y2]]
for i in range(N):
        S_i = input()
        for j in range(N):
            S[i][j] = S_i[j]
            if S[i][j] == "P":
                P.append([i,j])
print(S,P)


#p->プレイヤーあり,.->プレイヤーなし＃－＞障害物
#direct0,1,2,3が上右下左
def move_grid(x,y,direct):
    if direct ==0:
        if y-1>=0 and S[y-1][x] != "#":
            y -= 1 
    elif direct ==1:
        if x+1<N and S[y][x+1] != "#":
            x += 1
    elif direct ==2:
        if y+1 < N and S[y+1][x] !="#":
            y += 1
    else:
        if x-1>=0 and S[y][x] != "#":
            x -= 1 
    return x,y

def sousa_grid(x1,y1,x2,y2,direct):
    x1,y1 = move_grid(x1,y1,direct)
    x2,y2 = move_grid(x2,y2,direct)
    
    return x1,y1,x2,y2

INF = 10**6

for i in INF:
    x_dis = abs(P[0][0],P[1][0])
    y_dis = abs(P[0][1],P[1][1])
    