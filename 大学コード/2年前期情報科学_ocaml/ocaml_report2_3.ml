(*課題３-１*)
let rec trapezoid a b high = 
  (a +. b) *. high /. 2.
;;

trapezoid 2. 3. 10.;; 

(*課題３-２*)
let rec integral a b f = 
  if a < b then
    (f a *. 0.01) +. integral (a +. 0.01) b f
  else 0.
;;

let f x = x *. x
in integral 1. 3. f;;



