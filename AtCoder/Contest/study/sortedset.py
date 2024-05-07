from sortedcontainers import SortedSet, SortedList, SortedDict
S = SortedSet([3, 1, 2,6,7,8,9,10])
#SortedSet([1, 2, 3]), 初期化の計算量は O(N * logN)
S.add(4)
print(S)
#SortedSet([1, 2, 3, 4]), add の計算量は O(logN)
S.add(3)
print(S)
#SortedSet([1, 2, 3, 4]), 要素は重複しない
S.discard(4)
print(S)
#SortedSet([1, 2, 3]), 値4を削除 計算量は O(logN) 存在しない要素をdiscardすると、何も起こらない
#S.remove(100) とやると、KeyErrorが出る
S.pop(2)
print(S)
#S[2]を削除 S.pop()で最大要素の削除 S.pop(0) で最小要素の削除　全部 O(logN)
print(S[1])

#2 getは O(logN)
print(S[0:2])
#0 1 スライスなどもできる　これの計算量は長さを k として O(klogN)
print(len(S))
#2 現在の要素数 O(1)
print(S.bisect_left(1))
#1
print(S.bisect_right(1))
#2
#これらは二分探索。 S.bisect_left(x) で、Sにxを挿入する位置(index)を返す。
#S.bisect_right(x) との違いは、すでにxがSにあるときに左に入れるか右に入れるか
#Pythonのbisectと同じ使用感
print(S.index(2))

#1 Sに2が現れる最初の位置を返す。ないとValueError
print(S.irange(0,2))

#[1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙
