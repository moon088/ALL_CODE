#B

N,Q = map(int,input().split())
T = map(int, input().split())
Array = [1]*N


#この分岐を使わずに解くなら、Array[i-1]= 1-Array[i-1]で更新できる！！
for i in T:
    if Array[i-1] == 1:
        Array[i-1] = 0
    else:
        Array[i-1] = 1

count = 0
for i in Array:
    if i == 1:
        count +=1
        
print(count)

