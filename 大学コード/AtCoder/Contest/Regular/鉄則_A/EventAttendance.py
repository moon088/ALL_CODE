# A07 - Event Attendance

#入力ごとにすべて配列に1を加算していくアルゴリズムはオーダーやばい。
#入力からRインクリメント、Lデクリメントした配列計算してから参加者計算する
D = int(input())
N = int(input())

attendance = [0] * (D+1)
for i in range(N):
    L_i, R_i = map(int, input().split())
    attendance[L_i-1] -= 1
    attendance[R_i] += 1


for d in range(D, 0, -1):
    attendance[d-1] += attendance[d]

for i in range(1, D+1):
    print(attendance[i])
    




