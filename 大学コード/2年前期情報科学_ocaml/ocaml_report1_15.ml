(*１５．index*)
let rec index lst n = 
  match (n , lst) with 
    (n , []) -> failwith "Error"
  | (n , a :: rest) -> if not(n = a) then 1 + (index rest n)
      else + 0
;;