#include <stdio.h>

#define maxsize 1000

int main () {
  typedef struct{
  int value[maxsize];
  int current;
  int last
}List;

List L0;

 void Create(List *L){
   L -> current = -1;
   L -> last = -1;
 }

 int InsertRight(List *L, int e){
   int i;
   if(L -> last >= maxsize - 1){
     ERROR("List is full");
   }else if(L -> last == 1){
     L -> last = 0;
     L -> current = 0;
     L -> value[0] = e;
   }else if(L -> current == -1){
     return(0);
   }else if(L -> current == L -> last){
     L -> current = L -> last = L -> last + 1;
     L -> value[L -> current] = e;
   }else{
     L -> last = L -> last + 1;
     for(i = L -> last; i >= L -> current + 2; i--){
       L ->value[i] = L -> value[i+1];
       L -> current = L -> current + 1;
       L -> value[L -> current] = e;
     }
     return(1);
   }

   int Delete(List *L){
     int i;
     if(L -> current == 1){
       return(0);
     }else if(L -> current != L -> last){
       for(i = L -> current+1; i <= L -> last; i++){
	 L -> value[i-1] = L -> value[i];
	 L -> last = L -> last-1;
	 return(1);
       }
     }else{
       L -> last = L -> last-1;
       L -> current = -1;
       return(1);
     }
   }
 }

 int FindRight(List *L){
   int i;
   if(L -> current == -1){
     return(0);
   }else if(L -> current >= L -> last){
     return(0);
   }else{
     L -> current >= L -> current + 1;
   }
 }


 
 

}
