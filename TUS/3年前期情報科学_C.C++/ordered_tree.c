#include <stdio.h>
#include <stdlib.h>

typedef struct node_tag *Node;
Node p;
typedef char Label;

typedef struct node_tag {
	Node child;
	Label label;
	int tag;
	Node next;
}Nodestruct;


typedef Nodestruct *Tree;
Tree T;

Tree Create(Label L) {
  Node p;
  p = malloc(sizeof(Nodestruct));
  p->label = L;
  p->child = NULL;
  p->next = NULL;
  p->tag = 1;
  return((Tree)p);
}

Node FindRightSibling(Node n) {
  if (n == NULL)printf("空節はたどれません");
  if (n->tag)return NULL;
  else return n->next;
}

Node FindLeftmostChild(Node n){
  if(n == NULL)printf("空節はたどれません");
  if(n -> child == NULL){ 
    return NULL;
  }else{
    return n -> child;
  }
}

Node InsertLeftmostChild(Node n, Label L){
  Node p;
  if (n == NULL)printf("空節点");
  p = malloc(sizeof(Nodestruct));
  p->label = L;
  if (n->child != NULL) { //長男いる
		p->next = n -> child;
		p->tag = 0;
		p->child = NULL;
		n->child = p;
  }
  else { //長男いない
    p->next = n;
    p->tag = 1;
    p->child = NULL;
    n->child = p;
  }
  return p;
  
}

Node InsertRightSibling(Node n, Label L){
  Node p;
  if(n == NULL)printf("空節点");
  p = malloc(sizeof(Nodestruct));
  p -> label = L;
  
  if(n -> tag == 0){//末弟でない
    p -> next = n -> next;
    n -> next = p;
    p -> tag = 0;
    p -> child = NULL;    

  }else{  //末弟である
    p -> next = n -> next;
    n -> next = p;
    n -> tag = 0;
    p -> child = NULL;
    p -> tag = 1;   
  }

}

int DeleteLeftmostChild(Node n) {
  Node p;
  if (n == NULL) printf("空節点");
  p = n->child;
  if (p == NULL) return 0; 
  else if (p->child != NULL) return 0;
  else if (p->tag) n->child = NULL; 
  else n->child = p->next;
  free(p); 
  return 1;
}

int DeleteRightSibling(Node n){
  Node p;
  if (n == NULL) printf("空節点");
  if (n->tag) return 0; 
  p = n->next;
  if (p->child != NULL) return 0; 
  n->next = p->next; n->tag = p->tag;
  free(p);
  return 1;
}

int DeleteSubtree(Node n) {
  Node c, d;
  if (n == NULL) return 0;
  c = n->child;
  while (c != NULL) { 
    d = FindRightSibling(c); DeleteSubtree(c); c = d;
  }
  free(n);
  return 1;
  
}

int DeleteLeftmostSubtree(Node n) {
  Node c, d;
  if (n == NULL) printf("空節点");
  c = n->child;
  if (c == NULL) return(0); 
  n->child = FindRightSibling(c); 
  DeleteSubtree(c); 
  return 1;
}

int DeleteRightSubtree(Node n) {
  Node c, d;
  if (n == NULL) printf("空節点");
  c = FindRightSibling(n);
  if (c == NULL) return 0; 
  n->next = c->next; n->tag = c->tag;
  DeleteSubtree(c); 
  return 1;
}


Node FindRightSibling_test(Node n) {
  if (n == NULL)printf("空節はたどれません");
  if (n->tag){
    printf("末弟いません");
    return NULL;
  }else{
    printf("%c" , n-> next -> label);
    return n->next;
    
  }
}

Node FindLeftmostChild_test(Node n){
  if(n == NULL)printf("空節はたどれません\n");
  if(n -> child == NULL){
    printf("子供いません\n");
    return NULL;
  }else{
    printf("%c" , n -> child -> label);
    return n -> child;
  }
}


Node PreOrder(Node n){
  if(n ==NULL){
    printf("空節点はたどれません\n");
  }

  printf("%c" , n -> label);
  while(n -> child != NULL){
    n = n -> child;
    printf("%c" , n -> label);
  }
  
  while( n -> next != NULL){
    if(FindRightSibling(n) == NULL){
      n = n -> next;

    }else{
      n = n -> next;

      printf("%c" , n -> label);
      while(n -> child != NULL){
	n = n -> child;
	printf("%c" , n -> label);
      }
      
    }
  }
  printf("\n");
}


int main() {

  printf("課題1.1：順序を構成完了\n");
  T = Create('A');
  InsertLeftmostChild((Node)T, 'H');
  InsertLeftmostChild((Node)T, 'B');
  InsertRightSibling(FindLeftmostChild((Node)T), 'E');
  InsertLeftmostChild(FindLeftmostChild((Node)T), 'C');
  InsertRightSibling(FindLeftmostChild(FindLeftmostChild((Node)T)), 'D');
  InsertLeftmostChild(FindRightSibling(FindLeftmostChild((Node)T)), 'F');
  InsertLeftmostChild(FindLeftmostChild(FindRightSibling(FindLeftmostChild((Node)T))), 'G');

  //test
  printf("順序木が正しく構成できいてるか節探索経路を出力\n");
  FindLeftmostChild_test( FindLeftmostChild_test((Node)T));//C
  printf("\n");
  FindLeftmostChild_test( FindRightSibling_test( FindLeftmostChild_test((Node)T)));//F
  printf("\n");
  FindRightSibling_test( FindLeftmostChild_test( FindLeftmostChild_test((Node)T)));//D
  printf("\n");
  FindRightSibling_test(((Node)T));//いない
  printf("\n");
  FindLeftmostChild_test( FindLeftmostChild_test( FindLeftmostChild_test((Node)T)));//いない

  printf("------------------------------------\n");
  printf("課題1.2：ラベル列の印字\n");
  PreOrder((Node)T);


}
