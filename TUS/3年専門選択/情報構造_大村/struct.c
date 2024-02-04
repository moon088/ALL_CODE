#include <stdio.h>


int main() {
  typedef struct r{ /*構造体  複数のデータを同時に代入可、メモリ消費大*/
    int S;
    float T;
  }R;  /*Rという構造体名*/

  R b, c , *pb;
  b.S = 10; /*メンバー、.でアクセス*/
  b.T = 0.5;
  printf("%d\n" , b.S);
  c = b;
  printf("%d\n" , c.S);
  
  pb = &b;/*構造体をアロー演算子で参照*/
  printf("S: %d  T: %f\n" , (*pb).S, (*pb).T );

  typedef union u{    /*共用体 複数同時代入不可、メモリ消費小*/
    int S;
    float T;
  }U;

  U a;
  a.S = 5;
  printf("S: %d T:%f\n" , a.S, a.T);
  a.T = 0.5;  /*Sも変更される*/
  printf("S: %d T:%f\n" , a.S, a.T);

  long d = 1000; /*値呼び*/
  val(d); /*ここで呼び出しても1000*/
  printf("%d\n" , d);

  long e = 1000; /*参照呼び*/
  ref(&e);
  printf("%d\n" , e);

  


}



void val(long b){ /*値呼び関数*/
  b+= 100;  /*ここでは1100*/
  printf("%d\n" , b);
}

void ref(long *p){ /*参照呼び関数*/
  *p += 100;
  printf("%d\n" , *p);
  
}
