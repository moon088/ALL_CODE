#include <stdio.h>

int main () {
    int a =11;                      /*整数型変数a（月）の宣言と代入*/
    int b =40;                      /*整数型変数b（日）の宣言と代入*/


    switch(a){                      /*switch文を利用して月ごとに条件分岐*/
    case 1:                         /*１月の場合*/
	if( 0 < b && b < 20 ){      /*if文を利用して日にちによる条件分岐*/
	    printf("%d月%d日はおひつじ座です" , a , b ); /*１日から１９日までの場合*/
        }else if( b <= 31 ){        /*２０日から３１日までの場合*/
	    printf("%d月%d日はみずがめ座です" , a , b);
	}else                       /*日にちの入力が誤っている場合*/
	    printf(" %d月%d日 :正しい月日を指定してください" , a , b );
	break;

    case 2:                         /*2月の場合*/
	if( 0 < b && b < 19 ){      /*以下１月と同じ*/
	    printf("%d月%d日はみずがめ座です" , a , b );
	}else if ( b <= 28 ){       
	    printf("%d月%d日はうお座です" , a , b );
	}else
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
	break;

    case 3:
        if( 0 < b && b < 21 ){
            printf("%d月%d日はうお座です" , a , b );
        }else if ( b <= 31 ){
            printf("%d月%d日はおひつじ座です" , a , b);
        }else 
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;

     case 4:
        if( 0 < b && b < 20 ){
            printf("%d月%d日はみずがめ座です" , a , b );
        }else if( b <= 30 ){
            printf("%d月%d日はおうし座です" , a , b);
        }else 
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;


     case 5:
        if( 0 < b && b < 21 ){
            printf("%d月%d日はおうし座です" , a , b );
        }else if ( b <= 29 ){
            printf("%d月%d日はふたご座です" , a , b);
        }else
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;


      case 6:
        if( 0 < b && b < 22 ){
            printf("%d月%d日はふたご座です" , a , b );
        }else if ( b <= 30 ){
            printf("%d月%d日はかに座です" , a , b );
        }else
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;


       case 7:
        if(0 < b && b < 23 ){
            printf("%d月%d日はかに座です" , a , b );
        }else if ( b <= 31 ){
            printf("%d月%d日はしし座です" , a , b);
        }else 
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;

       case 8:
        if( 0 < b && b < 23 ){
            printf("%d月%d日はしし座です" , a , b );
        }else if ( b <= 30 ){
            printf("%d月%d日はおとめ座です" , a , b);
        }else 
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;

       case 9:
        if( 0 < b && b < 23 ){
            printf("%d月%d日おとめ座です" , a , b );
        }else if ( b <= 30 ){
            printf("%d月%d日はてんびん座です" , a , b);
        }else 
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;

       case 10:
        if( 0 < b && b < 24 ){
            printf("%d月%d日てんびん座です" , a , b );
        }else if ( b <= 31 ){
            printf("%d月%d日はさそり座です" , a , b);
        }else 
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break; 

        case  11:
        if( 0 < b && b < 23 ){
            printf("%d月%d日はさそり座です" , a , b );
        }else if ( b <= 30 ){
            printf("%d月%d日はいて座です" , a , b );
        }else
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );
        break;

        case 12:
        if( 0 < b && b < 22 ){
            printf("%d月%d日はいて座です" , a , b );
        }else if ( b <= 31 ){
            printf("%d月%d日はやぎ座です" , a , b);
        }else
	    printf("%d月%d日 :正しい月日を指定してください" , a , b );

        default:              /*月の入力が誤っている場合*/
	    printf("%d月%d日：正しい月日を指定してください" , a , b );

        break;

 
}
}
