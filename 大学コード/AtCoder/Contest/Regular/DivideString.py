#A

T = int(input())
S =[]
for i in range(T):
    N = int(input())
    S_i = list(map(str, input()))
    S.append(S_i)
#print(S)

def isCut(top,end,S):
    if top > end:#単語がない
        return True,end
    if end >= len(S)-1: #文字列のけつに到達
        return (False,0)
    if ord(S[top]) < ord(S[end+1]): #大きかったら切れる
        return (True, end)
    elif ord(S[top]) > ord(S[end+1]): #切れない
        return (False,0)
    else:#先頭じゃ判断できない
        return isCut(top+1,end+1,S)
        
        
        
#now_wordには対象単語のindex入れる
def cut_str(now_word,S):
    top = now_word[0]
    end = now_word[len(now_word)-1]
    if now_word[end] == len(S)-1: #けつに到達 
        return False, end
    result = isCut(top, end, S)
    if result[0]: #now_wordで切れる
        end = result[1]
        return True ,end
    else:  #切れないときはnow_wordに取り込む
        now_word.append(end+1)  
        return cut_str(now_word, S)
            

def isCut_S(S):
    for i in range(1,len(S)+1):
        count = 0  #全体で切ったことがあるか01
        first_word = [x for x in range(i)] #初期単語を0~iまでとする
        #print(first_word)
        result = cut_str(first_word, S)
        #print(first_word,result)
        if result[0]: #単語で切れる(最後まで行ってない)なら次やる
            print("Yes")
            return
        elif not result[0] and result[1] == len(S)-1: #きれず、後ろまで行ってない
            continue
        else: #切れず、後ろまで行ってない   
            top = result[1] + 1
            cut_str([top],S) #次の単語へと行く
    print("No")
    
for i in range(T):
    S_i = S[i]
    #print(S_i)
    isCut_S(S_i)
            
            