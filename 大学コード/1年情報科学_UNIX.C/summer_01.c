#include <stdio.h>

int main () {
    int a = 2021;     /*整数型変数aの宣言と代入*/
    int b = a % 400;  /*整数型変数bの宣言と代入*/
    int c = a % 100;  /*整数型変数cの宣言と代入*/
    int d = a % 4;    /*整数型変数dの宣言と代入*/
         
    if( b == 0 ) {                                /*変数bが０の時の条件分岐*/
      printf( "%d年は閏年です\n" , a );           /*2021年は閏年です　を表示*/
   }else if ( c == 0 ) {                          /*変数cが０の時の条件分岐*/
      printf( "%d年は閏年ではありません\n" , a ); /*2021年は閏年ではありません　を表示*/
   }else if ( d == 0 ) {                          /*変数dが０の時の条件分岐*/
      printf( "%d年は閏年です\n" , a );           /*2021年は閏年です　を表示*/           
   }else {                                        /*そのほかの場合の条件分岐*/
       printf( "%d年は閏年ではありません\n" , a ); /*2021年は閏年ではありません　を表示*/
    }
}
