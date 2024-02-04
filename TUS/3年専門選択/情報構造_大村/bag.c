#include <stdio.h>
#include <stdbool.h>
#define maxsize 100

typedef struct {
  int value[maxsize];
  int size;
}BAG;

BAG B;
BAG insert(int e, BAG B){
  if (B.size < maxsize-1){
    B.size = B.size + 1;
    B.value[B.size] = e;    
  }else{
    printf("BAG is full\n");
  }
  return B;
 
}


int search(int e, BAG *B){
  int i = 0;
  while( (B -> value[i] != e) && (i <= B -> size) )
    i++;
  if(i <= B -> size)
    return i;
  else
    return -1;
}


BAG delete(int e, BAG B){
  int i;
  i = search(e, &B);
  if(i != -1){
    B.value[i] = B.value[B.size];
    B.size = B.size-1;
  } 
  return B;
}

BAG empty(){
  BAG b;
  //b.size = 0;
  return b;
  }

bool is_empty(BAG *B){
  if(B -> size == 0)
    return true;
  else
    return false;
}


bool is_element(int e, BAG *B){
  if(search(e, B) == -1){
    return false;
  }else{
    return true;
  }
}


int main(void){
  printf("%d\n" , B.size);
  printf("is empty? : %d\n" , is_empty(&B));
  B = insert(3, B);
  B = insert(2, B);
  B = insert(3, B);
  printf("is empty? : %d\n" , is_empty(&B));
  B = delete(2, B);
  printf("%dis element? : %d\n" , 3 , is_element(3, &B));
}
