def print_updated_hands(initial_hand, discards):
    # 手牌を数値のリストに変換
    hand_tiles = initial_hand.split(',')
    # 結果の手牌を出力するためのリスト
    updated_hands = []

    for discard in discards:
        # T（ツモ）の場合、その牌を手牌に加える
        if discard.startswith('T'):
            tile = discard[1:]
            hand_tiles.append(tile)  # ツモ牌を追加
            updated_hands.append(','.join(hand_tiles))  # 現在の手牌を記録
        # D（打）の場合、その牌を手牌から取り除く
        elif discard.startswith('D'):
            tile = discard[1:]
            if tile in hand_tiles:
                hand_tiles.remove(tile)  # 打牌を取り除く

    # 各ツモの後の手牌を出力する
    for hand in updated_hands:
        print(hand)

# 例えば、以下のような出力が得られた場合の手牌を表示する
initial_hand = "91,124,49,2,59,44,100,32,77,63,29,27,76"
discards = ['T135', 'D2', 'U51', 'E118', 'V41', 'F73', 'W93', 'G37', 'T115', 'D115', 'U70', 'E105', 'V109', 'F30', 'W47', 'G110', 'F125', 'W72', 'G72', 'T54', 'D124', 'U1', 'E70', 'F90', 'W98', 'G126', 'T97', 'D135', 'U55', 'E133', 'V9', 'F102', 'W71', 'G121', 'T106']
