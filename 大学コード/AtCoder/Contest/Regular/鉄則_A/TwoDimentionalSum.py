#A08 - Two Dimentional Sum

H, W = map(int, input().split())
X = []

#H行W列の行列をXに格納
for i in range(H):
    row = list(map(int, input().split()))
    X.append(row)

Q = int(input())

for q in range(Q):
    A, B, C, D = map(int, input().split())
    rect = 0
    for i in range(A-1, C):
        for j in range(B-1, D):
            rect += X[i][j]
    print(rect)
    













