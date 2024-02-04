#include <stdio.h>
#define maxsize 100

typedef char element;

typedef struct{
  int top;
  element value[maxsize];
}stack;


int pushdown(stack *s, element e){
  if(s -> top == 0){
    return 0;
  }else{
    s -> top = s -> top-1;
    s -> value[s->top] = e;
    return 1;
  }  
}

int popup(stack *s){
  if(empty(s)){
    return 0;
  }else{
    s -> top = s -> top + 1;
    return 1;
  }
}

int retrieve(stack *s, element *v){
  if(empty(s)){
    return 0;
  }else{
    *v = s->value[s->top];
    return 1;    
  }
}

void create(stack *s){
  s -> top = maxsize;
}

int empty(stack *s){
  return (s -> top = maxsize);
}


void Edit(){
  stack S, T; element e; char c;

  create(&S);
  do{
    scanf("%c", &c); 
    if(c == '#'){ if(!popup(&S)){ ERROR("popup Error"); return; } }
    else if (c == '@'){ create(&S); } 
    else { if(!pushdown(&S, c)){ ERROR("pushdown Error"); return; } } 
  } while( c != '\n');
  
  create( &T ); 
  while(!empty(&S)){ pushdown( &T, (retrieve(&S, &e), e )); popup(&S); }
  while(!empty(&T)){ 
    printf("%c", (retrieve(&T, &e), (char)e)); 
    popup(&T);}}




typedef struct{
  int front, rear;
  element value[maxsize];
} Queue;
Queue Q0;


int EnQueu(Queue *Q, element e){ 
  if( AddOne( AddOne(Q->rear) ) == Q->front) return 0;
  else{
    Q->rear = AddOne(Q->rear);
    Q->value[Q->rear]=e;return 1;
  }
}

int DeQueue(Queue *Q){
  if(Empty(Q)) return 0; 
  else{
    Q->front = AddOne(Q->front); return 1;
  }
}

int Retrieve(Queue *Q, element *v){
if (Empty(Q)) return 0;
else{ *v = Q->value[Q->front]; return 1; } }


int Empty(Queue *Q){
return(AddOne(Q->rear) == Q->front); }


void Create(Queue *Q){
Q->front = 0;
Q->rear = maxsize -1; }


int AddOne(int i){
return (i + 1) % maxsize; }




int main(){
  

}
