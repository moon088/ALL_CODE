#include <stdio.h>

int sequence (int arg1 , int arg2 , int arg3){ /*関数sequenceを宣言*/ 
    int xn = arg2;                             /*整数型変数xnとiを宣言しxnをarg2を代入*/
    int i;

    for (i = 1; i < 10000; i++){               /*くり返し文を利用してnがarg3まで漸化式を計算する*/
	if (i == arg3){
	    if ( arg1 >= 1 && arg2 >= 1 && arg3 >= 1){ /*漸化式の計算後返す値を条件分岐*/
		return xn;                                          
 	    }else{                                   
		return -1;
	    } 
	}else{
	    xn = xn + arg1;
	}
    }
} 


int main() {
    int result;                           /*整数型変数result,arg1,arg2,arg3を宣言*/     
    int arg1 , arg2 , arg3;

    arg1 = 5;                             /*arg1,arg2,arg3にそれぞれ任意の整数を代入*/
    arg2 = 3;
    arg3 = 8;
    
    result = sequence (arg1 ,arg2 ,arg3); /*関数sequenceの返り値によって出力結果を条件分岐*/
    if( result != -1){
        printf("----------\n");
	printf("arg1:%d\n" , arg1);
	printf("arg2:%d\n" , arg2);
	printf("arg3:%d\n" , arg3);
	printf("----------\n");
	printf("x%d:%d\n" , arg3 , result);

    }else{
	printf("----------\n");
	printf("arg1:%d\n" , arg1);
	printf("arg2:%d\n" , arg2);
	printf("arg3:%d\n" , arg3);
	printf("----------\n");
	printf("Error:引数が１以上の整数値ではない。\n");
    }
}    



