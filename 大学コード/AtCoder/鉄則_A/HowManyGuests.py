#A06 -How Many Guests

'''
N, Q = map(int, input().split())
A_N = list(int(x) for x in input().split())

question = []
for i in range(Q):
    Q_i = list(int(x) for x in input().split())
    question.append(Q_i)

for i in range(len(question)):
    L_i = question[i][0]
    R_i = question[i][1]
    #print(L_i,R_i)
    count_visitor = 0
    for j in range(L_i - 1, R_i):
        count_visitor += A_N[j]
    print(count_visitor)
    count_visitor = 0
'''

N, Q = map(int, input().split())
A_N = list(int(x) for x in input().split())

#1~k日までの来場者合計を配列に格納してオーダー減らす。
#このときもオーダー減らすためにi-1使う
visitor_kdays = [0]
for i in range(1, len(A_N) + 1):
    visitor_kdays.append(visitor_kdays[i-1] +A_N[i-1])  
#print(visitor_kdays)

for i in range(Q):
    L, R = map(int, input().split())
    count_visitor = visitor_kdays[R] - visitor_kdays[L-1]
    print(count_visitor)








