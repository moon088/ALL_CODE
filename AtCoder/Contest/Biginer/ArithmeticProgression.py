#A- Arithmetic Progression

A, B, D = map(int, input().split())

val = A
while val != B:
    print(val,end=" ")
    val += D
print(B,end=" ")

