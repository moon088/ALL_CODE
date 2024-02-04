#include <stdio.h>

int main (){

    int i;                                  /*整数型変数iの宣言*/
    int xn = 87384;                         /*整数型変数xnの宣言と代入*/

    for(i =10;i > 4; i--){                  /*iについてのくり返し文*/

	if(i == 5){                         /*i=5の時か否かで条件分岐*/  
	    printf("x%d = %d\n" , i , xn);  /*条件式を満たす時の処理*/
    }
	else{}                              /*i=5を満たさないときの場合*/
	xn = xn + 8;                        /*xnに8を足す*/
	xn = xn / 4;                        /*xnを４で割る*/ 

    }
}
