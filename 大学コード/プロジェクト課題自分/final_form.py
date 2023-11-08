#これは全体の動きをイメージするための物

import second_process
import update_hand
import ex_change_characters
#import feature_val_cal
import os

second_process.directory_path = r'C:\Users\81809\Documents\ALL_CODE\大学コード\プロジェクト課題自分'

for filename in os.listdir(second_process.directory_path):
    if filename.endswith('.xml'):
        result = []
        file_path = os.path.join(second_process.directory_path, filename)
        result = (second_process.analyze_xml(file_path))
        
# second_process.pyで出力されるリストを二つに分け、update_handに作用させる。
        # 'hai' を整数のリストとして分ける
    
        # すべてのデータサンプルに対して処理を行う
        for sample in result:
            # haiXとdiscards_before_reachのキーを取得
            hai_keys = [key for key in sample if key.startswith('hai')]
            for key in hai_keys:
                # hai_valuesを文字列から整数のリストに変換
                hai_values = [int(value) for value in sample[key].split(',')]
                discards_values = sample['discards_before_reach']
                
                #print(f"x = {key[-1]}")
                #print("hai values:", hai_values)  # ここで整数のリストとして出力
                #print("discards_before_reach:", discards_values)
                #print()  # 改行で区切る

            # 初期手牌 = initial_hands , Discards before REACH = discardsにして、update_handにぶち込む。
                update_hand.initial_hand = hai_values
                update_hand.discards = discards_values
                update_hand.x = int(key[-1])

                nested_list = update_hand.print_updated_hands(update_hand.initial_hand, update_hand.discards,update_hand.x)
                print("aaa")
                for i in range(1, len(nested_list)):
                # 前のリストと現在のリストをセットに変換
                    prev_set = set(nested_list[i-1])
                    current_set = set(nested_list[i])

                    # 前のリストにはあったが、現在のリストにはない要素を探す
                    missing_elements = prev_set - current_set

                    # 消えた要素を出力
                    #if missing_elements:
                        #print(f"消えた要素: {missing_elements}")
                    #else:
                        #print("新しいリストには前のリストのすべての要素が含まれています")

                    # そしてその出力結果をex_change_charactersにかまして136次元にする。かましたもの = indices_136[]になるイメージ。
                    # 最終的にはfeature_val_cal.pyの予定だけど。今回はとりあえず七対子は使わないで行く。すまん。
                    # なので、今回に限った平均化パーセプトロンの動かし方してるからね。
                    test_character = ex_change_characters.create_feature_vector(prev_set)
                    print(test_character)