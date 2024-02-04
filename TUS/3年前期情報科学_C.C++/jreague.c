#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define HASHSIZE 17


struct match_score{ /*各試合の詳細*/
  int year;
  int month;
  int day;
  int home_score;
  int away_score;
  struct match_score *next;
};

struct match{  /*試合一つ一つの構造体*/
  char *home;
  char *away;
  struct match_score *r;
  struct match *next;
};

struct match *hashtable[HASHSIZE];


/*ハッシュ関数*/
int hash(char *hashkey1, char *hashkey2){
  int hashval = 0;
  while(*hashkey1 != '\0'){
    hashval = hashval + *hashkey1;
    hashkey1++;
  }
  while(*hashkey2 != '\0'){
    hashval = hashval + *hashkey2;
    hashkey2++;
  }

  return hashval % HASHSIZE;
}




void add(int year,int month,int day,char* home_team,int home_score,int away_score,char* away_team){
  struct match_score *match_data;
  match_data = malloc(sizeof(struct match_score));

  //メモリの確保と、メンバ変数への代入
  match_data -> year = year;
  match_data -> month = month;
  match_data -> day = day;
  match_data -> home_score = home_score;
  match_data -> away_score = away_score;
  match_data -> next = NULL;

  //対戦カードの探索
  int matchpair = 0;
  int hashval = hash(home_team, away_team);
  struct match *ptr = hashtable[hashval];
  
  while(ptr != NULL){
    if(strcmp(ptr->home, home_team) == 0 && strcmp(ptr->away,away_team) ==0){
      matchpair = 1; //対戦カードの組が見つかったため真
      match_data -> next = ptr -> r;
      ptr -> r = match_data;
      break;
    }
    ptr = ptr -> next;
  }

  /*対戦カードが見つからなかった場合、新たに対戦カードを追加*/
  if(matchpair == 0){
    struct match *new_matchcard;
    new_matchcard = malloc(sizeof(struct match));
    new_matchcard -> home = strdup(home_team);
    new_matchcard -> away = strdup(away_team);
    new_matchcard -> r = NULL;
    new_matchcard -> next = NULL;

    new_matchcard -> r = match_data;
    new_matchcard -> next = hashtable[hashval];
    hashtable[hashval] = new_matchcard;
  }  


}




void dist(){
  printf("--HASHSIZE: %d--\n" , HASHSIZE);
  for(int i = 0;i < HASHSIZE; i++){
    int count = 0;
    struct match *ptr = hashtable[i];
    while(ptr != NULL){
      count++;
      ptr = ptr -> next;
    }

    printf("TABLE[%d]:%d\n" , i, count);
  }
}


void record(char* home, char* away){
  int hashval = hash(home, away);
  int count = 0;
  int win = 0;
  int lose = 0;
  int draw = 0;

  struct match *ptr;
  struct match_score *ptr2;
  ptr = hashtable[hashval];

  while(ptr != NULL){ /*リスト構造の末端まで探索*/
    if(strcmp(ptr->home,home) == 0&&strcmp(ptr->away,away) ==0){
      ptr2 = ptr -> r;
      while(ptr2 != NULL){
	/*探索した対戦カードのリストを末端までアクセスし数をカウント*/
	count++;
	if(ptr2 ->home_score > ptr2 -> away_score){
	  win++;
	}else if(ptr2 -> home_score < ptr2 -> away_score){
	  lose++;
	}else{
	  draw++;
	}
	ptr2 = ptr2 -> next;
      }
      break;
    }
    ptr = ptr -> next;
  }
  printf("%s (HOME) vs %s (AWAY) : %d games.(win:%d, lose:%d, draw:%d)\n"
	 , home, away, count, win, lose, draw);
}


void record_year(char* home, char* away, int year){
  int hashval= hash(home,away);
  int count = 0;
  int win = 0;
  int lose = 0;
  int draw = 0;
  
  struct match *ptr;
  struct match_score *ptr2;
  ptr = hashtable[hashval];

  while(ptr != NULL){
    if(strcmp(ptr -> home,home) ==0 && strcmp(ptr -> away,away) ==0){
      ptr2 = ptr -> r;
      while(ptr2 != NULL){
	if(ptr2->year ==year){ /*年度が一致しているか条件式を追加*/
	  count++;
	  if(ptr2->home_score > ptr2 -> away_score){
	    win++;
	  }else if(ptr2 -> home_score < ptr2 -> away_score){
	    lose++;
	  }else{
	    draw++;
	  }
	}
	ptr2 = ptr2 -> next;
      }
      break;
    }
    ptr = ptr -> next;
  }
  printf("[year:%d]: %s (HOME) vs %s (AWAY) : %d games.(win:%d, lose:%d, draw: %d)\n" , year, home, away, count, win, lose, draw);
}



int main(){
  char home_team[256], away_team[256];
  int home_score, away_score;
  int year, month, day, i, f;
  char *filename = "jleague.txt";
  FILE *fp;

  for(i=0; i < HASHSIZE; i++){
    hashtable[i]=NULL;
  }

  
  fp = fopen(filename,"r");
  while((f = fscanf(fp,"%d %d %d %s %d %d %s",&year,&month,&day,home_team,&home_score,&away_score,away_team))!=EOF){
    add(year,month,day,home_team,home_score,away_score,away_team);
  }

  dist();
  record("Urawa_Red_Diamonds","Kashiwa_Reysol");
  record("Kashiwa_Reysol","Urawa_Red_Diamonds");
  record("Kashima_Antlers","Gamba_Osaka");
  record_year("Kashima_Antlers","Gamba_Osaka",2007);
}
