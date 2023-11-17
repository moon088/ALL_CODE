#抽出し、仕分けされたデータから特徴量の計算
import os
import second_process

#データ読み込み
second_process.directory_path = r'C:\Users\81809\Documents\ALL_CODE\大学コード\プロジェクト課題自分'

for filename in os.listdir(second_process.directory_path):
    if filename.endswith('.xml'):
        result = []
        file_path = os.path.join(second_process.directory_path, filename)
        result = (second_process.analyze_xml(file_path))

        for sample in result:
            # haiXとdiscards_before_reachのキーを取得
            hai_keys = [key for key in sample if key.startswith('hai')]
            for key in hai_keys:
                # hai_valuesを文字列から整数のリストに変換
                hai_values = [int(value) for value in sample[key].split(',')]


print(hai_values)
hai_values.sort()
print(hai_values)

#ここまでで牌の文字列を整数変換してソートした
#牌列を数値ではなく可視化する
def convert_to_category(input_list):
    def convert_to_category_sub(num):
        if 1.0 <= num <= 35:
            temp = int((num)/4+1)
            return 'm'+ str(temp)
        elif 36 <= num <= 71:
            temp = int((num-36)/4+1)
            return 'p' + str(temp)
        elif 72 <= num <= 107:
            temp = int((num-72)/4+1)
            return 's' + str(temp)
        elif 108 <= num <= 136:
            temp = int((num-108)/4+1)
            return 'z' + str(temp)
        else:
            return 'Invalid'
        
    converted = [convert_to_category_sub(num)  for num in input_list]
    return converted

rihairetu = convert_to_category(hai_values)
print(rihairetu)


#ここからは特徴量の計算
def calculate_titoitu_shanten(hand):
    def calculate_titoitu_shanten_sub(hand):
        if len(hand) != 13:
            return "error"
        
        count_of_kantu = 0
        for tile in hand:
            count = hand.count(tile)
            if count >= 4:
                count_of_kantu += 1
                
        allcount_of_kantu = int(count_of_kantu/4)        
        unique_tiles = set(hand)
        pairs_count = 0
        for tile in unique_tiles:
            count = hand.count(tile)
            pairs_count += count // 2

        shanten = 6 - pairs_count + allcount_of_kantu
        return shanten

    shanten = calculate_titoitu_shanten_sub(hand)
    
    if shanten == "error":
        print("手牌の長さが不正です。")
    else:
        print("向聴数:", shanten)


def calculate_kokusi_shanten(hand):
    





calculate_titoitu_shanten(rihairetu)





