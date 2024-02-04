#include <stdio.h>

int plus(int *pa , int *pb){
    return *pa + *pb;
}

int main() {
    int i = 3;
    int j = 4;
    int y = plus(&i , &j);
    printf("i+j = %d\n" , y);

}
