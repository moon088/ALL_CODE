#抽出し、仕分けされたデータから特徴量の計算
import os

#データ読み込み
dir_path = r'C:\Users\81809\Documents\ALL_CODE\大学コード\プロジェクト課題自分'
file_name = 'proceed_data.txt'

file_path = os.path.join(dir_path, file_name)
with open(file_path, 'r', encoding='utf-8') as file:
        txt_data = file.readlines()

data_strip = [line.strip() for line in txt_data ]
list_hai0 = [line_s for line_s in data_strip if 'hai0' in line_s ]      
hai1 = list_hai0[1].strip("hai0=") 

hai1_num = hai1.split(',')
hai1_num = [int(num.strip('"')) for num in hai1_num]
hai1_num.sort()

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

rihairetu = convert_to_category(hai1_num)
print(rihairetu)











