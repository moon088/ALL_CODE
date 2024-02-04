#C
INF = 10**6
N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


#まずaの最大値を求める
max_a = INF
for i in range(N):
    if A[i] == 0:#0除算のため分岐
        continue
    max_a = min(max_a, Q[i]//A[i])
#print(max_a)

max_ab = 0
for j in range(max_a+1):
    max_b = INF
    for i in range(N):
        if B[i] == 0:
            continue
        max_b = min(max_b, (Q[i]-A[i]*j)//B[i])
    #print(max_b)
    max_ab = max(max_ab, max_b+j)
print(max_ab)
