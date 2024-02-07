#A19 - Knapsack1
N, W = map(int, input().split())

cost = [0]*N
val = [0]*N
for i in range(N):
    cost[i],val[i] = map(int, input().split())
    

def Knapsack_dp(cost, val, limit):
    dp_table = [[0 for _ in range(limit+1)] for _ in range(N)]
    
    for j in range(limit+1):
        if j >= cost[0]:
            dp_table[0][j] = val[0]
    
    for i in range(N):
        for j in range(limit+1):
            if j < cost[i]:
                dp_table[i][j] = dp_table[i-1][j]
            else:
                temp_choice = dp_table[i-1][j-cost[i]] + val[i]
                dp_table[i][j] = max(temp_choice, dp_table[i-1][j])
    #print(dp_table)
    return dp_table[len(cost)-1][limit]

result = Knapsack_dp(cost, val, W)
print(result)
'''
別解
n,W=map(int,input().split())
dp=[0]*(W+1)
for i in range(n):
    w,v=map(int,input().split())
    for j in range(W,w-1,-1):dp[j]=max(dp[j-w]+v,dp[j])
print(dp[W])


'''






