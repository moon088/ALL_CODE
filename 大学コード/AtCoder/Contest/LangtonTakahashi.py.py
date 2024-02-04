#B
import numpy as np
H, W, N = map(int, input().split())
Z = [[0 for x in range(W)] for y in range(H)]


#上、右、下、左を0,1,2,3
#行をy,列をx

def move_grid(x,y,direct):
    if direct==0:
        y = (y-1)%H
    elif direct == 1:
        x = (x+1)%W
    elif direct ==2:
        y = (y+1)%H
    else:
        x = (x-1)%W
    return x,y
        
def sousa_grid(x, y, direct):
    if Z[y][x] == 0: #0が白1が黒
        Z[y][x] = 1
        direct = (direct + 1) % 4
        x, y = move_grid(x,y,direct)
        return x,y,direct
    else:
        Z[y][x] = 0
        direct = (direct -1) % 4
        x, y = move_grid(x,y,direct)
        return x,y,direct

#初期化
direct = 0
x,y = 0,0
for i in range(N):
    x,y,direct = sousa_grid(x,y,direct)
    

for x in range(H):
    for y in range(W):
        if Z[x][y]==0:
            print(".", end="")
        else:
            print("#", end="")
    print()
