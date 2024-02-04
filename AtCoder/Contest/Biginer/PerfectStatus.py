#C

N = int(input())
A = list(map(int, input().split()))

start = 0
passenger = 0

for i in range(len(A)):
    passenger += A[i]
    if passenger < 0:
        start += (-1)*passenger
    passenger = max(0, passenger)
    #print(start, passenger)
print(passenger)




