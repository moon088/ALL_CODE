#include <stdio.h>
#include <stdlib.h>

int main (){
    int buffer;
    int*p;
    printf("Input an integer:\n");
    scanf("%d" , &buffer);
    p = malloc(sizeof(int));
    *p = buffer;
    printf("%d\n" , *p);
    free(p);
}
