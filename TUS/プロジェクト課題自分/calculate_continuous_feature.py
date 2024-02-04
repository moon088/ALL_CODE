from collections import Counter
import itertools

hand = ['m2', 'm5', 'm6', 'p1', 'p2', 'p2', 'p3', 'p3', 'p4', 'p6', 's5', 's6', 's7']
def count_consecutive_sets(hand, n):
    count = 0
    i = 0
    while i <= len(hand) - n:
        if all(hand[i + j] == hand[i] + j for j in range(n)):
            count += 1
            i += n  # Skip the next 'n-1' tiles as they are part of the current set
        else:
            i += 1
    return count

def process_hand(hand):
    # Sort and separate the hand into suits and honor tiles
    suits = {'m': [], 'p': [], 's': [], 'z': []}
    for tile in hand:
        suits[tile[0]].append(int(tile[1:]))
    for suit in suits:
        suits[suit].sort()
    return suits

def calculate_continuous_feature(hand):
    # Process the hand
    processed_hand = process_hand(hand)

    # Count consecutive sets for each suit and each length (2 to 9)
    set_counts = {n: sum(count_consecutive_sets(suit, n) for suit in processed_hand.values()) for n in range(2, 10)}
    #print(set_counts)
    # The maximum number of sets possible for each length
    max_sets = [6, 4, 3, 2, 2, 1, 1, 1]  # for lengths 2, 3, 4, 5, 6, 7, 8, 9

    # Generating all possible combinations of set counts
    all_combinations = itertools.product(*[range(max_sets[i]+1) for i in range(8)])
    # Find the index of the combination that matches our set counts
    for idx, combination in enumerate(all_combinations):
        if all(combination[i] == set_counts[i + 2] for i in range(8)):
            return [1 if j == idx else 0 for j in range(10080)]

    # Return a vector of zeros if no match is found (should not happen)
    #return [0] * 10080
#def if1(a):
    boooool = calculate_continuous_feature(hand)
    count = 0
    index = 0
    for i in boooool:
        if i == 1:
            index = boooool.index(i)
            count += 1
    return count,index
#print(if1(hand))
print(len(calculate_continuous_feature(hand)))
# Example hand
#hand = ['m2', 'm5', 'm6', 'p1', 'p2', 'p2', 'p3', 'p3', 'p4', 'p6', 's5', 's6', 's7']
#feature_vec = calculate_continuous_feature(hand)

# Outputting the length of the feature vector and a snippet of it to verify
#len(feature_vec), feature_vec[:100]  # Displaying the first 100 elements for brevity
    
    
    
    
    
    
    
    
    
    