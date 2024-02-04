# SQL
## コマンド
### 基本コマンド
* データベース一覧表示
`show datebases`
```sql
mysql> create database prac;
Query OK, 1 row affected (0.04 sec)
```
* テーブル作成
  `create table テーブル名(データ要素名　型)`
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
```sql
  mysql> drop table test_rec;
  Query OK, 0 rows affected (0.06 sec)
```
* 列追加
```sql
mysql> alter table test_rec add point int not null;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
* データ挿入
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

* テーブル結合
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

* ファイル実行
`soure ファイル名`
* ビューの作成
`create view ビュー名 as (select文 [with [cascaded | local] check option])`
仮想的なテーブルであり、データは持たない。参照のたびに実行されるため、データ更新にも反映される。

* 画面クリア
???




### 集約関数
* AVG(列名)
指定した列のNULL以外の値の平均
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