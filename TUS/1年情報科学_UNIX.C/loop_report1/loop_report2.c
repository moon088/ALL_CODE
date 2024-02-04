#include <stdio.h>

int main (){

    int i;                                 /*整数型変数iの宣言*/ 
    int xn = 0;                            /*整数型変数xnの宣言と代入*/
    int yn = 1;                            /*整数型変数ynの宣言と代入*/
    int zn = xn + yn;                      /*整数型変数znの宣言と代入*/ 

    for(i = 1; i < 11; i++){               /*くり返し文を利用して１０回繰り返す*/
	if(i == 1){                        /*条件分岐　i=1の場合*/
	    printf("x%d = %d\n" , i , xn); 
	}
	else if (i == 2){                  /*i=2の場合*/
	    printf("x%d = %d\n" , i , yn);
	}
	else{
	printf("x%d = %d\n" , i , zn ); 
	xn = yn;                           /*xnの値をynに変更*/
	yn = zn;                           /*ynの値をznに変更*/
	zn = xn + yn;                      /*znの値をxn+ynに変更*/
	}
    }


}
