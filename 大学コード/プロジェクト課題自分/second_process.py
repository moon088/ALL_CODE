#吉場作、天鳳データから一人麻雀の教育データの仕分け
#出力値(最初にリーチした人,リーチした人の初期手配,ドラ,リーチになるまでに各プレイヤーの切った牌と順番通りに並べてもの)

import os
import xml.etree.ElementTree as ET

def analyze_xml(file_path):
    # XMLデータをファイルから読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_data = file.read()

    # XMLの構造をパースする
    root = ET.fromstring(xml_data)

    # <INIT> タグを見つける
    init_elements = root.findall('.//INIT')

    # 各 <INIT> タグに対して処理を行う
    for i in range(len(init_elements)):
        init = init_elements[i]
        # 次の<INIT>タグがあるか、または最後の<INIT>タグかを確認する
        if i < len(init_elements) - 1:
            next_init = init_elements[i+1]
            next_init_index = list(root).index(next_init)
        else:
            next_init_index = len(list(root))

        # 現在の<INIT>タグの位置を取得
        init_index = list(root).index(init)

        # 現在と次の<INIT>タグまたは</mjloggm>の間にある要素を取得
        elements_between = list(root)[init_index:next_init_index]

        # 現在の<INIT>タグから次の<INIT>タグまたは</mjloggm>の間の捨て牌を格納するリスト
        discards = []

        # 初期手牌とドラ表示牌を取得
        player_hands = {f"hai{p}": init.get(f"hai{p}") for p in range(4)}
        seed = init.get('seed').split(',')
        dora_indicator = seed[5] if len(seed) > 5 else 'NULL'  # ドラ表示牌はseedの5番目の要素

        # 最初のリーチが見つかるまでの捨て牌をリストに追加する
        reach_found = False
        for elem in elements_between:
            # 最初のリーチを検出
            if elem.tag == 'REACH' and elem.get('step') == '1':
                player_number = elem.get('who')
                reach_found = True
                break  # 最初のリーチの後は捨て牌を見ない
            elif elem.tag[0] in 'TUVWDEFG':  # 捨て牌に関連するタグの場合
                discards.append(elem.tag + elem.text if elem.text else elem.tag)

        # 出力
        if reach_found:
            print(f"Round starting at <INIT> index {init_index} has a REACH by player {player_number}.")
            print(f"hai{player_number}=\"{player_hands[f'hai{player_number}']}\"")
            if not any(e.tag == 'RYUUKYOKU' for e in elements_between):
                print(f"dorahai = \"{dora_indicator}\"")
            else:
                print("dorahai = NULL")
            print(f"Discards before REACH: {discards}\n")
        else:
            print(f"Round starting at <INIT> index {init_index} does not have a REACH.\n")

# ディレクトリ内のすべての.xmlファイルを検索して処理
directory_path = r'C:\Users\81809\Documents\ALL_CODE\大学コード\\プロジェクト課題自分' # XMLファイルが保存されているディレクトリのパスを指定

for filename in os.listdir(directory_path):
    if filename.endswith('.xml'):
        file_path = os.path.join(directory_path, filename)
        analyze_xml(file_path)
