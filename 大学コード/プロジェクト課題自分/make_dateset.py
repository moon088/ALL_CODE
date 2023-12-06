import normal_xianting
import calculate_titoi_feature
import calculate_kokushimusou_shanten


hand = ['m1','m1','m4','m7','p1','p2','p5','p6','s1','s5','s7','s7','s9']

#通常手向聴数変換
def normal_convert(hand):
    numbers = [8, 8, 9, 12, 15, 16, 17, 18, 19, 20, 23, 23, 23, 26, 1, 8, 5]
    hand_numbers = numbers[:14]
    mahjong_hand = normal_xianting.convert_to_mahjong_hand(hand_numbers)
    normal_result = normal_xianting.xiangting(normal_xianting.shoupai(mahjong_hand))
    return normal_result
#test
#result = normal_convert(hand)
#print(result)


#七対子向聴数変換
def titoi_convert(hand):
    titoi_result = calculate_titoi_feature.calculate_titoitu_shanten(hand)
    titoi_dataset = [0] * 7
    titoi_dataset[titoi_result] = 1
    return titoi_dataset
#test
#print(titoi_dataset(hand))

#国士無双向聴数変換
def kokusi_convert(hand):
    kokusi_result = calculate_kokushimusou_shanten.calculate_kokushimusou_shanten(hand)
    kokusi_dataset = [0] * 14
    kokusi_dataset[kokusi_result] = 1
    return kokusi_dataset
#test
#print(kokusi_convert(hand)) 




















