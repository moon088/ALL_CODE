#include <stdio.h>
#include <stdlib.h>

typedef struct node_tag *Node;
Node p;

typedef int Label;

typedef struct node_tag{
  Label label;
  Node left;
  Node right;
  int ltag; //1の解き子、０の解き紐
  int rtag;
}Nodestruct;


typedef Nodestruct *BiTree;
BiTree T;


BiTree Create(Label L){
  Node p, h; //hはひも付き表現の際のヘッダ
  
  p = malloc(sizeof(Nodestruct));
  h = malloc(sizeof(Nodestruct));
  
  p -> label = L;
  p -> left = h;
  p -> right = h;
  p -> ltag = 0;
  p -> rtag = 0;
  /*Insertleftの際に左紐が左端だけheadを指しているため、
  その判別のためにheadのラベルをNULLにしておく*/
  h -> label = NULL;
  h -> left = p;
  h -> right = p;

  return (  (BiTree)p );
}

Node FindLeftChild(Node n){
  if(n == NULL){
    printf("空節点をたどれない\n");
  }else{
    return n -> left;
  }
}

Node FindRightChild(Node n){
  if(n == NULL){
    printf("空節点をたどれない\n");
  }else{
    return n -> right;
  }
}

Node InsertLeftChild(Node n, Label L){
  Node p;
  if(n == NULL){
    printf("空節点には挿入できない\n");

  }else if(n -> ltag == 0){
    p = malloc(sizeof(Nodestruct));
    p -> label = L;
    p -> right = n;
    n -> left = p;
    p -> ltag = 0;
    p -> rtag = 0;
    n -> ltag = 1;

    //p -> leftだけ特別？左端の葉leftがheadに向かっているため
    if(n -> left -> label == NULL){ //headかどうか判別（既存のラベルの中がNULLのものがあるとこの文だとおかしい）
      p -> left = n -> left;
    }else{
      p -> left = n;
    }
    
    return p;

  }else{
    return NULL;
  }
}


Node InsertRightChild(Node n, Label L){
  Node p;
  if(n == NULL){
    printf("空節点には挿入できない\n");

  }else if(n -> rtag == 0){
    p = malloc(sizeof(Nodestruct));
    p -> label = L;
    p -> left = n;
    p -> right = n -> right;
    n -> right = p;
    p -> ltag = 0;
    p -> rtag = 0;
    n -> rtag = 1;
    return p;
  }else{
    return NULL;
  }
}

/*ポインタによる二分木の直接表現からひも付き表現に拡張する際に、delete関数だけ表現できませんでした。
  理由は,Node nの子を削除する際、通り掛け順になるよう紐づけしなおす必要があるため、nを指している親のアドレスが必要になり、そこへのアクセス方法がわかりませんでした。*/

int DeleteLeftChild(Node n){
  if(n == NULL){
    printf("空節点は削除できない\n");
    
  }else{
    if(n -> left == NULL){ //削除対象に左の子いない
      return 0;
    }else if(n -> left -> left == NULL || n -> left -> right == NULL){
      return 0; //削除対象に子がいると削除できない
    }else{
      n -> left = NULL;
      free(n -> left);
      return 1;
    } 
  }
}

int DeleteRightChild(Node n){
  if(n == NULL){
    printf("空節点は削除できない\n");
  }else{
    if(n -> right == NULL){
      return 0;
    }else if(n -> right -> left == NULL  || n -> right -> right == NULL){
      return 0; //削除対象に子がいると削除できない
    }else{
      n -> right = NULL;
      free(n -> right);
      return 1;
    }
  }
}


int DeleteSubtree(Node n){
  if(n == NULL){
    return 0;
  }else{
    free(n);
    DeleteSubtree(n -> left);//削除部分木すべて領域開放するため
    DeleteSubtree(n -> right);
    return 1;
  }
}

int DeleteLeftSubtree(Node n){
  if(n == NULL){
    printf("空節点は削除できない\n");
  }else{
    n -> left = NULL;
    return DeleteSubtree(n -> left);
  }
}


int DeleteRightSubtree(Node n){
  if(n == NULL){
    printf("空節点は削除できない\n");
  }else{
    n -> right = NULL;
    return DeleteSubtree(n -> right);
  }
}


Node CopySubtree(Node s){
  Node d;
  if(s == NULL){
    return NULL;
  }else{
    d = malloc(sizeof(Nodestruct));
    d -> label = s -> label;

    if(s -> ltag == 0){
      d -> ltag = 0;
    }else{
      d -> left = CopySubtree(s -> left);
    }

    if(s -> rtag == 0){
      d -> rtag = 0;
    }else{
      d -> right = CopySubtree(s -> right); 
    }
    return d;
  }
}

Node InsertLeftSubtree(Node n, BiTree T){
  if(n == NULL){
    printf("空節点には挿入できない\n");
  }else{
    if(n -> ltag == 1){
      return NULL;
    }else{
      n -> left = CopySubtree((Node)T);
      return n -> left;
    }
  }
}

Node InsertRightSubtree(Node n, BiTree T){
  if(n == NULL){
    printf("空節点には挿入できない\n");
  }else{
    if(n -> rtag == 1){
      return NULL;
    }else{
      n -> right = CopySubtree((Node)T);
      return n -> right;
    }
  }
}

Node FindInOrder(Node n, BiTree T){
  Node p;
  if(n == NULL){
    printf("空節点はたどれない\n");
  }else{
    p = n -> right;
  }

  if(n -> rtag == 1){
    while(p -> ltag == 1){
      p = p -> left;
    }
  }else if(p -> label == NULL){
    p = NULL;
  }else{
    return p;
  }
  return p;
  
}

Node for_FindInOrder(BiTree T){ //FindInOrderを回転させる

  Node n = (Node)T;

  if(n == NULL){
    printf("空節点はたどれない\n");
   
  }else{
    while(n -> ltag == 1 || n -> rtag == 1){ //通り掛け初めの葉まで探索
      if(n -> ltag ==1){
	n = n -> left;
      }else{
	n = n -> right;
      printf("b");
      }
    }
    
    while(FindInOrder(n,T) != NULL){ //ひとつづつ次に進めながら出力
      n = FindInOrder(n , T);
      printf("%d" , n -> label);
      }

  }
  printf("\n");
}

int main (){
  printf("課題2.1二分木のポインタによる直接表現を拡張し、ひも付き表現にしました。\n");

  T = Create(1);
  InsertLeftChild((Node)T, 2);
  InsertLeftChild( (FindLeftChild((Node)T)), 3);
  InsertLeftChild( (FindLeftChild((FindLeftChild((Node)T)))) , 4);
  InsertRightChild( (FindLeftChild((Node)T)), 5);
  InsertRightChild((Node)T, 6);
  InsertLeftChild( (FindRightChild((Node)T)), 7);

  printf("課題2.1：通り掛がけ順にラベルを出力\n");  
  for_FindInOrder((Node)T);








}
