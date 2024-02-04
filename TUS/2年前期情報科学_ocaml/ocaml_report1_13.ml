(*１３assoc*)
let rec assoc n lst = 
  match (n , lst) with
    (n , []) -> failwith "Not found..."
  | (n , (a , b):: rest)-> 
      if n = a then b
      else if n = b then a 
      else assoc n rest  
          
;;

assoc 33 [(3,4); (33,5); (11,2); (55,1)];;

assoc 2 [(3,4); (33,5); (11,2); (55,1)];;

assoc "03" [("Kyoto", "075"); ("Osaka", "06"); ("Tokyo", "03")];;

assoc "Kyoto" [("Kyoto", "075"); ("Osaka", "06"); ("Tokyo", "03")];;

assoc 6 [(3,4); (33,5); (11,2); (55,1)];;