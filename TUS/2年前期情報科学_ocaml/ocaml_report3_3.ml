(*課題４*)
module Student:
sig
  exception Not_found 
  type date
  val empty : date
  val add : int -> string -> date -> date
  val find : string -> date -> int
  val show : date -> unit
  val is_empty : date -> bool
end
=  struct
  
  exception Not_found
 
  type date = Nil | Cell of int * string * date
    
  let empty = Nil
  
  let add num name lst = 
    match lst with 
      Nil -> Cell (num , name , Nil) 
    |Cell (num' , name' , rest) -> Cell (num , name , lst )
  
  let rec find name lst = 
    match lst with
      Nil-> raise Not_found 
    |Cell (num , name', rest) -> 
        if name' = name then num
        else find name rest

  let rec show lst =
    let rec print_date lst = 
      match lst with
        Nil -> print_string ":"
      | Cell (num , name , rest) ->
          print_int num ; print_string ":" ; print_string name ; 
          print_newline () ; print_date rest
    in print_date lst

  let is_empty lst = 
    if lst = empty then true
    else false
end;;

open Student;;
let a0 = empty;; 
let a1 = add 1 "takimoto" a0;;
let a2 = add 2 "matsuzawa" a1;;
let a3 = add 3 "katsurada" a2;;
find "takimoto" a3;;
find "katsurada" a3;;
find "takeda" a3;;
show a3;;
