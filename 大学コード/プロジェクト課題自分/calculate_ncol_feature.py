from itertools import combinations

def calculate_syanten(hand):
    # 牌の種類
    suits = ["m", "p", "s", "z"]
    
    # 各色の牌を0にした場合の向聴数を格納するリスト
    syanten_results = []

    # n色の牌を0にした場合の向聴数を計算
    for n in range(1, 4):
        for suit_combination in combinations(suits, n):
            # 各色の牌を0にする
            modified_hand = hand.copy()
            for suit in suit_combination:
                modified_hand = [tile if tile[0] != suit else "0" for tile in modified_hand]
            
            # 向聴数を計算
            syanten = calculate_syanten_for_hand(modified_hand)
            
            # 結果をリストに追加
            syanten_results.append((n, syanten))
    
    return syanten_results

def calculate_syanten_for_hand(hand):
    # ここに向聴数を計算するコードを追加
    # 例えば、牌の組み合わせや待ちの形に基づいて向聴数を計算するロジックを実装
    
    # 仮の返り値
    return 0

# テスト用の手牌（例: 東南西北・一二三四五六七八九・東）
hand = ["1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m", "1p", "2p", "3p", "1z"]

# 向聴数の計算
syanten_results = calculate_syanten(hand)

# 結果の表示
for n, syanten in syanten_results:
    print(f"色{n}を0にした場合の向聴数: {syanten}")