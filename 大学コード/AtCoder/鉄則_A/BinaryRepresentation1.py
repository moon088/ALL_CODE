#A04 -Binary Representation1
'''
N = int(input())

binaryNum = []
count = 0

while N > 1:
    div = N // 2
    mod = N % 2
    binaryNum += str(mod)
    N = div 
binaryNum += str(N)    

while len(binaryNum) < 10:
    binaryNum += "0"

#リストの逆順変換(新たに生成はreversed(binaryNum))
binaryNum.reverse()
#リストの各要素結合
joined_binary = ''.join(binaryNum)
print(joined_binary)
'''



#別解もっと簡単
N = int(input())
ans = ""
for i in range(10):
    ans = str(N // (2 ** i) % 2) + ans 
print(ans)    

