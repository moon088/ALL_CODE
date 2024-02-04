(*課題２-１*)  
let differential x f =
  ( f (x +. 0.00000001) -. f x ) /. 0.00000001
;;

let f x = x *. x
in differential 3. f
;;

(*課題２-２*)
let rec ext x y f =  (*x,yはそれぞれ極値を求める上限、下限の設定*)
  if x > y then failwith "Error" 
  else if (differential (x -. 0.01) f) *.(differential (x +. 0.01) f) < 0. then
    x
  else ext (x +. 0.1) y f
;;

ext (-20.) 20. (fun x -> x *. x);; 
ext (-20.) 20. (fun x -> x *. x *. x);; 