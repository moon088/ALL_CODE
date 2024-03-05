#C

H, W, N= map(int, input().split())
T = list(map(str,input()))

Map = [ list(input()) for _ in range(H)]
T.reverse()

def move(y,x,situate):
    if situate=="U":
        if y-1 >= 0 and Map[y-1][x]==".":
            return True,y-1,x
        else:
            return False,y-1,x
    if situate=="R":
        if x+1 < W and Map[y][x+1]==".":
            return True,y,x+1
        else:
            return False,y,x+1

    if situate=="D":
        if y+1 < H and Map[y+1][x]==".":
            return True,y+1,x
        else:
            return False,y+1,x
    if situate=="L":
        if x-1 >=0 and Map[y][x-1]==".":
            return True,y,x-1
        else:
            return False,y,x-1

count=[]
for i in range(H):
    for j in range(W):
        count.append([i,j])
#print(count)

for i in range(len(T)):
    j=0
    while j < len(count):
        result=move(count[j][0],count[j][1],T[i])
        if result[0]:
            count[j][0]=result[1]
            count[j][1]=result[2]
            j+=1
        else:
            x=count.pop(j)
            #print(x)
print(count)