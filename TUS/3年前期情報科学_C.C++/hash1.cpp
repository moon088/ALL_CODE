#include<iostream>
#include<cstring>
#define HASHSIZE 17
using namespace std;
using ll = long long;

class Member_list{
  Member_list* next = NULL;
  char name[16] ;
  ll age ;

public:
  Member_list* operator()(const char* c) const;
  int hash(const char* key) const;
  Member_list* insert(const char* name, const ll age);
  void operator-= (const char* c); 
  const char* fetch_name() const;
  void update_name(const char* name);
  ll fetch_age() const;
  void update_age(const ll age); 
  Member_list* fetch_next() const;
  void update_next(Member_list* next);
};


Member_list* Member_list::operator() (const char* c) const{
  const Member_list *p = this;           
  while(p != NULL){
    if(strcmp(c, p ->name) == 0){
      return const_cast<Member_list*>(p); 
    }
    p = p -> fetch_next();
    }
  return NULL;
}

int Member_list::hash(const char* key) const{
  int hashval = 0;
  while(*key != '\0'){
    hashval += *key;
    key++;
  }
  return hashval % HASHSIZE;
}

Member_list* Member_list::insert(const char* name, const ll age){
  Member_list *ptr = new Member_list;  
  ptr->update_name(name); 
  ptr->update_age(age);
  ptr->update_next(this);
  return ptr;
}

void Member_list::operator-= (const char* name){
  Member_list *p = this -> fetch_next();
  Member_list *prev = this; 
  while(p != NULL){
    if(strcmp(name, p->fetch_name()) == 0){ 
      prev -> update_next(p -> fetch_next());
      delete p;
      return ;
    }
    prev = p;
    p = p -> next;
  }
}

const char* Member_list::fetch_name() const{
  return this -> name;
}

void Member_list::update_name(const char* name){
  strcpy(this->name,name);
}

ll Member_list::fetch_age() const{
  return this -> age;
}

void Member_list::update_age(const ll age){
  this -> age = age;
}

Member_list* Member_list::fetch_next() const {
  return next;
}

void Member_list::update_next(Member_list* next){
  this->next = next;
}

class Hashtable{
  Member_list* hashtable[HASHSIZE];
  Member_list* fetch_member(int hashval) const;        
  void update_member(int hashval, Member_list* member); 

public:
  Hashtable();
  Member_list* operator() (const char* c) const;
  int hash(const char* hashkey) const;
  void insert(const char* name, const ll age);
  void operator-= (const char* c);
};

Member_list* Hashtable::fetch_member(int hashval) const {
  return hashtable[hashval] ;
}

void Hashtable::update_member(int hashval, Member_list* member) {
  hashtable[hashval] = member;
}

Hashtable::Hashtable(){
  for(int i = 0; i < HASHSIZE; i++){
    hashtable[i] = NULL;
  }
}

Member_list* Hashtable::operator() (const char* c) const{
  return fetch_member(hash(c)) -> operator() (c);
}

int Hashtable::hash(const char* hashkey) const{
  int hashval = 0;
  while(*hashkey != '\0'){
    hashval += *hashkey;
    hashkey++;
    }
  return hashval % HASHSIZE;
}

void Hashtable::insert(const char* name, const ll age) {
  int hashval = hash(name);
  if(fetch_member(hashval) == NULL) {
    hashtable[hashval] = new Member_list;
    hashtable[hashval]->update_name(name); 
    hashtable[hashval]->update_age(age); 
  } else {
    Member_list* new_member = hashtable[hashval]->insert(name,age); 
    if (new_member != NULL) {
      update_member(hashval , new_member);
    }
  }
}

void Hashtable::operator-= (const char* c) {
  int hashval = hash(c);
  if (fetch_member(hashval) != NULL) {
    if(strcmp(fetch_member(hashval)->fetch_name(), c) == 0) { 
      Member_list* to_delete = fetch_member(hashval);
      update_member(hashval,  fetch_member(hashval) ->fetch_next()); 
      delete to_delete;
    } else {
      fetch_member(hashval)->operator-= (c);
    }
  }
}

int main(){
  char word[1024];
  Member_list* ptr;  
  Hashtable table;

  
  table.insert("takimoto",42);
  table.insert("katsurada" ,122);
  table.insert("matsuzawa" , 35);
  table.insert("ohmura" , 12);
  table-="takimoto";


  while(scanf("%s" , word)!= EOF){
    ptr = table(word);
    if(ptr!= NULL){
       cout<<ptr->fetch_name()<< "" <<ptr -> fetch_age()<<endl; 
    }
    else{
      cout << "none" << endl;
    }
  }
  return 0;
}
