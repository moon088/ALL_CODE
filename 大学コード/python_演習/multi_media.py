import numpy as np
print("HELLO!")

sequence = ['I' , 'have', 'a', 'pen']
for word in sequence:
    print("word:", word)
    for char in word:
        print("",char)

for num in range(5,20,2):
    print(num)
    if num == 11:
        break
print(list(range(10)))    

for i in range(10):
    print(i)

char_list = ["a","b","c","d","e","f","g"]

for i in  char_list:
    print("")
    for j in range(7):  #文字列変換
        #temp += char + str(j) + " " で足していくのもあり
        print(i + str(j) + " ", end="") #改行なし
print("")

gohan = 10 #モジュールスコープ
def decrement(gohan):
    gohan -= 1
    print("Local gohan is" , gohan) #ローカルスコープの出力
    return gohan
decrement(gohan)
print("Module scope gohan is" , gohan)#モジュールスコープの出力
#ローカルからモジュールスコープの変更はできない
#関数内でグローバル変数を変更するのなら関数の返戻値を代入すべき

gohan = decrement(gohan)
print("Module scope gohan is", gohan)

