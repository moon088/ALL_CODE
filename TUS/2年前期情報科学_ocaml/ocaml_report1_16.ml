(*１６集合の計算*)
(*1.共通集合*)
let rec inter l1 l2 = 
  let l3 = l2 in
  let rec inter2 l1 l3  = 
    match (l1, l3) with
      ([] , l3) -> []
    |(a :: rest1 ,[]) -> inter rest1 l2 
    |(a :: rest1 , b :: rest2) -> 
        if a = b then a :: inter rest1 l2
        else inter2 l1 rest2 
  in inter2 l1 l2

;;

inter [10 ; 15 ;2 ;3 ;59 ;12] [12; 14; 3 ;42 ;10 ];;

(*２．和集合*)
let  rec append l1 l2 = (*二つのリストを結合したリストを返す関数appendを定義*)
  match l1 with
    [] -> l2
  | first :: rest -> first :: (append rest l2)
;;
let rec union l1 l2 =
  let l3 = l2 in 
  let rec union2 l1 l3 =
    match (l1 , l3) with 
      ([] , []) -> []
    |([] , l3) -> append l3 (union2 [] [])
    |(a :: rest1 , []) -> a :: union rest1 l2 
    |(a :: rest1 , b :: rest2) -> 
        if a = b then union rest1 l2
        else union2 l1 rest2
               
  in union2 l1 l2

;;

union [10; 15; 2; 3; 59; 12] [9 ; 12; 14; 3; 42; 10;11];;


(*３．差集合(l1 \ l2の場合)*)
let rec diff l1 l2 =
  let x = inter l1 l2 in
  let l3 = l2 in
  let rec diff2 x l3 =         (*和集合zから集合yを引く*)
    match (x , l3) with
      (a :: rest1 , []) -> a :: diff rest1 l2 
                    
    |([] , _) -> []  
    |(a :: rest1 , b :: rest2) -> 
        if  a = b then diff rest1 l2
        else diff2 l1 rest2 
  in diff2 l1 l2
;;
            
diff [10 ; 15 ;2 ;3 ;59 ;12] [12; 14; 3 ;42 ;10 ];;  
diff [10; 15; 2; 3; 59; 12; 39 ;40] [9 ; 12; 14; 3; 42; 10;11];;
 




