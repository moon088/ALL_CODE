#A

T = int(input())
S =[]
for i in range(T):
    S_i = list(map(int, input().split()))
    S.append(S_i)
#print(S)


def isContain(N,A,B):
    X = N - A
    if X < 0:
        print("No")
        return
    #X行X列でB考える 
    if X == 0:
        if B == 0:
            print("Yes")
            return
        else:
            print("No")
            return
    necessary_B = B // X
    if (B% X) != 0:
        necessary_B += 1
    #print(necessary_B)
    
    if necessary_B - A <= 1:
        necessary_row = necessary_B + A
    else:
        diff = necessary_B - A -1
        necessary_row = necessary_B + A + diff
    #print(necessary_row)
    
    if necessary_row <= N:
        print("Yes")
        return 
    else:
        print("No")
        return

#isContain(S[1][0],S[1][1],S[1][2])
for i in range(T):
    S_i = S[i]
    #print(S_i)
    isContain(S_i[0],S_i[1],S_i[2])
