#include <stdio.h>

int main(){

    int num1 = 256;            /*整数型変数num1の宣言と代入*/ 
    int num2 = 368;            /*整数型変数num2の宣言と代入*/ 

    
    if( num1 >= num2){         /*num1とnum2のどちらが大きいかで条件分岐*/
	int i = num1 % num2;   /*整数型変数iの宣言と代入*/
	
	while(i != 0){         /*iが0出ないときに行う繰り返し文の条件式を設定*/   
	    num1 = num2;       /*num1をnum2に変更*/
	    num2 = i;          /*num2をnum1に変更*/
	    i = num1 % num2;   /*再び新たなnum1とnum2から剰余を設定*/	    
	}
	printf("%d\n" , num2 );/*iが0になったときにnum2を出力*/ 
    }

    else{                      /*num2の方がnum1より大きい場合の処理*/ 
	int i = num2 % num1;   /*以下同じ処理を行い、最大公約数を出力*/

	while(i != 0){
	    num2 = num1;
	    num1 = i;
	    i = num2 % num1;
	}
	printf("%d\n" , num1 );	
    }
}
