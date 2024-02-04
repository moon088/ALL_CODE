#include <stdio.h>
#include <string.h>

struct inf{
    char name[50];
    int year;
    int month;
    int date;
};


int main (){
    struct inf TOKIO[] = {
	{ "Joshima" , 1970 , 11 , 17},
	{ "Kokubun" , 1974 , 9 , 2},
	{ "Matsuoka" , 1977 , 1 , 11},

    };

    int i;
    for (i = 0; i < 3; i++){
	printf("名前：%s\n" , TOKIO[i].name );
	printf("生まれ年：%d\n"  ,TOKIO[i].year );
	printf("生まれ月：%d\n" , TOKIO[i].month );
	printf("生まれ日：%d\n" , TOKIO[i].date );

    }



}
