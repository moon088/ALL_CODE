#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p;       /*ポインタ変数を宣言*/
    printf("%p\n" , p);
    
    p = malloc( sizeof(int) ); /*ポインタ変数が指し示すメモリを確保*/
    printf("%p\n" , p);
        
    free( p );                 /*確保したメモリを開放し、不明のメモリを指している*/
    printf("%p\n" , p);
    
    p = NULL;                  /*メモリを確保せず、どこも指差ないようにするy*/
    printf("%p\n" , p);   


}
