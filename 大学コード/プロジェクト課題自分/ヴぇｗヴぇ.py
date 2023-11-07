import os

dir_path = r'C:\Users\81809\Documents\ALL_CODE\大学コード\プロジェクト課題自分'
file_name = 'proceed_data.txt'

file_path = os.path.join(dir_path, file_name)
with open(file_path, 'r', encoding='utf-8') as file:
        txt_data = file.readlines()

data_strip = [line.strip() for line in txt_data ]
#print(data_strip)

#抽出
keywords_to_extract = ["hai0", "hai1", "hai2","hai3"]
pickup_initial_hand = [item for item in data_strip if any(keyword in item for keyword in keywords_to_extract)]



# 削除したいキーワードのリスト
keywords_to_remove = ["hai0=", "hai1=","hai2=","hai3="]

# キーワードを削除して新しい配列に格納
filtered_initial_hand = pickup_initial_hand.copy()  # 元の配列を変更しないためにコピー

for keyword in keywords_to_remove:
    filtered_initial_hand = [item.replace(keyword, "") for item in filtered_initial_hand]

#ここまででhai0~3の手配抽出していらない文字削除


print(filtered_initial_hand)


 
 
hai = ['"91,124,49,2,59,44,100,32,77,63,29,27,76"', '"25,50,68,5,85,28,21,61,18,7,38,47,37"']
hai1_num = filtered_initial_hand[1]
hai1_num = hai1_num.split(',')
hai1_num = [int(hai1_num.strip('"')) for num in hai1_num]
hai1_num.sort()


for item in filtered_initial_hand:
    initial_hand = item.split(',')
    initial_hand = [int(num.strip('"')) for num in item]
    initial_hand.sort()
print(initial_hand)