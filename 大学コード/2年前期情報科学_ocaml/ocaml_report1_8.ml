(*８．inslist*)
let rec inslist n m lst = 
  match (n , m , lst) with
    (0 , m , lst) -> failwith "Error"
  | (1 , m , lst) -> m :: lst
  | (n , m , a :: rest) -> a :: (inslist (n - 1) m rest)
;;

inslist 2 "*" ["A"; "B"; "C"; "D"; "E"];;

inslist 6 "*" ["A"; "B"; "C"; "D"; "E"];;

inslist 1 "+" [];;

inslist 1 "+" ["A"];;

inslist 0 "+" ["A"];;