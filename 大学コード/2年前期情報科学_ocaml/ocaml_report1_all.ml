(*6321120　横溝尚也 ocaml report*)

(*１．dellt*)
let rec dellt n  lst =
  if n >= 0 then 
    if n > 0 then
      match lst with
        []-> []
      | first :: rest -> dellt (n-1) rest
    else lst
  else failwith "Error";;

dellt 0 [1;2;3;4];;
dellt 1 [1;2;3;4];;
dellt 2 [1;2;3;4];;
dellt 3 [1;2;3;4];;
dellt 5 [1;2;3;4];;
dellt 3 ["A"; "B"; "C"; "D"; "E"; "F"];;
dellt(-2) [1; 2];;

(*2.dellt*)
let rec dellt2 n lst =
  match (n , lst) with
    (0 , _) -> lst
  | (_ , []) -> failwith "Error"
  | (1 , a :: rest) -> rest
  | (n , a :: rest) -> a :: (dellt2 (n - 1)rest)
;;

dellt2 1 ["A"; "B"; "C"; "D"; "E"; "F"];;
dellt2 3 ["A"; "B"; "C"; "D"; "E"; "F"];;
dellt2 3 [1; 2; 3; 4; 5; 6];;


(*３．find*)
let rec find n lst =
  match (n , lst) with
    (n , a :: rest) -> if n = a then true
      else find n rest
  | (_ , []) -> false 
;;

find 3 [1; 2; 3; 4; 5; 6];;
find 1 [2; 3; 4; 5];;


(*４．posl*)
let rec posl n lst =
  match (n , lst) with
    (0 , lst) -> failwith "No Exist..."
  | (n , []) -> failwith "No Exist..."
  | (1 ,a :: rest) -> a
  | (n , a :: rest) ->( posl (n-1) rest ) 
;;

posl 3 ["AB"; "C"; "DEF"; "G"; "H"; "IJ"];;
posl 2 [ 1; 2; 3; 4; 5];;
posl 0 [ 1; 2; 3; 4; 5];;

(*５．divlist*)
let rec divlist lst1 lst2 =
  match (lst1 , lst2) with
    ([] , []) -> []
  |([] , lst2) -> failwith "Error"
  |(lst1 , []) -> failwith "Error"
  |(a :: rest1 , b :: rest2) ->
      if b = 0 then failwith "Not Difinite"
      else (a / b) :: divlist rest1 rest2 
;;

divlist [12; 8; 9; 7] [2; 4; 3; 7];;


(*６．mul2list*)
let rec mul2list lst =
  match lst with
    [] -> failwith "Error"
  | _ :: [] -> failwith "Error"
  | a :: b :: rest1 -> if rest1 = [] then [a * b]
      else (a * b) :: mul2list (b :: rest1)
;;

mul2list [1; 2];;
mul2list [1; 2; 3];;
mul2list [1; 2; 3; 4; 5];;


(*７．chglist*)
let rec chglist (n , m) lst =
  match (n , m , lst) with
    (_ , _ , []) -> []
  | (n , m , a :: rest) -> 
      if n = a then m :: chglist (n , m) rest
      else  a :: chglist (n , m) rest
;;

chglist ("A", "*") ["1"; "A"; "2"; "B"; "A"; "A"; "3"; "4"];;


(*８．inslist*)
let rec inslist n m lst =
  if n < 0 then failwith "Error"
  else match (n , m , lst) with
      (n , m , []) -> 
        if n = 1 then m :: lst
        else failwith "Error"
    | (0 , m , lst) -> failwith "Error"
    | (1 , m , lst) -> m :: lst
    | (n , m , a :: rest) -> a :: (inslist (n - 1) m rest)
;;

inslist 2 "*" ["A"; "B"; "C"; "D"; "E"];;
inslist 6 "*" ["A"; "B"; "C"; "D"; "E"];;
inslist 1 "+" [];;
inslist 1 "+" ["A"];;
inslist 0 "+" ["A"];;


(*９．replicate*)
let rec replicate n lst =
  match(n , lst) with 
    (1 , _) -> [lst]
  | (n , _) -> lst :: (replicate (n - 1) lst)
;;

replicate 3 ["A"];;
replicate 5 "A";;
replicate 3 ["1"; "#"];;


(*１０．merge*)
let rec merge lst1 lst2 =
  match (lst1 , lst2) with
    (a:: rest1 , b :: rest2) ->
      a :: b :: merge rest1 rest2
  | ([] , lst2) -> lst2
  | (lst1 , []) -> lst1
;;

merge [1; 2; 3] [4; 5; 6];;
merge ["A"; "B"] [ "C"; "D"; "EF"; "GH"];;


(*１１．inside_length*)
let rec inside_length lst =
  match lst with
    [] -> 0
  | first :: rest1 -> (*リストの中の一つのリストを固定し、要素数を数える。*)
      let rec inside_inside_length first = 
        match first with
          [] -> 0
        | first_first :: rest2 -> 1 + (inside_inside_length rest2)   (*固定するリストを変更*)
      in (inside_inside_length first) + (inside_length rest1)
;;

inside_length[[1; 2; 3]; [4; 5]; [6]; [7; 8; 9; 10]];;
inside_length[["A"; "B"]; [ "C"; "D"]; ["EF"; "GH"]];;


(*１２．concat*)
let rec append l1 l2 = (*リスト同氏を結合させる関数appendを用意*)
  match l1 with
    [] -> l2
  | first :: rest -> first :: (append rest l2)
;;

let rec concat lst =
  match lst with
    [] -> []
  | a :: rest -> let rec append l1 l2 =
                   match l1 with
                     [] -> l2
                   | first :: rest -> first :: (append rest l2)
      in append a (concat rest)
;;

concat [[0; 3; 4]; [2]; [0]; [5; 0]];;


(*１３assoc*)
let rec assoc n lst =
  match (n , lst) with
    (n , []) -> failwith "Not found..."
  | (n , (a , b):: rest)->
      if n = a then b
      else if n = b then a
      else assoc n rest 
;;

assoc 33 [(3,4); (33,5); (11,2); (55,1)];;
assoc 2 [(3,4); (33,5); (11,2); (55,1)];;
assoc "03" [("Kyoto", "075"); ("Osaka", "06"); ("Tokyo", "03")];;
assoc "Kyoto" [("Kyoto", "075"); ("Osaka", "06"); ("Tokyo", "03")];;
assoc 6 [(3,4); (33,5); (11,2); (55,1)];;


(*１４．maximum*)
let rec maximum lst =
  match lst with
    ([]) -> failwith "Error"
  |(a :: []) -> a
  |(a :: b :: rest) ->  (*常にリストの左端を暫定最大値に変更し、１つずつ判別する*)
      if rest = [] then
        if a > b then a 
        else b
      else if a > b then
        maximum (a :: rest)
      else maximum (b :: rest)
;;

maximum [3; 2; 5; 1];;
maximum ["abc"; "sdf"];;
maximum [];;


(*１５．index*)
let rec index lst n =
  match (n , lst) with
    (n , []) -> failwith "Error"
  | (n , a :: rest) -> 
      if not(n = a) then 1 + (index rest n)
      else + 0
;;

index [21; 2; 31; 1] 21;;
index ['a'; '3'; 'b'; 'z'; '1'] 'z';;


(*１６集合の計算*)
(*１６－１．共通集合*)
let rec inter l1 l2 =
  let l3 = l2 in  (*l2は常にすべての要素がそろっている状態、l3は判定する際にだんだん少なくなっていくものとして引数を増やす。*)
  let rec inter2 l1 l3  =
    match (l1, l3) with 
    |(a :: rest1 ,[]) -> inter rest1 l2 
    |(a :: rest1 , b :: rest2) -> (*l1の要素を固定し、l2の全要素と一致するものがないか比較*)
        if a = b then a :: inter rest1 l2 (*一致すればそれを出力の一部にし、l1の次の要素の判定に移る*)
        else inter2 l1 rest2 (*一致しなければその要素を省きほかのl2の要素の判定*)
    |(a :: rest1 ,[]) -> inter rest1 l2(*一致するものがなくl2の全要素調べ上げたら、l1の固定する要素の変更*)
    |([] , l3) -> [] (*l1の全要素調べ上げたら、終了*)
  in inter2 l1 l2
;;

inter [10 ; 15 ;2 ;3 ;59 ;12] [12; 14; 3 ;42 ;10 ];;


(*１６－２。和集合*) (*以下引数l1,l2をそれぞれ集合A,集合Bとする*)
let  rec append l1 l2 = (*二つのリストを結合したリストを返す関数appendを定義*)
  match l1 with
    [] -> l2
  | first :: rest -> first :: (append rest l2)
;;
let rec union l1 l2 = (*A\Bを作成し、最後にA\B+Bを行う方針*)
  let l3 = l2 in
  let rec union2 l1 l3 =
    match (l1 , l3) with
      ([] , []) -> [] 
    |(a :: rest1 , b :: rest2) ->(*l1の要素を固定し、l2と一致するものがあるのか調べる。*)
        if a = b then union rest1 l2(*一致した場合、重複しているため、l1の方を削除*)
        else union2 l1 rest2  (*一致しなかったら、次の判定に移る*)
    |(a :: rest1 , []) -> a :: union rest1 l2 (*すべてのl2について調べたら、固定するl1の要素を変更*)
    |([] , l3) -> l3 
  in union2 l1 l2
;;

union [10; 15; 2; 3; 59; 12] [9 ; 12; 14; 3; 42; 10;11];;


(*１６－３．差集合(l1引くl2の場合)*)
let rec diff l1 l2 =
  let x = inter l1 l2 in  (*和集合を利用*)
  let l3 = l2 in
  let rec diff2 x l3 =    (*和集合xから集合Bを引く*)
    match (x , l3) with 
      (a :: rest1 , b :: rest2) ->
        if  a = b then diff rest1 l2
        else diff2 l1 rest2
    |(a :: rest1 , []) -> a :: diff rest1 l2
    |([] , _) -> [] 
  in diff2 l1 l2
;;

diff [10 ; 15 ;2 ;3 ;59 ;12] [12; 14; 3 ;42 ;10 ];;
diff [10; 15; 2; 3; 59; 12; 39 ;40] [9 ; 12; 14; 3; 42; 10;11];;


