(*１０．merge*)
let rec merge lst1 lst2 =
  match (lst1 , lst2) with 
    (a:: rest1 , b :: rest2) -> 
      a :: b :: merge rest1 rest2
  | ([] , lst2) -> lst2 
  | (lst1 , []) -> lst1 
;;


merge [1; 2; 3] [4; 5; 6];;

merge ["A"; "B"] [ "C"; "D"; "EF"; "GH"];;



      