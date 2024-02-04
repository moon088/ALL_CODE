(*課題１：１.挿入ソート*)
let sort_of_insert lst = 
  let lst2 = [] in
  let rec insert lst lst2 = 
    match lst with 
    | [] -> lst2
    | a :: rest ->
        let rec insert2 lst2 = 
          match lst2 with
          |[] -> a :: lst2
          | x :: rest2 ->
              if a > x then x :: (insert2 rest2) 
              else a :: lst2 
        in insert rest (insert2 lst2)
  in insert lst lst2
;;

sort_of_insert [150;2;14;56;3;4];;
sort_of_insert [100;123;3;6;38;394;4441;5;0];;
  
(*課題１：２.選択ソート*) 
(*サブ関数：指定した要素をリストから引き抜く*)
let rec pull_out n lst =
  match (n , lst) with 
  | (_ , []) -> []
  | (n , a :: rest) -> 
      if n = a then (pull_out n rest)
      else a :: (pull_out n rest)
;;

(*メイン関数*)
let rec sort_of_select lst =
  match lst with
  | [] -> []
  | [a] -> [a]
  | a :: b :: rest -> 
      let newlst = lst 
      in let rec pick_min lst =
           match lst with
           | [] -> []
           | [a] -> a :: sort_of_select (pull_out a newlst)
           | a :: b :: rest -> 
               if a >= b then pick_min (b :: rest)
               else pick_min (a :: rest)
      in pick_min lst
;;

sort_of_select [150;2;14;56;3;4];;
sort_of_select [100;123;3;6;38;394;4441;5;0];;   
        
(*課題１：３.バブルソート*)  
let rec sort_of_bubble lst =
  match lst with
    [] -> []
  | lst -> 
      let lst2 = lst 
      in let rec bubble lst2 =
           match lst2 with
             [] -> []
           | [a] -> [a]
           | a :: b :: rest -> 
               if a > b then b :: bubble (a :: rest)
               else a :: bubble (b :: rest)
      in let lst3 = (bubble lst2)
      in if lst3 = lst2 then lst3
      else sort_of_bubble lst3
;;

sort_of_bubble [150;2;14;56;3;4];;
sort_of_bubble [100;123;3;6;38;394;4441;5;0];;   


(*課題２-１*)  
let differential x f =
  ( f (x +. 0.00000001) -. f x ) /. 0.00000001
;;

let f x = x *. x
in differential 3. f
;;

(*課題２-２*)
let rec ext x y f =  (*x,yはそれぞれ極値を求める上限、下限の設定*)
  if x > y then failwith "Error" 
  else if (differential (x -. 0.01) f) *.(differential (x +. 0.01) f) < 0. then
    x
  else ext (x +. 0.1) y f
;;

ext (-20.) 20. (fun x -> x *. x);; 
ext (-20.) 20. (fun x -> x *. x *. x);; 


(*課題３-１*)
let rec trapezoid a b high = 
  (a +. b) *. high /. 2.
;;

trapezoid 2. 3. 10.;; 

(*課題３-２*)
let rec integral a b f = 
  if a < b then
    (f a *. 0.01) +. integral (a +. 0.01) b f
  else 0.
;;

let f x = x *. x
in integral 1. 3. f;;


(*課題４*)
let rec recursion n = 
  if n mod 2 = 0 then recursion (n / 2) 
  else if n = 1 then 1 
  else recursion ((n * 3) + 1) 
;;

recursion 6;;
recursion 7;;

(*課題４-２考察：ステップ数出力*)
let rec recursion n = 
  if n mod 2 = 0 then recursion (n / 2) + 1
  else if n = 1 then 0
  else recursion ((n * 3) + 1) + 1
;;

recursion 6;;
recursion 7;;


(*課題５*)
(*サブ関数１：２点間の距離を計算する関数*)
let calculate_length (x1 ,y1) (x2 , y2) = 
  sqrt ((x1 -. x2) *. (x1 -. x2) +. (y1 -. y2) *. (y1 -. y2))
;; 

(*サブ関数２：基準点から最も遠い点の出力*)
let rec max (x1 ,y1) lst =
  match lst with 
    [] -> failwith "Error"
  | (x2 , y2) :: (x3 , y3):: rest -> 
      if calculate_length(x1 , y1) (x3 , y3) > calculate_length (x1 , y1) (x2 , y2) 
      then max (x1, y1) ((x3, y3)::rest)  
      else max (x1 , y1) ((x2 , y2) :: rest)
  | (x4, y4) :: rest ->  (x4, y4) 
;; 

(*サブ関数３：リストからn番目の要素の出力*)
let rec posl n lst = 
  match (n , lst) with
    (1 ,a :: rest) -> a
  | (n' , a :: rest) when n' > 0 ->( posl (n-1) rest ) ;; 

(*サブ関数４：リストから指定した要素の出力*)
let rec pull_out n lst =
  match (n , lst) with 
  | (_ , []) -> []
  | (n , a :: rest) -> 
      if n = a then (pull_out n rest)
      else a :: (pull_out n rest)
;;

(*メイン関数１：最長並び順を出力*) 
let shuffle lst = 
  let rec shuffle2 lst = 
    match lst with 
      [] -> []
    |[(x1 , y1)] -> []
    |(x1 , y1) :: rest ->
        (max (x1 , y1) rest) :: shuffle2 ( max (x1 , y1) rest :: (pull_out (max (x1 , y1) rest) rest)) 
  in posl 1 lst :: shuffle2 lst
;;

shuffle [(5.,5.); (15.,10.); (10.,33.); (13.,4.); (1.,12.)];;

(*メイン関数２：最長並び順の距離を出力*)
let  max_distance lst = 
  let newlst = (shuffle lst) 
  in let rec max_distance2 newlst  = 
       match newlst with 
         [] -> 0.
       | [(x1 , y1)] -> calculate_length (posl 1 lst) (x1 , y1)
       | [(x1 , y1); (x2 , y2)] -> 
           calculate_length (x1 , y1) (x2 , y2) +. max_distance2 [(x2 , y2)]
       | (x1 , y1) :: (x2 , y2) :: rest ->
           
           (calculate_length (x1 , y1) (x2 , y2)) +. max_distance2 ((x2 , y2) :: rest)
  in max_distance2 newlst
;;

max_distance [(5.,5.); (15.,10.); (10.,33.); (13.,4.); (1.,12.)];;


(*課題６*)
let fib n =
  if n = 0 then failwith "Error"
  else 
    let rec fib2 n = 
      if n = 0 then 1
      else if n = 1 then 1 
      else fib2 (n-1) + fib2 (n-2)
    in fib2 n
;;
  
fib 0 ;;
fib 1 ;; 
fib 7 ;;
fib 8 ;;








