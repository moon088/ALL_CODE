#A05 -Three Cards

N, K = map(int ,input().split())

count = 0
for i in range(1,N+1):
    for j in range(1,N + 1):
        k = K - i - j #３回ループよりも格段にオーダー少ない
        if 0 < k <= N: 
            count += 1
print(count)
