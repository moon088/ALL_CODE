(*６．mul2list*)
let rec mul2list lst = 
  match lst with
    a :: b :: rest1 -> if rest1 = [] then [a * b]
      else (a * b) :: mul2list (b :: rest1) 
             
;;


mul2list [1; 2];;

mul2list [1; 2; 3];;

mul2list [1; 2; 3; 4; 5];;

