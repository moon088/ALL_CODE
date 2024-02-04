#A16- Dungeon1

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 動的計画法
dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N+1):
	dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])


print(dp[N])

'''
def min_route(i,count):
    print(i,count)
    if i == N-1:
        count += A[N-2]
        return count
    elif i == N:
        return count
    elif A[i-1] + A[i] > B[i-1]:
        count += B[i-1]
        return min_route(i+2,count) 
    else:
        count += A[i-1]
        return min_route(i+1,count)
result = min_route(1,0)
print(result)
'''