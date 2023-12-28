#課題(2)
#差集合の条件を満たしているか判定
import numpy as np
from itertools import product


#入力を受け付ける処理
def input_array():
    print("群の位数を入力してください。直積群の場合はそれぞれの群の位数を入力してください")
    print("最後に';'をつけてEnter押すと入力が終了します")
    print("例:Z_4×Z_4ならば4 4;と入力")
    
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
        
    order = [int(x) for x in input_lines[0].split()]
    
    if len(order) >= 2:
        print("集合を入力してください")
        print("要素をスペースで区切り、行ごとにEnterを押してください。")
        print("最後に';'をつけてEnterを押すと入力が終了します.")

        input_lines_sets = []
        while True:
            try:
                line_sets = input()
                if line_sets.endswith(';'):
                    line_sets = line_sets.rstrip(';')
                    input_lines_sets.append(line_sets)
                    break
                input_lines_sets.append(line_sets)
            except ValueError:
                print("無効な入力です")

        # 入力されたテキストを2次元配列に変換
        two_dimensional_array = []
        for line in input_lines_sets:
            row = [int(x) for x in line.split()]
            two_dimensional_array.append(row)
        #print(two_dimensional_array)
        return two_dimensional_array, order
    elif len(order) == 1:
        print("集合を１行で入力してください")
        print("要素をスペースで区切り、最後に;をつけてEnterを押すと入力が終了します")
        try:
            input_line = input()
            
            # ';'が含まれているか確認
            if ';' in input_line:
                # ';'を取り除き、空白で分割して整数に変換
                numbers = [[int(x)] for x in input_line.rstrip(';').split()]
                
                return numbers, order
            else:
                print("入力が不正です")
        
        except ValueError:
            print("無効な入力です")
    else:
        print("正しく位数を入力してください")

#入力の不備やDが有限アーベル群の部分集合であるか判定
def check_input(differenceset, order):
    dim = len(order)

    #入力した位数の剰余類の要素であるか確認
    for i in range(len(order)):
        for element_index in range(len(differenceset)):
            if order[i] < differenceset[element_index][i]:
                print("入力された集合の要素は指定された有限アーベル群の部分集合ではありません")
                return 
        if len(differenceset[element_index]) != dim:
            print("入力された要素の中に指定した次元と異なるものがあります。")
            return

#組み合わせ求める関数
def generate_combinations(input_list):
    ranges = [range(x) if x > 1 else [0] for x in input_list]

    # 全組み合わせを生成
    combinations = list(product(*ranges))
    #print(combinations)
    
    # 生成した組み合わせを出力
    result_list = []
    for combo in combinations:
        flat_combo = list(combo)
        result_list.append(flat_combo)
        
    return result_list


#入力された各剰余類の下で各集合要素の減算を行う
def cal_substruct_inMod(differenceset, order):
    cal_substruct = [[0] *  len(order) for _ in range(len(differenceset)*(len(differenceset)-1))]
    element_num = len(differenceset) * len(differenceset)
    count = 0
    
    for element_i in range(len(differenceset)):
        for element_j in range(element_i+1,len(differenceset)):
            #２要素の減算(与えられた方の中で)
            for index in range(len(order)):
                quotient, result = divmod(differenceset[element_i][index] - differenceset[element_j][index], order[index])
                #print(differenceset[element_i][index], differenceset[element_j][index],result)
                cal_substruct[count][index] = result
            count += 1
            
    #逆方向で減算        
    for element_i in range(len(differenceset)):
        for element_j in range(element_i+1,len(differenceset)):        
            
            for index in range(len(order)):
                quotient, result = divmod(differenceset[element_j][index] - differenceset[element_i][index], order[index])
                #print(differenceset[element_i][index], differenceset[element_j][index],result)
                cal_substruct[count][index] = result
            count += 1
            
    return cal_substruct

#計算した集合が入力した位数の有限加法アーベル群の部分集合か判定
def isSuperset(all_Element_G, cal_Element_G, order):
    set1 = set(map(tuple, cal_Element_G))
    set2 = set(map(tuple, all_Element_G))
    
    return set1.issuperset(set2)


 #v個の要素が何回計算した集合(cal_Element_G)に含まれているか計算
def count_meetings(all_Element_G, cal_Element_G, v):
    count_meetings = [0] * (v-1) #0元除く
    for i in range(len(cal_Element_G)):
        for j in range(len(all_Element_G)):
            if cal_Element_G[i] == all_Element_G[j]:
                count_meetings[j] += 1
    
    return count_meetings

def check_differenceset():
    differenceset, order = input_array()
    #print(differenceset,order)
    check_input(differenceset, order)
    
    #vの計算
    v = np.prod(order)
    #print(v)
    
    #入力集合の濃度
    cardinaryOfSet = len(differenceset)
    
    #群Gの全要素を準備
    all_Element_G =  generate_combinations(order)
    #差集合の定義より0元以外の要素が対象
    #入力した位数の次元個の0を持つタプルを除いたアーベル群    
    zero_list = [0] * len(order)
    all_Element_G_non0 = [row for row in all_Element_G if row != zero_list]
    #print(all_Element_G_non0)
    
    #入力された各剰余類の下で各集合要素の減算を行う
    cal_Element_G = cal_substruct_inMod(differenceset, order)
    #print(cal_Element_G)
    
    
    #入力された集合Dの任意の要素x,yに対して{x-y}が群G\{0}の部分集合となっていないとき
    if not isSuperset(all_Element_G_non0, cal_Element_G, order):
        #λ回Gの要素が出現するどころか一回も出現していない要素がある
        print("入力した集合はdifferenceSetではありません")
        return
    
    #v個の要素が何回計算した集合(cal_Element_G)に含まれているか計算
    meetings = count_meetings(all_Element_G_non0, cal_Element_G, v)
    #print(meetings)
    
    #λを計算し、一定なら性質満たす
    meet = meetings[0]  #会合数の初期化
    for i in range(len(meetings)): 
        if meetings[i] != meet:
            print("計算した結果群Gの要素がちょうどλ回出てこないためdifferenceSetではありません")
            return
    
    #differenceSetの性質をすべて満たしているときの出力
    print("入力された集合はdifferenceSetです")
    return
    
    
check_differenceset()
