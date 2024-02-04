#include <stdio.h>
#include <string.h>

struct member{
    char name[50];
    struct member*next;
    
};

int main(){
    struct member a , b , c ,d , e , f;

    strcpy(a.name, "munehiro");
    a.next = NULL;

    strcpy(b.name, "kouiti");
    b.next = &a;
    
    strcpy(c.name, "tomohumi");
    c.next = &b;

    strcpy(d.name, "hidehumi");
    d.next = &c;
    
    strcpy(e.name, "syouhei");
    e.next = &d;
    
    strcpy(f.name, "shun");
    f.next = &e;
    
    printf("%s\n" , f.name);
    printf("%s\n" , f.next -> name);
    printf("%s\n" , e.next -> name);
    printf("%s\n" , d.next -> name);
    printf("%s\n" , c.next -> name);
    printf("%s\n" , b.next -> name);
    printf("---------------\n");

    d.next = NULL;
    e.next = &c;

    printf("%s\n" , f.name);
    printf("%s\n" , f.next -> name);
    printf("%s\n" , e.next -> name);
    printf("%s\n" , c.next -> name);
    printf("%s\n" , b.next -> name);
    printf("---------------\n");
    
    struct member h;
    strcpy(h.name, "shigeo");
    h.next = &f;
   
    printf("%s\n" , h.name);
    printf("%s\n" , h.next -> name);
    printf("%s\n" , f.next -> name);
    printf("%s\n" , e.next -> name);
    printf("%s\n" , c.next -> name);
    printf("%s\n" , b.next -> name);
   


}
