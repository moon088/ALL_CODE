#D
from sortedcontainers import SortedSet, SortedList, SortedDict

N, K = map(int, input().split())
P = list(map(int, input().split()))
newP = [x-1 for x in P]
Q = [0]*N
for i in range(N):
    Q[newP[i]] = i
#print(newP,Q)

def judge():
    # x個で連続Kが達成できるか
    L = []
    for i in range(K):
        L.append(Q[i])
    S = SortedSet(L)
    #print(L,S)
    now = S[K-1] - S[0]
    mn = now
    for i in range(K, N):
        S.discard(Q[i-K])
        S.add(Q[i])
        now = S[K-1] - S[0]
        if now < mn:
            mn = now
    return mn

ans = judge()
print(ans)




