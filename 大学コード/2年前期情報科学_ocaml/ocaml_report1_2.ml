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

