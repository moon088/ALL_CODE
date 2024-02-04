(*課題４*)
let rec recursion n = 
  if n mod 2 = 0 then recursion (n / 2) 
  else if n = 1 then 1 
  else recursion ((n * 3) + 1) 
;;

recursion 6;;
recursion 7;;

(*課題４-２考察：ステップ数出力*)
let rec recursion n = 
  if n mod 2 = 0 then recursion (n / 2) + 1
  else if n = 1 then 0
  else recursion ((n * 3) + 1) + 1
;;

recursion 6;;
recursion 7;;


