(*１４．maximum*)
let rec maximum lst = 
  match lst with 
    ([]) -> failwith "Error"
  |(a :: []) -> a
  |(a :: b :: rest) -> 
      if rest = [] then 
        if a > b then a
        else b
      else if a > b then 
        maximum (a :: rest)
      else maximum (b :: rest)
;;

maximum [3; 2; 5; 1];;

maximum ["abc"; "sdf"];;

maximum [];;
