#A13 - Close Pairs
import bisect

#bisectとbisect_rightは対象の値の最右のindex,bisect_leftは最左のindexを返す。二分探索で

N, K = map(int, input().split())
A = list(int(x) for x in input().split())
count = 0
for i in range(len(A)):
    count_i = bisect.bisect_right(A, A[i]+K)
    #print(i, count_i)
    count += count_i - i -1
print(count)


'''
def searchDiff_K(A, x, L, R):
    n = (R + L) // 2
    #print(L,R,n)
    if n == len(A)-1:
        return n
    elif A[n]-x <= K and A[n+1] - x > K:
        return n  
    elif A[n+1] - x  <= K:
        L = n + 1
        return searchDiff_K(A, x, L, R)
    elif A[n] - x > K:
        R = n - 1
        return searchDiff_K(A, x, L, R)
        

sum_comb = 0 
for i in range(len(A)):
    result = searchDiff_K(A, A[i], i, len(A)-1)
    if i == len(A)-1:
        print(sum_comb)
    else:
        sum_comb = sum_comb + result - i
    #print(sum_comb)
    '''