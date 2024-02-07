# AtCoderメモ
## メソッド
###　文字変換
* upper(): すべての文字を大文字に変換
* lower(): すべての文字を小文字に変換
* capitalize(): 先頭の一文字を大文字、他を小文字に変換 
* title(): 単語の先頭の一文字を大文字、他を小文字に変換
* swapcase(): 大文字を小文字に、小文字を大文字に変換
* isupper(): すべての文字が大文字かどうか判定
* islower(): すべての文字が小文字かどうか判定
* istitle(): タイトルケースかどうか判定
  
###　リスト
* l.insert(index,val): indexにvalを追加
* l.extend(): 末尾にリスト追加
* l.copy(): コピー
* l.sort(),sorted(): 変換か、新たなリスト生成
* l.reverse(),reversed(): copyと同じ
* l.pop(index): indexの値削除し、値取得
* l.clear(): クリア
  
### 辞書型
辞書型に関するURL: <https://www.sejuku.net/blog/24122>


###　文字コード
* ord():文字から文字コード取得
* chr():文字コードから文字取得
  * ex.) a->97, A->65

###　入力
* 入力に関するURL: <https://qiita.com/scythercas/items/5e08dfffb49468dd1176>

###　その他
* recerced(A): 逆順リストの新たな生成
* NEW_A = "".join(A)リストの各要素結合
* pow(a,N): aをN乗



## アルゴリズム
1. 幅優先探索
各ノードに始点には0、他INFにセット。キューを使用して終点に行きつくまで繰り返し処理を行う。
2. k回目の処理：キューから一つデキューしてそのノードについて調べる。現在のノードと隣接しているノードをキューに距離をkとし、プッシュ。プッシュされたノードは順に処理される

3. 4方向の回転:directを0,1,2,3とし、右回転ならインクリメント、左回転ならデクリメントして4の剰余とる

4. 二分探索: Left=0,Right=INF(最大値),MID=(R-L)//2とする。
  MIDに対して走査してそれより右にあるなら LをMIDに、左にあるならRをMIDとする。これを繰り返す。ただしソートされているのが前提

5. ３つ足してKとなるa,b,c:a,b,cそれぞれにループさせたらオーダー大きいから、a,bループしてK-a-bがcに存在するか調べるとcのループしなくて済む

6. ある配列の値をインデックスとした違う配列の値を更新:例えばある条件の下でP[i] <- P[B[i]]など。
  この時は[3,2,4,1,5]ならば3->4->1->3と2->5->2となり必ず閉じた有効グラフとなる。そのため有効グラフで考える


7. 動的計画法(Dynamic Programing)
  全探索せずに小さな計算結果を保存し、冗長な計算を避ける。
   * 最適化、ナップサック問題、部分和問題 ect...
  例:Lこの数値をいくつか足し合わせてSになるものを探す。
    L行S+1列の配列に最大値を入れていく。
    オーダーはL(S+1)

    <動的計画法に関するURL>
    [初歩]<https://www.momoyama-usagi.com/entry/info-algo-dp#i>
    [Quita]<https://qiita.com/drken/items/dc53c683d6de8aeacf5a>
    [Quita:Dp問題の網羅](https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB-----dp-%E3%81%AF%E5%BD%B9%E3%81%AB%E7%AB%8B%E3%81%A4)
    [Quita:Dp問題の網羅2](https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB-----dp-%E3%81%AF%E5%BD%B9%E3%81%AB%E7%AB%8B%E3%81%A4)
  
  ```python
  def find_max_dp(num_list, limit): #行がリストの要素、列がSまでの数値
    list_len = len(num_list)
    dp_table = [[0 for j in range(limit + 1)] for i in range(list_len)]

    # 1番目
    for j in range(limit + 1):
        if num_list[0] <= j:
            dp_table[0][j] = list[0] # 1番目追加
 
    # 2番目以降
    for i in range(list_len):
        for j in range(limit + 1):
            tmp_not_choice = dp_table[i-1][j]
            if num_list[i] > j: # i番目の要素がjに到達しないときはi-1をそのまま採用
                dp_table[i][j] = tmp_not_choice 
            else: 
              #i-1行j列の値(i番目を不採用)とi-1行(j-i番目の値)列にi番目の値を足したもの(i番目を採用)をmaxで判定
                tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(tmp_choice,tmp_not_choice)
 
    return dp_table[list_len - 1][limit]

  list = [4,8,6]
  print(find_max_dp(list,10))
  ```

```python
  # A18 - Subset Sum
  #部分和問題SとなるならYes,ならないならNo

N, S = map(int, input().split())
A = list(map(int, input().split()))


# 動的計画法（i=0）
dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
dp[0][0] = True
for i in range(1, S+1):
	dp[0][i] = False

# 動的計画法（i=1）
for i in range(1, N+1):
	for j in range(0,S+1):
		if j < A[i-1]:
			if dp[i-1][j] == True:
				dp[i][j] = True
			else:
				dp[i][j] = False

		if j >= A[i-1]:
			if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
				dp[i][j] = True
			else:
				dp[i][j] = False

# 出力
if dp[N][S] == True:
	print("Yes")
else:
	print("No")
  ```