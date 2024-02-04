(*課題３*)
module Vector = struct
  exception Empty
  
  let vempty = []
  
  let rec at n lst = 
    match (n , lst) with
      (_ , []) -> raise Empty
    |(0 , a :: rest) -> a
    |(n , a :: rest) -> at (n - 1) rest
  
  let vector lst = lst
  
  let rec vlength lst = 
    match lst with
      [] -> 0
    |a :: rest -> 1 + (vlength rest)
  
  let vshow lst =
    let rec print_list lst= 
      match lst with
        [] -> ()
      | a :: rest -> print_int a ; print_string "," ; print_list rest
    in print_list lst
            
  let isvempty x = 
    if x = vempty then true 
    else false

  
end


open Vector;;
let a0 = vempty;;
isvempty a0;;
let a1 = vector [1;2;3;4];;
isvempty a1;;
vlength a1;;
at 3 a1;;
at 4 a1;;
vshow a1;;











