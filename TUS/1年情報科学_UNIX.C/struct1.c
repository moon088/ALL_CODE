#include <stdio.h>

struct rectangle{
    int height;
    int width;

};

int area_of(struct rectangle r){
   
    return r.height * r.width;

}

int main (){
    struct rectangle r;
    
    r.height = 10;
    r.width = 20;
   
    int result = area_of(r);
    printf("高さ：%d\n" , r.height);
    printf("横：%d\n" , r.width);
    printf("面積：%d\n" , result);



}
