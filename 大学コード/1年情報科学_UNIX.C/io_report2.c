#include <stdio.h>

int main(){
    float num;         /*整数型変数numの宣言*/
    char operation;    /*文字型変数operationの宣言*/
    float answer = 0;  /*整数型変数naswerの宣言と代入*/ 


    while( scanf("%c%*c%f%*c" , &operation , &num ) != EOF ){  /*外部から入力された数値と演算子を読み込み、処理を繰り返す*/
	if(operation == '/' && num == 0){                      /*ゼロ除算となるときのエラーの出力*/
	    printf("エラー：ゼロ除算になる。\n");
	    
	}else if (operation != '+' && operation != '-'         /*演算子が適切でないときのエラーの出力*/
		  && operation != '*' && operation != '/'){
	    printf("エラー：演算子ではない。\n");

	}else{                                                 /*正常に外部から入力されたときの処理*/
	    switch(operation){                                 /*それぞれの演算子が読み込まれたときのanswerに行う処理*/
	    case '+':
		answer = answer + num;
		break;
		
	    case '-':
		answer = answer - num;
		break;
	    
	    case'*':
		answer = answer * num;
		break;
	    
	    case'/':
		answer = answer / num;
		break;
	    }
	    
	    printf("結果：%f\n" , answer );                    /*計算結果の出力*/
	}

    }
}
