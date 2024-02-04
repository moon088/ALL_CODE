(*課題６*)
let fib n =
  if n = 0 then failwith "Error"
  else 
    let rec fib2 n = 
      if n = 0 then 1
      else if n = 1 then 1 
      else fib2 (n-1) + fib2 (n-2)
    in fib2 n
;;
  
fib 0 ;;
fib 1 ;; 
fib 7 ;;
fib 8 ;;
  