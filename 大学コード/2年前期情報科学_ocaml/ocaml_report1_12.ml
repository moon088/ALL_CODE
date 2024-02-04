(*１２．concat*)

let rec append l1 l2 =
  match l1 with
    [] -> l2
		| first :: rest -> first :: (append rest l2)
;;

let rec concat lst =
  match lst with
    [] -> [] 
  | a :: rest -> let rec append l1 l2 = 
                   match l1 with
                     [] -> l2
                   | first :: rest -> first :: (append rest l2)
      in append a (concat rest)
;;
      
  
concat [[0; 3; 4]; [2]; [0]; [5; 0]];;



