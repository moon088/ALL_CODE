from itertools import combinations
from collections import Counter

def calculate_consecutive_combinations_features(hand):
    # 牌の種類ごとの枚数をカウント
    tile_count = Counter(hand)

    # 特徴量の初期化
    features = []

    # 2から6までのnに対して処理
    for n in range(2, 7):
        # 牌の種類ごとに連続するn種類の持っている枚数を計算
        for combination in combinations(tile_count.keys(), n):
            count = sum(tile_count[tile] for tile in combination)
            features.append(count)

    return features

# テスト用の手牌（例: "m1", "m2", "m2", "p4", "p5", "s7", "s8"）
hand = ["m1", "m2", "m2", "p4", "p5", "s7", "s8"]

# 特徴量の計算
result = calculate_consecutive_combinations_features(hand)

# 結果の表示
print(result)
print("Length of the feature array:", len(result))

