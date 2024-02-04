type gakusei_t = {namae : string; tensuu : int; seiseki : string};;
exception Error;;

let rec max_score lst = match lst with
    [] -> raise Error
  | first :: rest -> 
      match first with
        {namae = n; tensuu = t; seiseki = s} -> 
          let t_max = max_score rest in
          if t > t_max then t
          else t_max;;


let gakusei1 = {namae = "asai"; tensuu = 30;seiseki = "B"};;
let gakusei2 = {namae = "tanaka"; tensuu = 70;seiseki = "S"};;
let gakusei3 = {namae = "yamada"; tensuu = 50;seiseki = "A"};;

max_score [gakusei1;gakusei2;gakusei3];;
(*max_score [{"a"; 10; "s"}; {"b"; 70; "a"}; {"c"; 50; "b"}];;ダメ*)

let hyouka_list lst = 
  let hyouka gakusei = match gakusei with 
      {namae = n; tensuu = t; seiseki = s} -> 
        {namae = n; tensuu = t; seiseki = if t >= 80 then "A" 
                                  else if t >= 70 then "B" 
                                  else if t >= 60 then "C"
                                  else "D"}
  in List.map hyouka lst;;

let count_A lst = 
  let seiseki_A gakusei = match gakusei with
      {namae = n; tensuu = t; seiseki = s} -> s = "A"
  in List.length (List.filter seiseki_A lst)
;;
count_A [gakusei1;gakusei2;gakusei3];;


let heikin_A lst = (*成績Aの人の平均点を出す*)
  let seiseki_A gakusei = match gakusei with
      {namae = n; tensuu = t; seiseki = s} -> s = "A" in
  let lst_A = List.filter seiseki_A lst in
  let add gakusei goukei = match gakusei with
      {namae = n; tensuu = t; seiseki = s} -> t + goukei
  in (List.fold_right add lst_A 0) / (List.length lst_A)
;;

[1;2] @ [3] @ [3;4];;

type 'a option = None | Some of 'a;;

let add x = fun y -> x + y;;




