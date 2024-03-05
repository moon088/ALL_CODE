#B

N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    S,T=map(int,input().split())
    while A[i]>=S:
        A[i] -=S
        A[i+1]+=T
print(A[N-1])