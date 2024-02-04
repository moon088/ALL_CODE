

let question = App ("male" , [Var"X"] );;  (*  male (X)  *)

let question = App ( "parents" ,   [Atom ("namihei")  ;  Var("Y")]     )    ;  ;;  (*  parents (namihei , X)  *)


(*eval (program , question) *)
(*課題１の解答*)
let program = [ [App( "male" ,   [Atom ("namihei")])] ;
                [App( "male" ,   [Atom ("katsuo")]) ];
                [App( "male" ,   [Atom ("tara")]) ];
                [App( "male" ,   [Atom ("masuo")]) ];
                [App( "female" ,   [Atom ("fune")])];
                [App( "female" ,   [Atom ("wakame")])] ;
                [App( "female" ,   [Atom ("sazae")])] ;
                [App( "father" ,   [Atom ("masuo") ; Atom ("tara")]   )] ;
                [App( "father" ,   [Atom ("namihei") ; Atom ("sazae")]   )];
                [App( "father" ,   [Atom ("namihei") ; Atom ("katsuo")]   )];
                [App( "father" ,   [Atom ("namihei") ; Atom ("wakame")]   )];
                [App( "mother" ,   [Atom ("sazae") ; Atom ("tara")]   )];
                [App( "mother" ,   [Atom ("fune") ; Atom ("sazae")]   )];
                [App( "mother" ,   [Atom ("fune") ; Atom ("katsuo")]   )];
                [App( "mother" ,   [Atom ("fune") ; Atom ("wakame")]   )];
                [App( "parents" ,   [Var ("X")  ;  Var("Y")]     )    ;  App(  "father"  , [Var("X")   ;   Var("Y")]  ) ];
                [App( "parents" ,   [Var ("X")  ;  Var("Y")]     )    ;  App(  "mother"  , [Var("X")   ;   Var("Y")]  ) ];
                [App( "son" ,   [Var ("X")  ;  Var("Y")]     )    ;  App(  "parents"  , [Var("Y")   ;   Var("X")]  )  ;   App(  "male"  , [Var("X")]  )];
                [App( "daughter" ,   [Var ("X")  ;  Var("Y")]     )    ;  App(  "parents"  , [Var("Y")   ;   Var("X")]  )  ;   App(  "female"  , [Var("X")]  )];
                [App( "grandfather" ,   [Var ("X")  ;  Var("Y")]     )    ;  App(  "parents"  , [Var("Z")   ;   Var("Y")]  )  ;   App(  "father"  , [Var("X") ; Var("Z")]  )];
                [App( "grandmother" ,   [Var ("X")  ;  Var("Y")]     )    ;  App(  "parents"  , [Var("Z")   ;   Var("Y")]  )  ;   App(  "mother"  , [Var("X") ; Var("Z")]  )];

              ] ;;









(*課題３　改造版*)
module Evaluator =
struct


  type ast = |Atom of string			
             |Var of string			
             |App of string * ast list
        
  module P = Printf
 
  exception Compiler_error


  let rec print_ast ast = 
    match ast with
    |(App(s, hd::tl)) -> (P.printf "App(\"%s\",[" s ; print_ast hd; List.iter (fun x -> (print_string ";"; print_ast x)) tl; print_string "])")
    |(App(s, [])) -> P.printf "App(\"%s\",[])" s
    |(Atom s) -> P.printf "Atom \"%s\"" s
    |(Var s) -> P.printf "Var \"%s\"" s

  let print_ast_list lst = 
    match lst with
    |(hd::tl) -> (print_string "["; print_ast hd; List.iter (fun x -> (print_string ";"; print_ast x)) tl; print_string "]")
    |[] -> print_string "[]" ;;

  let sub name term =
    let rec mapVar ast = match ast with
      |(Atom x) -> Atom(x)
      |(Var n) -> if n=name then term else Var n
      |(App(n, terms)) -> App(n, List.map mapVar terms)
    in mapVar

  let mgu (a,b) =

    let rec ut (one, another, unifier) = 
      match (one, another) with

      |([], []) -> (true, unifier)

      |(term::t1, Var(name)::t2) ->
          let r = fun x -> sub name term (unifier x) in
          ut(List.map r t1, List.map r t2, r)

      |(Var(name)::t1, term::t2) ->
          let r = fun x -> sub name term (unifier x) in
          ut(List.map r t1, List.map r t2, r)

      |(Atom(n)::t1, Atom(m)::t2) ->
          if n=m then ut(t1,t2,unifier) else (false, unifier)

      |(App(n1,xt1)::t1, App(n2,xt2)::t2) ->
          if n1=n2 && List.length xt1 = List.length xt2 then
            ut(xt1@t1, xt2@t2, unifier)
          else (false, unifier)

      |(_,_) -> (false, unifier);
    in ut ([a],[b], (fun x -> x)) 

  let succeed query = (print_ast query; true)

  let rename ver term =
    let rec mapVar ast = 
      match ast with
      |(Atom x) -> Atom(x)
      |(Var n) -> Var(n^"#"^ver)
      |(App(n, terms)) -> App(n, List.map mapVar terms)
    in mapVar term

  let rec solve (program, question, result, depth) = 
    match question with
      [] -> succeed result
    |goal::goals ->
        let onestep _ clause =
          match List.map (rename (string_of_int depth)) clause with
          |[] -> raise Compiler_error
          |head::conds ->
              let (unifiable, unifier) = mgu(head,goal) in
              if unifiable then
                solve (program, List.map unifier (conds@goals), unifier result, depth+1)
              else true
        in List.fold_left onestep true program


  let eval (program, question) = solve(program, [question], question, 1) 


  let rec peanuts (program, question, result, depth) =
    match question with
    |[k::rest] -> if rest = [] then solve (program , k, result, depth)
        else solve (program , k, result, depth)  peanuts (program, rest, result, depth) ;; 



end ;;
