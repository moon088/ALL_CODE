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




