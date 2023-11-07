def calculate_mahjong_shanten(hand):
    def calculate_mahjong_shanten_sub(hand):
        if len(hand) != 13:
            return "Invalid hand"

        unique_tiles = set(hand)
        pairs_count = 0

        for tile in unique_tiles:
            count = hand.count(tile)
            pairs_count += count // 2

        shanten = 6 - pairs_count
        return shanten

    shanten = calculate_mahjong_shanten_sub(rihairetu)

    if shanten == "Invalid hand":
        print("Invalid hand")
    else:
        print("向聴数:", shanten)

rihairetu = ['m2', 'm2', 'm5', 'm6', 'm7', 'm8', 'p1', 'p1', 'p3', 'p4', 'p7', 'p9', 's4']    
calculate_mahjong_shanten(rihairetu)    