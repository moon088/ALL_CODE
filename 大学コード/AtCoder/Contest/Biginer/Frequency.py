#B
S = str(input())

A = [0]*26
for i in range(97, 123):
    moji = chr(i)
    count = S.count(moji)
    A[i-97]= count
#print(A)

result = A.index(max(A))
print(chr(97+result))

