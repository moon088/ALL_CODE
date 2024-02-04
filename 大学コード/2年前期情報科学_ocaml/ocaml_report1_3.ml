(*３．find*)
let rec find n lst = 
  match (n , lst) with
    (n , a :: rest) -> if n = a then true
      else find n rest
  | (_ , []) -> false ;;

find 3 [1; 2; 3; 4; 5; 6];;

find 1 [2; 3; 4; 5];;

