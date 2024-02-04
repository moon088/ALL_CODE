#include<iostream>
#include<cstring>
#define HASHSIZE 17
using namespace std;
using ll = long long;


template <typename T>
class Member_list{
  Member_list<T>* next = NULL;
  char name[16] ;
  T age ;

public:
  Member_list<T>* operator()(const char* c) const;
  int hash(const char* key) const;
  Member_list<T>* insert(const char* name, const T age);
  void operator-= (const char* c); 
  const char* fetch_name() const;
  void update_name(const char* name);
  T fetch_age() const;
  void update_age(const T age); 
  Member_list<T>* fetch_next() const;
  void update_next(Member_list* next);
};


template <typename T>
Member_list<T>* Member_list<T>::operator() (const char* c) const{
  const Member_list<T> *p = this;           
  while(p != NULL){
    if(strcmp(c, p ->name) == 0){
      return const_cast<Member_list<T>*>(p); 
    }
    p = p -> fetch_next();
    }
  return NULL;
}

template <typename T>
int Member_list<T>::hash(const char* key) const{
  int hashval = 0;
  while(*key != '\0'){
    hashval += *key;
    key++;
  }
  return hashval % HASHSIZE;
}

template <typename T>
Member_list<T>* Member_list<T>::insert(const char* name, const T age){
  Member_list<T> *ptr = new Member_list<T>;  
  ptr->update_name(name); 
  ptr->update_age(age);
  ptr->update_next(this);
  return ptr;
}


template<typename T>
void Member_list<T>::operator-= (const char* name){
  Member_list<T> *p = this -> fetch_next();
  Member_list<T> *prev = this; 
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

template <typename T>
const char* Member_list<T>::fetch_name() const{
  return this -> name;
}

template <typename T>
void Member_list<T>::update_name(const char* name){
  strcpy(this->name,name);
}

template <typename T>
T Member_list<T>::fetch_age() const{
  return this -> age;
}

template <typename T>
void Member_list<T>::update_age(const T age){
  this -> age = age;
}

template <typename T>
Member_list<T>* Member_list<T>::fetch_next() const {
  return next;
}

template <typename T>
void Member_list<T>::update_next(Member_list<T>* next){
  this->next = next;
}

template <typename T>
class Hashtable{
  Member_list<T>* hashtable[HASHSIZE];
  Member_list<T>* fetch_member(int hashval) const;        
  void update_member(int hashval, Member_list<T>* member); 

public:
  Hashtable();
  Member_list<T>* operator() (const char* c) const;
  int hash(const char* hashkey) const;
  void insert(const char* name, const T age);
  void operator-= (const char* c);
};

template <typename T>
Member_list<T>* Hashtable<T>::fetch_member(int hashval) const {
  return hashtable[hashval] ;
}

template <typename T>
void Hashtable<T>::update_member(int hashval, Member_list<T>* member) {
  hashtable[hashval] = member;
}

template <typename T>
Hashtable<T>::Hashtable(){
  for(int i = 0; i < HASHSIZE; i++){
    hashtable[i] = NULL;
  }
}

template <typename T>
Member_list<T>* Hashtable<T>::operator() (const char* c) const{
  return fetch_member(hash(c)) -> operator() (c);
}

template <typename T>
int Hashtable<T>::hash(const char* hashkey) const{
  int hashval = 0;
  while(*hashkey != '\0'){
    hashval += *hashkey;
    hashkey++;
    }
  return hashval % HASHSIZE;
}

template <typename T>
void Hashtable<T>::insert(const char* name, const T age) {
  int hashval = hash(name);
  if(fetch_member(hashval) == NULL) {
    hashtable[hashval] = new Member_list<T>;
    hashtable[hashval]->update_name(name); 
    hashtable[hashval]->update_age(age); 
  } else {
    Member_list<T>* new_member = hashtable[hashval]->insert(name,age); 
    if (new_member != NULL) {
      update_member(hashval , new_member);
    }
  }
}

template <typename T>
void Hashtable<T>::operator-= (const char* c) {
  int hashval = hash(c);
  if (fetch_member(hashval) != NULL) {
    if(strcmp(fetch_member(hashval)->fetch_name(), c) == 0) { 
      Member_list<T>* to_delete = fetch_member(hashval);
      update_member(hashval,  fetch_member(hashval) ->fetch_next()); 
      delete to_delete;
    } else {
      fetch_member(hashval)->operator-= (c);
    }
  }
}

int main(){
  char word[1024];
  Member_list<float>* ptr; //この2行の型を変える  
  Hashtable<float> table; 

  
  table.insert("takimoto",42.2);
  table.insert("katsurada" ,122.3);
  table.insert("matsuzawa" , 35.1);
  table.insert("ohmura" , 12.3);
  table-="takimoto";


  while(scanf("%s" , word)!= EOF){
    ptr = table(word);
    if(ptr!= NULL){
      cout<<ptr->fetch_name()<< "" <<ptr ->fetch_age()<<endl;      
    }
    else{
      cout << "none" << endl;
    }
  }
  return 0;
}
