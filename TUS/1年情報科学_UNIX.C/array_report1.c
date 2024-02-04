#include <stdio.h>

int main(){

    float array[7];         /*少数型変数として配列array[]を格納*/
    int i;                   /*整数型変数iの宣言*/  
    float xn = 300;          /*少数型変数xnの宣言と代入*/  
    
    for(i = 0;i < 7; i++){  /*くり返し文の利用*/
	array[i] = xn;       /*配列array[]をxnの値で格納する*/
	xn = xn / 2;         /*xnを２で割った値を新たにxnとする*/
    }
 
    for(i = 7; i > 2 ;i--){ /*くり返し文の利用*/              
	    printf("x%d = %f\n" , i , array[i-1] ); /*格納した配列を出力する*/
	}
}
