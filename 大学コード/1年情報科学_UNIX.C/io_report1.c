#include <stdio.h>


int main(){
    char sequence[10000];     /*文字型変数の配列sequence[]の宣言*/
    scanf("%s" , sequence);   

    int numcount = 0;         /*必要な整数型で変数を宣言と代入*/
    int abccount = 0;
    int markcount = 0;
    int i;

    for (i = 0; sequence[i] != '\0' ; i++){   /*繰返し範囲を配列内に格納されている要素すべてに設定*/
	if ( (sequence[i] >= 'a' && sequence[i] <= 'z' ) || (sequence[i] >='A' && sequence[i        ] <= 'Z') ) {
	    abccount++;                       /*配列内に格納された文字が文字a～z,A～Zであるときの処理*/
	
	}else if (sequence[i] >= '0' && sequence[i] <= '9'){ /*配列内に格納された文字が0～9*/
	    numcount++;

	}else{
	    markcount++;
	    
	}
    }

    printf("アルファベット：%d文字\n" , abccount); /*カウントした文字数の出力*/
    printf("数値：%d文字\n" , numcount);
    printf("その他：%d文字\n" , markcount);


}
