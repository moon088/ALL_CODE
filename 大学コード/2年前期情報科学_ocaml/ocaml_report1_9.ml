(*９．replicate*)
let rec replicate n lst = 
  match(n , lst) with
    (1 , _) -> [lst]
  |(n , _) -> lst ::(replicate (n - 1) lst)
;;

replicate 3 ["A"];;

replicate 5 "A";;

replicate 3 ["1"; "#"];;

