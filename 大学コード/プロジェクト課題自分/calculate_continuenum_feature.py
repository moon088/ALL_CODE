def calculate_mahjong_stats(hand, target_color):
    # 手牌情報をリストに変換
    hand_list = list(hand)

    # 指定された色の牌を0に変更
    for i in range(len(hand_list)):
        if hand_list[i][0] == target_color:
            hand_list[i] = '0' + hand_list[i][1:]

    # 向聴数の計算
    shanten = calculate_shanten(hand_list)

    # 色の数の計算
    color_count = hand_list.count('0' + target_color)

    return shanten, color_count

def calculate_shanten(hand):
    # 向聴数の計算ロジックを実装
    # ここに向聴数を計算するコードを追加する

    # 仮の戻り値として -1 を返す
    return -1

# テスト用の手牌と指定色を設定
test_hand = "123m456p789s11234z"
target_color = "m"  # 例えば、萬子(manzu)の場合は"m"を指定

# 向聴数と色の数を計算
shanten, color_count = calculate_mahjong_stats(test_hand, target_color)

# 結果の出力
print(f"向聴数: {shanten}")
print(f"{target_color}の数: {color_count}")
