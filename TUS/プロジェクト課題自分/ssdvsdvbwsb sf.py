def calculate_colors_feature(hand):
    if len(hand) != 13:
        return "error"
    count_2to8 = 0
    for hai in hand:
        if hai != 'm1' and hai != 'm9' and hai != 's1' and hai != 's9' and hai != 'p1' and hai != 'p9' and hai != 'z1' and hai != 'z2' and hai != 'z3' and hai != 'z4' and hai != 'z5' and hai != 'z6' and hai != 'z7':
            count_2to8 += 1
    return count_2to8

#test
#result = calculate_colors_feature(hand)
#print("2から8の枚数:",result)

def countOf2To8_convert(hand):
    count_result = calculate_colors_feature(hand)
    count_dataset = [0] * 15
    count_dataset[count_result] = 1
    return count_dataset
#test
hand = ['m1','m1','s1','s9','p1','p1','z1','z1','z3','z4','z5','z6','z7']
print(countOf2To8_convert(hand)) 