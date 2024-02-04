#include <stdio.h>

int doubleF(int *xyz){
    *xyz = 2 * *xyz;
    return *xyz;

}

int main (){
    int x = 3;
    int y = doubleF(&x);
    printf("x = %d\n" , x);
    printf("y = %d\n" , y);


}
