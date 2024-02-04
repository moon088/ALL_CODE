(*５．divlist*)
let rec divlist lst1 lst2 = 
  match (lst1 , lst2) with
    ([] , []) -> []
  |(a :: rest1 , b :: rest2) -> 
      (a / b) :: divlist rest1 rest2 ;; 


divlist [12; 8; 9; 7] [2; 4; 3; 7];;




                                   