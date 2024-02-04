#D 未

H, W, K = map(int, input().split())
S = []
for i in range(H):
    S_i = list(input())
    S.append(S_i)
#print(S)


#. -> 〇

#まずはK候補を調べる
#status=0-> 行横
Z = [[None for x in range(W)] for y in range(H)]
#print(Z)

def isbatu(x,y):
    if S[y][x] == "x":
        return -1
    elif S[y][x] == "o":
        return 1
    else:
        return 0
    
#i,jはｋ連続可能か
def isKrenzoku(x,y,status):
    count=0
    step = 0
    while isbatu(x,y)>= 0 and count < K:
        if isbatu(x,y)==1:
            step +=1
        count += 1
        if count == K:
            return (True,step)
        if status==0:
            x += 1
        elif status == 1:
            y += 1
        if y >= H or x >= W:
            return (False,step)
    return (False,step)
        
max_step = 0
for y in range(H):
    for x in range(W):
        #print(x,y)
        result1 = isKrenzoku(x,y,0)
        result2 = isKrenzoku(x,y,1)
        #print(result1,result2)
        if result1[0] or result2[0]:
            Z[y][x] = max(result1[1],result2[1]) #両方
            max_step = max(max_step,Z[y][x])
#print(Z)
if max_step==0:
    print(-1)
else:
    print(K-max_step)

