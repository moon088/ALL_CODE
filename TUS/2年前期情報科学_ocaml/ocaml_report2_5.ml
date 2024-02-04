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
