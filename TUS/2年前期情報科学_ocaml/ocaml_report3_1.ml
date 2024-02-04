(*課題２*) 
(*10,2,5,8,12,3,1*)
module List = struct
  type 'a list = Nil | Cell of 'a * 'a list
  exception Empty
  let create = Nil 
  let unshift a lst = Cell (a , lst)
  let shift = function 
      Nil -> raise Empty
    |Cell (_ , a) -> a
 
  let rec push a lst=        
    match lst with
      Nil -> Cell (a , Nil) 
    | Cell (x , rest) -> Cell (x , push a rest)    
  
  let rec pop lst = 
    match lst with 
      Nil -> raise Empty 
    |Cell (x , rest) -> 
        if rest = Nil then Nil
        else Cell (x , pop rest)
                 
  let rec size lst = 
    match lst with
      Nil -> 0
    |Cell (a , rest) -> 1 + size rest 
    
  let rec max lst = 
    match lst with
      Nil -> raise Empty
    |Cell (x , Nil) -> x
    |Cell (x , Cell (y , rest)) ->
        if x > y then max (Cell (x , rest))
        else max (Cell (y , rest))
  
  let rec min lst =
    match lst with
      Nil -> raise Empty
    |Cell (x , Nil) -> x
    |Cell (x , Cell (y , rest)) -> 
        if x > y then min (Cell (y , rest))
        else max (Cell (x , rest))
            
  let get x lst =
    let n = 0 in
    let rec count n lst = 
      match lst with
        Nil -> raise Empty
      |Cell (a , rest) -> 
          if x = n then a
          else count (n + 1) rest
    in count n lst
      
  let indexOf x lst =
    let n = 0
    in let rec indexOf_2 n lst =
         match lst with
           Nil -> -1
         |Cell (a , rest) -> 
             if a = x then n
             else indexOf_2 (n + 1) rest
    in indexOf_2 n lst
      
  let rec set x y lst = 
    match lst with 
      Nil -> raise Empty
    |Cell (a , Nil) -> 
        if a = x then Cell (y , Nil)
        else Cell (a , Nil)
    |Cell (a , rest) -> 
        if a = x then Cell (y , set x y rest)
        else Cell (a , set x y rest)
      
  let rec remove x lst = 
    match lst with
      Nil -> raise Empty
    |Cell (a , Nil) -> 
        if a = x then Nil
        else Cell (a , Nil)
    |Cell (a , rest) -> 
        if a = x then remove x rest
        else (Cell (a , remove x rest))
  
  let rec concat l1 l2 =
    match l1 with
      Nil -> l2
    |Cell (a , Nil) -> Cell (a , l2)
    |Cell (a , rest) -> Cell (a , concat rest l2)
  
end

open List;;
let l1 = push 8 (unshift 10 (push 5 (unshift 2 create)));;
let l2 = push 1 (unshift 12 (unshift 2 create));;
let l = concat l1 l2;;
shift l;;
pop l;;
size l2;;
max l2;;
min l2;;
get 3 l;;
indexOf 12 l;;
set 1 0 l;;
remove 5 l;;












