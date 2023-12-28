import check_BIBD
import check_differenceSet

#多次元配列の足し算D+gをする
def add_elements(array, value, order):
    result = []

    if isinstance(array[0], list):
        # 2次元の場合
        result = [[(element[i] + value[i]) % order[i] for i in range(len(element))] for element in array]
    else:
        # 1次元の場合
        result = [element + value for element in array]

    return result


def make_BIBD(result):
    #他のファイルからの返戻地を格納
    v = result[1]
    differenceSet = result[4]
    order = result[5]
    all_Element_G = result[6]
    #print(differenceSet)
    #print(all_Element_G)
    #print(v)
    
    #演算
    symmetric_BIBD = []
    for i in range(v): #D+gをgの個数(v個)分ループ
        added_element = add_elements(differenceSet, all_Element_G[i], order)
        symmetric_BIBD.append(added_element)

    return symmetric_BIBD
    
    
def toDifferenceSetFromBIBD():
    result = check_differenceSet.check_differenceset()
    if not result[0]: #そもそも差集合でない
        print("入力された集合はdifferenceSetではありません")
        return 
    
    #BIBDを計算
    BIBD = make_BIBD(result)
    #print(BIBD)
    
    #課題1使用してBIBDか判定
    isBIBD = check_BIBD.check_BIBD(BIBD)
    check_BIBD.make_output(isBIBD)
    return

toDifferenceSetFromBIBD()