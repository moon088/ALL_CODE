#抽出し、仕分けされたデータから特徴量の計算
import os

#データ読み込み
dir_path = r'C:\Users\81809\Documents\ALL_CODE\大学コード\プロジェクト課題自分'
file_name = 'proceed_data.txt'

file_path = os.path.join(dir_path, file_name)
with open(file_path, 'r', encoding='utf-8') as file:
        txt_data = file.readlines()

data_strip = [line.strip() for line in txt_data ]

pickup_initial_hand = [item for item in data_strip if "hai0=" in item]
filtered_initial_hand = [item.replace("hai0=", "") for item in pickup_initial_hand]
initialhand = filtered_initial_hand[1].split(',')
initialhand = [int(num.strip('"')) for num in initialhand]
initialhand.sort()


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

rihairetu = convert_to_category(initialhand)
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

calculate_titoitu_shanten(rihairetu)





