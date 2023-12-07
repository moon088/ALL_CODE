def calculate_riichi_feature(hand):
    tehai = hand[0]
    huuro = hand[1]

    if(len(huuro) == 0):
        #リーチできる
        return 1
    else:
        #リーチできない
        return 0
    

#test
hand = [['m1','m1','s1','s9','p1','p1','z1','s1','s1','s1','s9','s9','s9'],[]]
result = calculate_riichi_feature(hand)
print(result)
