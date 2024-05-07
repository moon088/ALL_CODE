class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x): # パス圧縮
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y): # サイズの大きい方が合併後の根となる
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


H, W = map(int, input().split())
S = [list(input().rstrip()) for _ in range(H)]
N = H * W
# print(S)
T = [[0] * W for _ in range(H)]

dij = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            T[i][j] = -1
            continue
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if S[ni][nj] == "#":
                T[i][j] = 1

uf = UnionFind(N)
for i in range(H):
    for j in range(W):
        if T[i][j] == -1 or T[i][j] == 1:
            continue
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if T[ni][nj] == 0:
                uf.union(i*W+j, ni*W+nj)
                
#print(uf.parents)
cnts = [set() for _ in range(N)]
#print(cnts)
for i in range(H):
    for j in range(W):
        ij = i*W+j
        if T[i][j] == -1:
            continue
        x = uf.find(ij)
        cnts[x].add((i,j))
        if T[i][j] == 0:
            for di, dj in dij:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if T[ni][nj] == -1:
                    continue
                cnts[x].add((ni, nj))
        #print(cnts)
#print(uf.parents)
ans = 0
for ij in range(N):
    # print(ij, uf.find(ij), cnts[ij])
    if len(cnts[ij]) > ans:
        ans = len(cnts[ij])
print(ans)
# print(cnts)

        
            

