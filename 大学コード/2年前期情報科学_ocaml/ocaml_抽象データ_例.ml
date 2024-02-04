type 'a stack = 
    Nil
  |Cell of 'a * 'a stack;;

exception Empty;;(*右にスタック、左端の挿入左の抽出操作*)
let create = Nil;;
let push st x = Cell (x , st);; (*左cell一つ追加*)
let pop = (*右全部(2番目以降のcellすべて)抽出*)
  function  Nil -> raise Empty 
          |Cell (_ , a) -> a;;
let top = (*左端のcellの値一つ抽出*)
  function Nil -> raise Empty 
         |Cell (x , _) -> x;;



exception Empty;;
let create = [];;
let pop lst = 
  match lst with 
    [] -> raise Empty 
  | n :: rest -> n;;

(*左の挿入右の抽出*)
exception Empty;;
type 'a queue = Nil 
              |Cell of 'a *'a queue;;
let create = Nil;;
let rec enqueue x q = Cell (x , q);; (*左cell一つ追加*)
let rec dequeue = (*右一つ消去（１からn-1番目までcell表示)*)
  function Nil -> raise Empty 
         |Cell (x , xs) -> 
             if xs = Nil then Nil
             else Cell (x , dequeue xs);;
let rec front = (*右端の値一つ抽出*)
  function Nil -> raise Empty
         | Cell (x , xs) -> 
             if xs = Nil then x
             else front xs;;

exception Empty;;
let create = [];;
let enqueue x q = x :: q;; (*左cell一つ追加*)
let back q = (*左抽出*)
  match q with 
    [] -> raise Empty
  |n :: rest -> n;;
let rec front q = (*右抽出*)
  match q with
    [] -> raise Empty
  |n :: rest -> 
      if rest = [] then n
      else front rest;;
let rec dequeue q = (*右消去*)
  match q with
    [] -> raise Empty 
  |n :: rest -> 
      if rest = [] then []
      else n :: dequeue rest;;
  
  
pop [2];;
  
  
  





