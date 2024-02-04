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
    |[] -> print_string "[]" 

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

  let rename ver term =
    let rec mapVar ast = 
      match ast with
      |(Atom x) -> Atom(x)
      |(Var n) -> Var(n^"#"^ver)
      |(App(n, terms)) -> App(n, List.map mapVar terms)
    in mapVar term 
      
  let rec print_succeed lst= (*3*)
    match lst with
    |[] ->P.printf ")"
    |(Atom s)::rest -> P.printf (",%s") s; print_succeed rest
    | _ -> ()
  
  let succeed query =  (*3*)
    let rec succeed2 query = match query with
      |App (_ , []) ->  () ;
      |App (predicate , (Atom s)::rest ) -> P.printf ("%s") predicate; P.printf "(" ; P.printf ("%s") s ; print_succeed rest
      | _ -> ()
    in succeed2 query ; true
                      
  let rec solve (program, question, result, depth) = 
    match question with
    |[] -> succeed result  
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


end ;;



(*字句解析*)
module Lexer = struct 
  type token = CID of string | VID of string | NUM of string 
             | TO | IS | QUIT | OPEN | EOF | ONE of char 
  module P = Printf 
  exception End_of_system
  let count  = ref 1 
  let _ISTREAM = ref stdin
  let ch = ref [] 
  let read () = match !ch with [] -> input_char !_ISTREAM
                             | h::rest -> (ch := rest; h)
  let unread c = ch := c::!ch
  let lookahead () = try let c = read () in unread c; c with End_of_file -> '$'
  let rec integer i =
    let c = lookahead () in
    if (c >= '0' && c <= '9') then
      integer (i^(Char.escaped (read ())))
    else i
  and identifier id =
    let c = lookahead () in
    if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') ||
        (c >= '0' && c <= '9') || c == '_') then
      identifier (id^(Char.escaped (read ())))
    else id
  and native_token () =
    let c = lookahead () in
    if (c >= 'a' && c <= 'z') then 
      let id = identifier "" in 
      match id with
        "is" -> IS
      | "quit" -> QUIT
      | "open" -> OPEN
      | _ -> CID (id)
    else if (c >= 'A' && c <= 'Z') then VID (identifier "")
    else if (c >= '0' && c <= '9') then NUM (integer "")
    else if (c = ':') then (read() ; if (lookahead()=='-') then (read(); TO) else ONE (c)) 
    else ONE (read ())
  and gettoken () = 
    try 
      let token = native_token () in
      match token with
        ONE ' ' ->  gettoken ()
      | ONE '\t' -> gettoken ()
      | ONE '\n' -> count := !count + 1 ; gettoken () 
      |  _ ->  token
    with End_of_file -> EOF 
  
  let print_token tk =
    match tk with
      (CID i) -> P.printf "CID(%s)" i 
    | (VID i) -> P.printf "VID(%s)" i
    | (NUM i) -> P.printf "NUM(%s)" i
    | (TO) -> P.printf ":-"
    | (QUIT) -> P.printf "quit"
    | (OPEN) -> P.printf "open"
    | (IS) -> P.printf "is"
    | (EOF) -> P.printf "eof"
    | (ONE c) -> P.printf "ONE(%c)" c 
    
end 


(*構文解析*) 
module Parser = struct
  module L = Lexer 
  module E = Evaluator
  let prog = ref [[E.Var ""]] (*追加*)
  let tok = ref (L.ONE ' ')
  let getToken () = L.gettoken ()
  let advance () = (tok := getToken();(* L.print_token (!tok)*)) (*L.print_token (!tok) をコメントアウトした*)
  exception Syntax_error
  let error () = raise Syntax_error
  let check t = match !tok with
      L.CID _-> if (t = (L.CID "")) then () else error()
    | L.VID _-> if (t = (L.VID "")) then () else error()
    | L.NUM _-> if (t = (L.NUM "")) then () else error()
    | tk -> if (tk=t) then () else error()
  let eat t = (check t; advance())
  let rec clauses() = match !tok with
      L.EOF -> () ; []
    | _  -> (let c1 = clause() in
             let c2 = clauses() in 
             (c1 :: c2))
  and clause() = match !tok with
      L.ONE '(' -> let t1 = term() in eat(L.ONE '.') ;[t1]
    | _ ->let t1 = predicate() in
        let t2 = to_opt()
        in eat(L.ONE '.') ; (t1::t2)
  and to_opt() = match !tok with
      L.TO -> (eat(L.TO);let t1 = terms() in (t1))
    | _ -> []
  and command() = match !tok with
      L.QUIT -> exit 0
    | L.OPEN -> (eat(L.OPEN); 
                 match !tok with
                   L.CID s -> (eat(L.CID ""); check (L.ONE '.'); 
                               L._ISTREAM := open_in (s^".pl"); advance();
                               prog := clauses(); close_in (!L._ISTREAM))
                 | _ -> error())
    | _ -> let t = term() in (check(L.ONE '.'); let _ = E.eval(!prog, t) in ())(*変更*)
  and term() = match !tok with
      L.ONE '(' -> eat(L.ONE '(');
        let u1 = term() in eat(L.ONE '('); (u1) 
    | _ -> predicate()
  and terms() = let u1 = term() in let u2 = terms'() in [u1]@u2
  and terms'() = match !tok with
      L.ONE ',' ->  eat(L.ONE ',');
        let u1 = term() in let u2 = terms'() in
        [u1]@u2
    | _ -> []
  and predicate() = match !tok with
    |L.CID d -> (eat(L.CID "") ; eat(L.ONE '(');
                 let s1 = args() in eat(L.ONE ')');
                 E.App(d,s1)) 
    |_ -> error ()
  and args() = let ext1 = expr() in let s1 = args'() in [ext1]@s1
  and args'() = match !tok with
      L.ONE ','->  eat(L.ONE ',');
        let ext1 = expr() in let s1 = args'() in
        [ext1]@s1
    | _ -> [] 
  and expr() = match !tok with
      L.ONE '(' -> eat(L.ONE '(');let ext1 = expr() in eat(L.ONE ')');ext1
    |L.ONE '[' -> eat(L.ONE '[');let list1 = list() in eat(L.ONE ']');list1
    |L.CID s -> eat(L.CID "");let tail1 = tail_opt(s) in tail1
    |L.VID s -> eat(L.VID "");E.Var s
    |L.NUM n -> eat(L.NUM "");E.Atom n
    | _ -> error()
  and tail_opt s =  match !tok with 
      L.ONE '(' -> eat(L.ONE '(') ; let arg1 = args() in eat(L.ONE ')') ; E.App (s,arg1)
    |_ -> E.Atom s
  and list() = match !tok with
      L.ONE ']'-> E.Atom "nil"
    | _ -> let ext1 = expr() in 
        let l1 = list_opt() in E.App("cons",[ext1;l1])
  and list_opt() = match !tok with
      L.ONE '|' -> eat(L.ONE '|');let i1 = id() in i1
    | L.ONE ',' -> eat(L.ONE ','); let p1 = list() in p1
    | _ -> E.Atom "nil"
  and id() = match !tok with
      L.CID s -> eat(L.CID ""); E.Atom s
    | L.VID s -> eat(L.VID ""); E.Var s
    | L.NUM n -> eat(L.NUM ""); E.Atom n
    | _ -> error () 
end 

let rec run() =
  print_string "?- ";
  while true do
    flush stdout; Lexer._ISTREAM := stdin;
    Parser.advance(); Parser.command(); print_string "\n?- "
  done 
  
let run' () =  
  try let c = run () in c
  with  Parser.Syntax_error -> print_string "\n"; print_string "文法エラー:" ; Printf.printf ("%d") !Lexer.count; print_string "行目"; print_string "\n?-"
  
let _ = run'() 

