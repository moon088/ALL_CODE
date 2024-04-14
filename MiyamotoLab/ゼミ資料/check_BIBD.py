#課題(1)
#部分集合族を入力した際にそのデザインがBIBDであるかの判定
import numpy as np

#すべてのブロックサイズがkであるか判定
def check_blocksize(subset_family):
        block_size = len(subset_family[0])
        for i in range(len(subset_family)):
            if block_size != len(subset_family[i]):
                return False ,block_size
        return True ,block_size
        

#点集合の要素Xと要素数vを計算
def cal_pointnum(subset_family):
    unique_points = []  # リストの初期化
    
    for subset in subset_family:
        for point in subset:
            if point not in unique_points:
                unique_points.append(point)

    return unique_points, len(unique_points)

#結合行列の作成
def make_incedenceMatrix(subset_family):
    X, v = cal_pointnum(subset_family) #点集合と点の数を格納
    b = len(subset_family) #ブロック数
    incidence_matrix = [[0] * b for _ in range(v)] #結合行列の初期化
    
    #結合行列にデザインの情報を格納
    for point_index in range(len(X)):
        for block_index in range(len(subset_family)):
            if(X[point_index] in subset_family[block_index]):
                incidence_matrix[point_index][block_index] = 1
    
    #print(np.array(incidence_matrix))
    return np.array(incidence_matrix)


#会合数が常に一定(λ)であるか判定
def cal_numberOfMeeting(subset_family):
    M = make_incedenceMatrix(subset_family) #結合行列をMとする
    processed_M = M @ M.T  #M * M転置を計算
    #print(processed_M)
    
    #MM_t[i][j]がi=jならばr,i!=jならばλとなるか判定
    r = processed_M[1][1]  #出現回数rの初期化
    meetings = processed_M[1][2] #会合数λの初期化
    check_bool = [True, True] #出現回数と会合数の判定の初期化

    for i in range(len(processed_M)):
        for j in range(len(processed_M[i])):
            if i == j: #rが一致しているか判定
                if r != processed_M[i][j]:
                    check_bool[0] = False
            else:
                if meetings != processed_M[i][j]:
                    check_bool[1] = False
        return check_bool, r, meetings

#入力を受け付ける処理
def input_array():
    print("2次元配列を入力してください。")
    print("要素をスペースで区切り、行ごとにEnterを押してください。")
    print("最後に';'をつけてEnterを押すと入力が終了します.")

    input_lines = []
    while True:
        try:
            line = input()
            if line.endswith(';'):
                line = line.rstrip(';')
                input_lines.append(line)
                break
            input_lines.append(line)
        except EOFError:
            break

    # 入力されたテキストを2次元配列に変換
    two_dimensional_array = []
    for line in input_lines:
        row = [int(x) for x in line.split()]
        two_dimensional_array.append(row)
   
    return two_dimensional_array


#メイン関数
def check_BIBD(subset_family):
    all_parameter = [0] * 5 #パラメータの初期化
    
    #ブロックサイズについて
    isBlocksize = check_blocksize(subset_family)[0]
    if not isBlocksize:    
        return False, 1
    #ブロックサイズの格納
    all_parameter[3] = check_blocksize(subset_family)[1]
    
    #点集合について
    all_parameter[0] = cal_pointnum(subset_family)[1]
    X = cal_pointnum(subset_family)[0]
    
    #会合数について
    isMeetings = cal_numberOfMeeting(subset_family)[0][1]
    if not isMeetings:
        return False, 2
    all_parameter[4] = cal_numberOfMeeting(subset_family)[2]
    all_parameter[2] = cal_numberOfMeeting(subset_family)[1]

    #ブロック数計算
    b = len(subset_family)
    all_parameter[1] = b
    #v>k>=2の確認
    if not (all_parameter[0] > all_parameter[3] >= 0):
        return False, 3
    
    return True, all_parameter[0], all_parameter[1], all_parameter[2], all_parameter[3], all_parameter[4]
    
def make_output(result):
    if result[0]:
        print("入力されたデザインはBIBDの条件を満たしています。以下がパラメータです")
        print("点の個数:" ,result[1],"ブロック数:" ,result[2],
            "出現回数:",result[3], "ブロックサイズ:", result[4], 
            "会合数:", result[5])
    else:
        if result[1] == 1:
            print("ブロックサイズが一定でないためBIBDではありません")
        elif result[1] == 2:
            print("会合数が一定でないためBIBDではありません")
        elif result[1] == 3:
            print("v > k >= 2を満たしていません")        
        else:
            print("何かエラーが起きてます")
            
            
#test:check_blocksize()
#print(check_blocksize(test1))

#test:cal_pointnum()
#print(cal_pointnum(test1))
 
#test:cal_numberOfMeeting()
#print(cal_numberOfMeeting(test2))

#test:cal_numberOfMeeting()
#print(cal_numberOfMeeting(test2))

#test:cal_numberOfMeeting()
#print(cal_numberOfMeeting(test2))

#test:check_BIBD()
#check_BIBD(test2)


if __name__ == "__main__":
    subset_family = input_array()
    #print(subset_family)
    result = check_BIBD(subset_family)
    make_output(result)

    