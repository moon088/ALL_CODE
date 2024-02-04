#A11 - Binary Search1

N, X = map(int, input().split())
A = list(int(x) for x in input().split())

def binary(array,temp):
    n = (len(array) // 2) 
    #print(n,X,array[n])
    
    if array[n] == X:
        print(temp+n+1)
    elif array[n] > X:
        binary(array[:n],temp)
    else:
        binary(array[n+1:],temp+n+1)

binary(A,0)

'''
N, X = map(int, input().split())
A = list(int(x) for x in input().split())

def binary(array):
    print(array.index(X)+1)
binary(A)'''