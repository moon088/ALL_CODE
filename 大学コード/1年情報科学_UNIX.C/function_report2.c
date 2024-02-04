#include <stdio.h>

int function (float num1 , float num2 , char operator ){            /*少数型変数num1,num2と文字型変数operatorを関数functionの引数として宣言*/
    if ( num1 < 0 || num1 > 500 || num2 < 0 || num2 > 500 ){    /*num1,num2が０以上５００以下でない場合のエラーメッセージの出力処理*/
	printf("Error:数値が０以上５００以下ではない。\n");
	printf("数値１:%f\n" , num1 );
	printf("数値２:%f\n" , num2 );
    
    }else if(operator !='+' && operator !='-' && operator !='*' && operator !='/'){ /*演算子operatorが適切でないときのエラーメッセージの出力処理*/
	printf("Error:演算子が適切ではない。\n");
	printf("演算子:%c\n" , operator);

    }else if ( operator == '/' && num2 == 0){                  /*ゼロ除算となる場合のエラーメッセージの出力処理*/
	printf("Error:計算がゼロ除算となる。\n");
	printf("%f%c%f\n" , num1 , operator , num2);
	
    }else{
        float answer;                /*正常に計算できる場合の計算処理*/
        if (operator == '+'){        /*それぞれの演算子の時の計算結果の代入*/
            answer = num1 + num2;
        }else if (operator == '-'){
            answer = num1 - num2;
        }else if (operator == '*'){
            answer = num1 * num2;
        }else{
            answer = num1 / num2;
        }	
	printf("%f%c%f=%f\n" , num1 , num2 , operator , answer );
    }
}


int main() {
    float num1 , num2 , answer;  /*関数function内のプログラムを実行するための変数の宣言*/
    char operator;

    num1 = 1.500000;             /*任意の数値２つと演算子１つの代入*/
    num2 = 2.500000;
    operator = '+';
    
    function( num1 , num2 , operator); /*関数functionのプログラムの実行*/

}
