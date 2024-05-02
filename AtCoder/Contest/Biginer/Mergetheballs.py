#C

N = int(input())
def merge(stack,newel):
    while stack:
        temp = stack.pop()
        if temp != newel:
            stack.append(temp)
            stack.append(newel)
            return stack
        else:
            newel +=1
    stack.append(newel) 
    return stack

stack=[]
line = list(map(int,input().split()))
for i in range(N):
    a = line[i]
    #print(stack)
    stack = merge(stack,a) 
print(len(stack))

