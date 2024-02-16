#C - Divide and Divide
'''
N = int(input())
board = [N]
count = 0
    
    
while len(board)!=0:
    val = board.pop(0)
    inf = val //2
    sup = (val+1)//2
    count += val
    #print(count,val,inf,sup)
    if inf >=2:
        board.append(inf)
    if sup >= 2:
        board.append(sup)
print(count)'''

N = int(input())
memo = {}
def f(n):
  if n == 1: return 0
  if n in memo.keys():
    return memo[n]
  memo[n] = n + f(n//2) + f((n+1)//2)
  return memo[n]

print(f(N))