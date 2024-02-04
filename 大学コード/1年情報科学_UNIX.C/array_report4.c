#include <stdio.h>

int main(){
    int array[10][10][10];                       /*配列arrayを宣言する*/    
    int i, j, k;                                 /*整数型変数,i,j,kを宣言*/


    for(i=0;i < 10;i++){                         /*繰り返し文を３回利用し配列に格納する*/
	for(j=0;j < 10;j++){
	    for(k=0;k < 10;k++){
		array[i][j][k] =(i+1)+5*(j+1)-k-1;
	    }
	}
    }
    int a = 3;                                    /*任意の自然数a,b,cを宣言*/
    int b = 7;
    int c = 9;
    printf("a = %d, b = %d, c = %d, result = %d\n" ,a,b,c,array[a-1][b-1][c-1]);
    /*計算結果の出力*/

}
