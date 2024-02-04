(*１．dellt*)
let rec dellt n  lst = 
  if n >= 0
  then if n > 0 then
      match lst with
        []-> []
      | first :: rest -> dellt (n-1) rest
    else lst
  else failwith "Error";;


    