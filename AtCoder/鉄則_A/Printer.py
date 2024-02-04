#A12 - Printer
'''
import math

N, K = map(int, input().split())
A = list(int(x) for x in input().split())

count = 0
count_sec = 0
lcm = math.lcm(*A)
#print(lcm,"公倍数", sum(A),"合計")
def countOutperiod(cn,sec,lcm):
    while cn  < K - sum(A):
        sec += lcm
        cn += sum(A)
    return cn,sec

def countInperiod(cn,sec):
    while cn < K:
        sec += 1
        for i in range(len(A)):
            if sec % A[i] == 0:
                cn += 1
    return sec


count ,count_sec= countOutperiod(count, count_sec, lcm)
#print(count,count_sec,"周期外")

count_sec = countInperiod(count, count_sec)
print(count_sec)

'''

# 答えが x 以下かを判定し、Yes であれば true、No であれば false を返す関数
def check(x, N, K, A):
	sum = 0
	for i in range(N):
		sum += x // A[i] # 「x÷A[i]」の小数点以下切り捨て

	if sum >= K:
		return True
	return False

# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索
# Left は探索範囲の左端を、Right は探索範囲の右端を表す
Left = 1
Right = 10 ** 9
while Left < Right:
	Mid = (Left + Right) // 2
	Answer = check(Mid, N, K, A)

	if Answer == False:
		Left = Mid + 1 # 答えが Mid+1 以上であることが分かる
	if Answer == True:
		Right = Mid # 答えが Mid 以下であることが分かる

# 出力（このとき Left=Right になっている）
print(Left)