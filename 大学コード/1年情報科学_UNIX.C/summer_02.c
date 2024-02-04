#include <stdio.h>

int main () {
    int a = 10;    /*整数型変数aの宣言と代入*/ 
    int b = 2;     /*整数型変数bの宣言と代入*/
    int c = a + b; /*整数型変数cの宣言と代入*/
    int d = a * b; /*整数型変数dの宣言と代入*/
    int e = a / b; /*整数型変数eの宣言と代入*/
    char f = '+';  /*文字型変数fの宣言と代入*/
    
    if ( f == '+') {                        /*変数fが+の時の条件分岐*/  
        printf( "a = 10\n" );               /*a = 10　の表示 */
	printf( "b = 2\n" );                /*b = 2　の表示*/
	printf( "f = %c\n" , f );           /*f = +　の表示*/
	printf( "a %c b = %d\n" , f , c  ); /*a + b = 12　の表示*/

    }else if ( f == '*' ){                  /*変数fが*の時の条件分岐*/
        printf( "a = 10\n" );               /*a = 10　の表示*/
	printf( "b = 2\n" );                /*b = 2　の表示*/
	printf( "f = %c\n" , f );           /*f =*　の表示*/
	printf( "a %c b = %d\n" , f , d );  /*a * b =20　の表示*/

    }else {                                 /*変数fが/の時の条件分岐*/
        printf( "a = 10\n" );               /*a = 10　の表示*/  
	printf( "b = 2\n" );                /*b = 2　の表示*/
	printf( "f = %c\n" , f );           /*f = /　の表示*/ 
	printf( "a %c b = %d\n" , f , e );  /*a / b = 5　の表示*/

    }
}
