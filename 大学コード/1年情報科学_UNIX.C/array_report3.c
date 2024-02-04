#include <stdio.h>

int main(){
    int array[5][10] = { {83, 0, 68, 39, 84, 26, 4, 18, 18, 89} ,   /*配列arrayに全受験者の点数を格納*/
			 {72, 17, 17, 6, 5, 28, 24, 94, 8, 98} ,
			 {45, 63, 44, 78, 72, 38, 31, 80, 7, 78} ,
			 {56, 57, 44, 23, 96, 95, 16, 66, 12, 0} ,
			 {54, 50, 85, 72, 56, 90, 66, 47, 49, 100} ,
    };
    int i , j ;                                                     /*整数型変数i,jの宣言*/
    float score;                                                    /*少数型変数scoreの宣言*/
    int number , class;                                             /*整数型変数number,classの宣言*/

    for(i = 0;i < 5;i++){                                           /*くり返し文を２回利用して全受験者の点数を足す*/
	for(j = 0; j < 10; j++){
	    score = score + array[i][j];
	}
    }
    score = score / 5 / 10;                                         /*点数をすべて足し合わせたものを人数で割る*/
    printf("---全受験者の平均点---\n%f\n" , score);                 /*平均点の出力*/
    score = 0;                                                      /*scoreをリセット*/

    
    printf("----各組の平均点---\n"); 
    for(i = 0; i < 5;i++){                                          /*各クラス分以下を繰り返す*/
	for(j = 0; j < 10;j++){                                     /*クラス全員の点数をくり返し文を使って足す*/
	score = score + array[i][j];                          
	}
	score = score / 10;                                         /*クラスの人数で割る*/  
	printf("%d組：%f点\n" , i+1 , score );                      /*クラスの平均点を出力*/   
	score = 0;                                                  /*scoreをリセット*/ 
    }


    printf("---最高得点---\n");                                            
    for(i = 0;i < 5;i++){                                           /*2回の繰り返し文を使って全受験者の点数が最高点であるのかを調べる*/
	for(j = 0;j < 10;j++){
	    if(array[i][j] > score){                                /*最高点であるのか条件式を用いて調べる*/
		score = array[i][j];                                /*最高点を更新*/
		number = i * 10 + 10 + j;                           /*現時点での最高点である人の受験番号を更新*/
		class = i + 1;                                      /*現時点での最高点である人のクラスを更新*/   
	    }else{
	    }	    
	}
    }
    
    printf("点数：%f点\n" , score);                                 /*最高点、番号、所属をそれぞれ出力*/      
    printf("番号：%d\n" , number );
    printf("所属：%d\n" , class);

}
