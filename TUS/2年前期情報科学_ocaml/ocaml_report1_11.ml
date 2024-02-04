(*１１．inside_length*)
let rec inside_length lst =
  match lst with
    [] -> 0
  | first :: rest1 -> 
      let rec inside_inside_length first = 
        match first with
          [] -> 0
        | first_first :: rest2 -> 1 + (inside_inside_length rest2)  
      in (inside_inside_length first) + (inside_length rest1)
;;
  
  
  
inside_length[[1; 2; 3]; [4; 5]; [6]; [7; 8; 9; 10]];;

inside_length[["A"; "B"]; [ "C"; "D"]; ["EF"; "GH"]];;
