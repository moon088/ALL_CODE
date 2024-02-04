(*７．chglist*)
let rec chglist (n , m) lst =
  match (n , m , lst) with 
    (_ , _ , []) -> []
  | (n , m , a :: rest) -> if n = a then m :: chglist (n , m) rest
      else  a :: chglist (n , m) rest
;;

chglist ("A", "*") ["1"; "A"; "2"; "B"; "A"; "A"; "3"; "4"];;




