#include <stdio.h>

int main(){
    int a;
    float b;
    char c;
    int d[10];
    float e[10];
    char f[10];


    printf("aのサイズは、%dです。\n" , sizeof(a));
    printf("aのアドレスは、%pです。\n" , &a);
    
    printf("bのサイズは、%dです。\n" , sizeof(b));
    printf("bのアドレスは、%pです。\n" , &b);

    printf("cのサイズは、%dです。\n" , sizeof(c));
    printf("cのアドレスは、%pです。\n" , &c);
    
    printf("dのサイズは、%dです。\n" , sizeof(d));
    printf("dのアドレスは、%pです。\n" , &d);
    
    printf("d[0]のサイズは、%dです。\n" , sizeof(d[0]));
    printf("d[0]のアドレスは、%pです。\n" , &d[0]);

    printf("d[1]のサイズは、%dです。\n" , sizeof(d[1]));
    printf("d[1]のアドレスは、%dです。\n" , d[1]);

    printf("eのサイズは、%dです。\n" , sizeof(e));
    printf("eのアドレスは、%p\n" , &e);

    printf("e[0]のサイズは、%dです。\n" , sizeof(e[0]));
    printf("e[0]のアドレスは、%dです。\n" , &e[0]);

    printf("e[1]のサイズは、%dです。\n" , sizeof(e[1]));
    printf("e[1]のアドレスは、%dです。\n" , &e[1]);
    
    printf("fのサイズは、%dです。\n" , sizeof(f));
    printf("fのアドレスは、%p\n" , &f);
    
    printf("f[0]のサイズは、%dです。\n" , sizeof(f[0]));
    printf("f[0]のアドレスは、%dです。\n" , &f[0]);

    printf("f[1]のサイズは、%dです。\n" , sizeof(f[1]));
    printf("f[1]のアドレスは、%dです。\n" , &f[1]);
    
}
