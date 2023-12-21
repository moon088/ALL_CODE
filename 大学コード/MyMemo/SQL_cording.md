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
    -> id integer,
    -> name char
    -> );
Query OK, 0 rows affected (0.11 sec)
```
* 列追加
```sql
mysql> alter table test_rec add point int not null;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
* データ挿入
`insert into テーブル名 set id = 1,val = 80`
* ファイル実行
`soure ファイル名`
* ビューの作成
`create view ビュー名 as (select文 [with [cascaded | local] check option])`
仮想的なテーブルであり、データは持たない。参照のたびに実行されるため、データ更新にも反映される。
### 集約関数
* AVG(列名)
指定した列のNULL以外の値の平均
* count(列名,(または*))
指定した列のNULL以外の値の数。*は表に含まれる行（レコード）の数
* max(列名),min(),sum
指定した列の最大値、最小、合計

### window関数
現在の行に関するテーブル全体をなめる計算をする。集約関数と似ている  

構文は、`ウィンドウ関数 over partition by 列名) from テーブル名`



### 集合演算
* 和、差、積集合
`SQL文１　union(except or interesect) SQL文2`

### データ処理・加工関数
* case関数
`case when 条件式 then trueの処理 else falseの処理 end`
* 日付関数
current_date,current_timestamp
* coalesce関数
引数のうち、NULLでない最初の引数を返す。
* concat関数
文字列の結合
`mysql> select * from aaa;`
