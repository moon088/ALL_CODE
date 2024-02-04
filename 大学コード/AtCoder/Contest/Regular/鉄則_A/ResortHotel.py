#A10 - Resort Hotel
'''
N = int(input())
A = list(int(x) for x in input().split())
D = int(input())
X = []

for i in range(D):
    X_i = [0] * 2
    X_i[0], X_i[1] = map(int, input().split())
    X.append(X_i)
    
for i in range(len(A)):
    A[i] = (A[i] , i)

sorted_A = sorted(A, reverse=True)
#print(sorted_A)

for i in range(D):
    L = X[i][0] -1
    R = X[i][1] -1
    for j in range(len(sorted_A)):
        #print(L,R,sorted_A[j][1])
        if 0 <= sorted_A[j][1] < L-1 or R < sorted_A[j][1] <= N:
            print(sorted_A[j][0])
            break
            '''  
N = int(input())
A = [0] + list(map(int, input().split()))
D = int(input())
L = [0]*(D+2)
R = [0]*(D+2)

for i in range(1, D+1, 1):
  L[i], R[i] = map(int, input().split())

P = [0]*(N+2)
Q = [0]*(N+2)

for i in range(1, N+1, 1):
  P[i] = max(A[i], P[i-1])
  Q[N+1-i] = max(A[N+1-i], Q[N+1-i+1])

for i in range(1, D+1, 1):
  print(max(P[L[i]-1], Q[R[i]+1]))