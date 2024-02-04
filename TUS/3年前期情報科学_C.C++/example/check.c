

  #include <stdio.h>

  struct foo {
    int a;
    float b;
    double c;
  };

union bar {
    int a;
    float b;
    double c;
  };



  main() {
    struct foo x;

    printf("%p\n",&x);
    printf("%p\n",&(x.a));
    printf("%p\n",&(x.b));
    printf("%p\n",&(x.c));
  union bar y;

    printf( "%p\n" , &y);
    printf( "%p\n" , &( y.a ) );
    printf( "%p\n" , &( y.b ) );
    printf( "%p\n" , &( y.c ) );



  }
