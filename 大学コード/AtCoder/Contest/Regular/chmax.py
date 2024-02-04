#B

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
B = [int(x+1) for x in range(N)]
#Pはリストようそが１～N
#P,B与えられたときAになるかbool
def sousa(P,B):
    i = 0
    while i < len(B):
        if A == B:
            return True
        index = B[i] -1
        if B[i] < P[index]:
            B[i] = P[index]
            i = 0
        else:
            i += 1
    return False


def generate_permutations(size):
    numbers = list(range(1, size + 1))
    permuted_lists = list(permutations(numbers))
    return permuted_lists

result = generate_permutations(N)


count = 0
for i in range(len(result)):
    #print(result[i],B)
    if sousa(result[i],B):
        count += 1
print(count)
        

    
