#include <stdio.h>

void swap (int *x , int *y){
    int *z;
    *z = *x;
    *x = *y;
    *y = *z;
}

int main () {
    int a = 100;
    int b = 200;
    printf("before:a = %d, b = %d\n" , a , b );
    swap( &a , &b);
    printf("after:a = %d, b = %d\n" , a , b );

}
