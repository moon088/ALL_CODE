#D

N, M = map(int, input().split())
X = list(map(int, input().split()))


def cal_zoubun(now,next):
    Z_i = [0]*(N+1)
    start = min(now, next)
    end = max(now, next)
    dis = end-start
    Z_i[1] = dis
    Z_i[start] += N - 2*dis
    Z_i[end] = 2*dis-N
    
    return Z_i

Z = [0]*(N+1)
for i in range(M-1):
    result = cal_zoubun(X[i], X[i+1])
    print(result)
    for j in range(N+1):
        Z[j] = Z[j] + result[j] 
    #print(Z)

for i in range(len(Z)):
    if i == 0:
        continue
    else:
        Z[i] += Z[i-1]
#print(Z)

print(min(Z[1:]))
    
    











