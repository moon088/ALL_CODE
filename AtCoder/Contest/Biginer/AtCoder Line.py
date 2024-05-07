#A
N,X,Y,Z = map(int, input().split())

if X > Y:
    if Y < Z < X:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
else:
    if X < Z < Y:
        print("Yes")
        exit()
    else:
        print("No")
        exit()


