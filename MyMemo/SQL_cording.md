# SQL
## 基本構文
### 宣言
* データベース一覧表示
`SHOW DATABASE`
```sql
mysql> create database prac;
Query OK, 1 row affected (0.04 sec)
```
* テーブル作成
  `CREATE TABLE テーブル名(データ要素名　型)`
```sql
mysql> create table test_rec(
    -> id int,
    -> name char(100),
    -> point int
    -> );
Query OK, 0 rows affected (0.04 sec)
mysql> create table code_list(
    -> name char(100),
    -> code char(100)
    -> );
Query OK, 0 rows affected (0.04 sec)
```
* テーブル削除
  `DELETE FROM 表名 [WHERE 条件]`
```sql
  mysql> drop table test_rec;
  Query OK, 0 rows affected (0.06 sec)
```

* 定義変更
  `ALTER`

* データ更新
  `UPDATE 表名 SET 列名 = 変更値, ,,,  [WHERE 条件]`
* データ削除
  `DELETE`

* 列追加
  `ALTER TABLE ~~ ADD ~~`
```sql
mysql> alter table test_rec add point int not null;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
* データ挿入
  `INSERT INTO 表名 [列名リスト] VALUES(列リスト)`
  `INSERT INTO 表名 [列名リスト] SELECT`
```sql
mysql> insert into test_rec(id ,name ,point)
    -> values(1,"alice",73);
Query OK, 1 row affected (0.01 sec)
mysql> select * from test_rec;
+------+-------+-------+
| id   | name  | point |
+------+-------+-------+
|    1 | alice |    73 |
+------+-------+-------+
1 row in set (0.00 sec)
```


* SELECT
  ```sql
  SELECT [ALL|DISTINCT] ~~
    FROM ~~
    [WHERE]```
    [GROUP BY]
    [HAVING]
    ```
この順で解釈される!!!



* ファイル実行
`SOURCE ファイル名`
* ビューの作成
`CREATE VIEW ビュー名 AS (SELECT文 [with [cascaded | local] check option])`
仮想的なテーブルであり、データは持たない。参照のたびに実行されるため、データ更新にも反映される。

* 画面クリア
???


### アクセス制御
読み取り権限->SELECT
挿入権限->INSERT
削除権限->DELETE
更新権限->UPDATE

* 表やビューのアクセス権の付与
  ALL PRIVILEGESですべての権限付与
  `GRANT 権限リスト ON 表名 TO 利用者リスト`
* アクセス権の削除
  `REMOVE 権限リスト ON 表名 FROM 利用者リスト`
* トランザクション処理の確定
  `COMMIT`
* トランザクション処理の取り消し
  `ROLLBACK`

### カーソル処理
SELECT文に対してカーソルを宣言するK所とで１行ずつ取り出して処理を行う

1. カーソルの割り当て・宣言
  `DECLARE カーソル名 CURSOR FOR SELECT,,,`
2. カーソルのオープン
  `OPEN カーソル名`
3. 1行取り出し
  `FETCH カーソル名 INTO 閣下受け取りのホスト変数`
* カーソルのクローズ
  `CLOSE カーソル名`

```sql
EXEC SQL DECLARE syain_cur CURSOR FOR
  SELECT 社員名 FROM 社員
    WHERE SQL OPE  syain_cur;
    WHILE(1){
      EXEC SQL FETCH syain_cur INTO :NAME;
      IF(SQLCODE != 0) BREAK;
      printf("氏名は%s￥n", name);}  
EXEC SQL CLOSE syain_cur;
```
### 検索条件
  * BETWEEN
  * IN
  * IS NULL
  * LIKE
    %は０文字以上、_は任意の１文字


### 集約関数
最も大切なのはグループ化したらSELECT句で指定できるのはグループ化列の名前、集合関数、定数のみ

* AVG(列名)
指定した列のNULL以外の値の平均
すべての列数ならAVG(*)

* count(列名,(または*))
指定した列のNULL以外の値の数。*は表に含まれる行（レコード）の数
* max(列名),min(),sum
指定した列の最大値、最小、合計

```sql
mysql> select point, avg(point) from test_rec natural join code_list group by point;
+-------+------------+
| point | avg(point) |
+-------+------------+
|    73 |    73.0000 |
|    64 |    64.0000 |
|    63 |    63.0000 |
|    80 |    80.0000 |
+-------+------------+
4 rows in set (0.00 sec)

mysql> select point, avg(point) from test_rec natural join code_list group by point having point >70;
+-------+------------+
| point | avg(point) |
+-------+------------+
|    73 |    73.0000 |
|    80 |    80.0000 |
+-------+------------+
2 rows in set (0.00 sec)
```

### 出力順
* ORDER BYによって
  `ORDER BY 年齢 (ASC昇順 OR DISC降順)`


### 参照制約
被参照表の主キーにない値を、参照表の外部キーに追加することはできない
被参照表の行の削除・変更するとき、制約を指定できる。
CREATE TABLEの時指定する。
`REFERENCE 被参照表　[ON DELETE 参照動作], [ON UPDATE 参照動作]`
* NO ANCTION 
  削除・変更はするが、参照制約が満たされなくなれば削除・変更取り消す。
* CASCADE
  削除・変更を実施し、当該行を参照している表の行があれば、その行も削除する。連鎖する
* SET DEFAULT
  被参照表の行が削除・変更されたとき、それを参照してい参照表の外部キーへ規定値を設定する。

###　列制約
CREATE TABLEの際に列ごとに制約を指定できる

* 一意制約性
  PRIMARY KEY 主キーに指定
  UNIQUE 値の重複を認めない
  `列名 データ型 PRIMARY KEY`
* 参照制約
  外部キーに指定被参照表とその列名を指定。列名指定しなければ主キーになる
  `列名 データ型 REFERENCE 被参照表 列名`
* 検査制約
  登録できる値の条件を指定
  `評価　INTEGER CHECK (評価 BETWEEN 1 AND 5)`
* 非NULL制約
* DEFAULT制約
  行挿入時に値が指定されていないときの既定値を入力

### データ型
* 文字型
  CHARACTER(n)-> nバイトの固定長
  CHARACTER VARYING(n)-> 最大nバイトの可変長文字列
* 数値型
  INTEGER -> 整数値
  NUMERIC(m,[,n])-> 固定小数点
* ビット型
  BIT
  BIT VARYING(n)
  BLOG(x)

### window関数
現在の行に関するテーブル全体をなめる計算をする。集約関数と似ている  

構文は、`ウィンドウ関数 over partition by 列名) from テーブル名`
```sql
mysql> select *,avg(point) over (partition by point) as avg from  test_rec natural join code_list;
+---------+------+-------+------+---------+
| name    | id   | point | code | avg     |
+---------+------+-------+------+---------+
| Charlie |    3 |    63 | AA   | 63.0000 |
| Bob     |    2 |    64 | EE   | 64.0000 |
| alice   |    1 |    73 | IS   | 73.0000 |
| Dave    |    3 |    80 | AU   | 80.0000 |
+---------+------+-------+------+---------+
4 rows in set (0.00 sec)
```

### 結合
* 内結合(等結合)
  指定した項目が等しいものを結合
 
* 外結合
  結合列が一致しなくても結合(NULLで埋める)
  ・左外結合LEFT OUTER JOIN
  ・右外結合RIGHT OUTER JOIN
  ・完全外結合FULL OUTER JOIN

結合の構文は以下
 ```sql 
  SELECT ~~
    FROM (A INNER JOIN B)
      ON A.a = B.b
  ```
* COALESCE
  外結合を拡張し、COALESCE(A,B)でAがNULLでなければAを、BがNULLでなければBを返す。

* テーブル結合
  `NATURAL JOIN`
```sql
mysql> select * from test_rec;
+------+---------+-------+
| id   | name    | point |
+------+---------+-------+
|    1 | alice   |    73 |
|    2 | Bob     |    64 |
|    3 | Charlie |    63 |
|    3 | Dave    |    80 |
+------+---------+-------+
4 rows in set (0.00 sec)
mysql> select * from code_list;
+---------+------+
| name    | code |
+---------+------+
| alice   | IS   |
| Bob     | EE   |
| Charlie | AA   |
| Dave    | AU   |
+---------+------+
4 rows in set (0.00 sec)

mysql> select * from test_rec natural join code_list;
+---------+------+-------+------+
| name    | id   | point | code |
+---------+------+-------+------+
| alice   |    1 |    73 | IS   |
| Bob     |    2 |    64 | EE   |
| Charlie |    3 |    63 | AA   |
| Dave    |    3 |    80 | AU   |
+---------+------+-------+------+
4 rows in set (0.00 sec)
```


>• ROW_NUMBER()
• RANK()
• DENSE_RANK()
• PERCENT_RANK()
• CUME_DIST()
• NTILE()
• LAG()
• LEAD()
• FIRST_VALUE()
• LAST_VALUE()
• NTH_VALUE()

などがwindow関数専用のものである
例として、
```sql
mysql> select *,rank() over (order by point) as "rank" from  test_rec natural join code_list;
+---------+------+-------+------+------+
| name    | id   | point | code | rank |
+---------+------+-------+------+------+
| Charlie |    3 |    63 | AA   |    1 |
| Bob     |    2 |    64 | EE   |    2 |
| alice   |    1 |    73 | IS   |    3 |
| Dave    |    3 |    80 | AU   |    4 |
+---------+------+-------+------+------+
4 rows in set (0.00 sec)
```

### 集合演算
* 和、差、積集合
`SQL文１　union(except or interesect) SQL文2`
UNION,INTERSECT,EXCEPT,CROSS　JOIN

```sql
mysql> select * from test_rec2;
+------+------+-------+
| id   | name | point |
+------+------+-------+
|    1 | carl |    38 |
|    2 | kont |    90 |
|    3 | gira |    45 |
+------+------+-------+

mysql> select * from test_rec union select * from test_rec2;
+------+---------+-------+
| id   | name    | point |
+------+---------+-------+
|    1 | alice   |    73 |
|    2 | Bob     |    64 |
|    3 | Charlie |    63 |
|    3 | Dave    |    80 |
|    1 | carl    |    38 |
|    2 | kont    |    90 |
|    3 | gira    |    45 |
+------+---------+-------+
7 rows in set (0.00 sec)
```

### データ処理・加工関数
* case関数
`case when 条件式 then trueの処理 else falseの処理 end`
```sql
mysql> select *, case when point >= 80 then 'S'
    -> when point >= 70 then 'A'
    -> when point >= 60 then 'C'
    -> else 'D'
    -> end as "val"
    -> from test_rec;
+------+---------+-------+-----+
| id   | name    | point | val |
+------+---------+-------+-----+
|    1 | alice   |    73 | A   |
|    2 | Bob     |    64 | C   |
|    3 | Charlie |    63 | C   |
|    3 | Dave    |    80 | S   |
+------+---------+-------+-----+
4 rows in set (0.00 sec)
```
* 日付関数
current_date,current_timestamp
* coalesce関数
引数のうち、NULLでない最初の引数を返す。
* concat関数
文字列の結合
`mysql> select * from aaa;`

### 副問い合わせ
最も大切なのは単一値ならWHERE ~~ =　(福問合わせ)でいいが、
複数値ならWHERE ~~ IN(副問い合わせ)にしないといけない

* 相関副問い合わせの見分け方
  副問い合わせがＦＲＯＭ句でしていない主問い合わせの表を使用していれば相関である。

WHEREは条件に対する結果TRUE OR FALSEが入る。
A=Bなのか、EXIST (式)など。
```sql
mysql> select * from test_rec natural join code_list where point in (select point from test_rec where point >= 70);
+-------+------+-------+------+
| name  | id   | point | code |
+-------+------+-------+------+
| alice |    1 |    73 | IS   |
| Dave  |    3 |    80 | AU   |
+-------+------+-------+------+
2 rows in set (0.00 sec)
```


### WITHとCASE
* WITH句
  その問い合わせの中でのみ使用できる一時的な表
以下は所属人数が最も多い部門の出力
```sql
  WITH 部門所属人数 (部門コード,所属人数)
    AS (SELECT 部門コード, COUNT(*)
      FROM 社員 GROUP BY 部門コード)
  
  SELECT 部門コード, 所属人数
    FROM 部門所属人数
    WHERE 所属人数 = (SELECT MAX(所属人数) FROM 部門所属人数) 
```

* CASE句
```sql
  SELECT 社員名 CASE
    WHEN 年齢 < 20 THEN "20未満"
    WHEN 年齢 >= 20 AND 年齢　< 30 THEN "20以上"
    ELSE "30以上"
    END AS 年代
  FROM 社員
```

###　ストアドプロシージャ
一つのSQL文を一つにまとめ、CALLコマンドで呼び出せるようにする処理
```sql
mysql> delimiter //
mysql> create procedure p1()
    -> begin
    -> select * from test_rec;
    -> end
    -> //
Query OK, 0 rows affected (0.01 sec)

mysql> delimiter ;
mysql> call p1;
+------+---------+-------+
| id   | name    | point |
+------+---------+-------+
|    1 | alice   |    73 |
|    2 | Bob     |    64 |
|    3 | Charlie |    63 |
|    3 | Dave    |    80 |
+------+---------+-------+
4 rows in set (0.01 sec)

Query OK, 0 rows affected (0.01 sec)
```

### ストアドファンクション
ストアドプロシージャと基本的に同じだが、関数なので返戻地が必要
```sql
mysql> delimiter //
mysql> create function f(i integer) returns integer deterministic
    -> begin
    -> return (i+i);
    -> end
    -> //
Query OK, 0 rows affected (0.01 sec)

mysql> delimiter ;
mysql> select f(10);
+-------+
| f(10) |
+-------+
|    20 |
+-------+
1 row in set (0.00 sec)
```


### ビュー
操作の簡易化や特定の条件で検索したビューだけをアクセスさせること元の表のデータの一部を隠蔽できる
SELECTに式や集合関数、DISTINCTを指定、
FROM句に更新不可ビューを指定
GROUP,HAVINGを使用
これらのときは更新不可能なビューである。
`CREATE VIEW ビュー名 [(列名1,列名2,,,,]  AS SELECT,,,`

###　INDEX
データベースの規模が拡大したときにアクセス速度を劇的に早くできる
* インデックスの確認
```sql
mysql> select * from friend;
+----+--------+--------+--------+
| id | name   | phone1 | phone2 |
+----+--------+--------+--------+
|  1 | Tanaka | 080    | NULL   |
|  2 | Suzuki | NULL   | 090    |
+----+--------+--------+--------+
2 rows in set (0.01 sec)

mysql> show index from friend;
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table  | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| friend |          0 | PRIMARY  |            1 | id          | A         |           2 |     NULL |   NULL |      | BTREE      |
|               | YES     | NULL       |
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
1 row in set (0.01 sec)
```

* インデックスの変更
```sql
mysql> alter table test_rec add index test_index(id,name);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show index from test_rec;
+----------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table    | Non_unique | Key_name   | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+----------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| test_rec |          1 | test_index |            1 | id          | A         |           3 |     NULL |   NULL | YES  | BTREE      |         |               | YES     | NULL       |
| test_rec |          1 | test_index |            2 | name        | A         |           4 |     NULL |   NULL | YES  | BTREE      |
    |               | YES     | NULL       |
+----------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
2 rows in set (0.01 sec)
```

* インデックスの削除
```sql
mysql> drop index test_index on test_rec;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

* その他のインデックス関係
• テーブル作成時にインデックス作成
• mysql> create table テーブル名(作成対象カラム名 データ型 not null,index インデックス名(作成対象カラム名));
• 既存のテーブルにインデックス作成
• mysql> create index インデックス名 on テーブル名(作成対象カラム名);
• mysql> alter table テーブル名 add index インデックス名(対象カラム名);
• インデックスの確認
• mysql> show index from テーブル名;
• インデックスを使用して検索しているか確認
• mysql> explain select * from テーブル名 where文～等
• インデックスの削除
• mysql> drop index インデックス名 on テーブル名;


## 関連リンク
* [Quitaコマンド集](https://qiita.com/shuyam/items/809ff4123d8dcb7321f9)