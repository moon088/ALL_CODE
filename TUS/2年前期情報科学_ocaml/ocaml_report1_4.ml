(*４．posl*)
let rec posl n lst = 
  match (n , lst) with
    (1 ,a :: rest) -> a
  | (n' , a :: rest) when n' > 0 ->( posl (n-1) rest ) ;;

posl 3 ["AB"; "C"; "DEF"; "G"; "H"; "IJ"];;

posl 2 [ 1; 2; 3; 4; 5];;

posl 0 [ 1; 2; 3; 4; 5];;
