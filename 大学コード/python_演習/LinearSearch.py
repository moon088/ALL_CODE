#A02 - Linear Search

#二つの入力
rangeN,match  = map(int, input().split()) 
input_2 = list(map(int, input().split()))
count_match = 0

#リストに含まれているかbool型
result = match in input_2
#print(result) あとtrueならyesでいい。

#これが自分が書いたやつ
for i in range(rangeN):
    if(match == input_2[i]):
        print("Yes")
        exit() #強制終了
print("No")











