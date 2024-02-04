#include<iostream>
#include<cstring>
#define HASHSIZE 17
using namespace std;

template <typename T>
class Member_list{
  Member_list* next = NULL;
  char name[16] ;
  T age ;
public:
  Member_list* operator()(const char* c) const;
  int hash(const char* key) const;
  Member_list* insert(const char* name, const T age);
  void operator-= (const char* c); 

  const char* getName() const;
  void setName(const char* name);
  T getAge() const;
  void setAge(const T age); 
  Member_list* getNext() const;
  void setNext(Member_list* next);
};

template <typename T>
Member_list<T>* Member_list<T>::operator() (const char* c) const{
  const Member_list *p = this;           
  while(p != NULL){
    if(strcmp(c, p ->name) == 0){
      return const_cast<Member_list*>(p); 
    }
    p = p -> getNext();
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
  Member_list *ptr = new Member_list;  
  ptr->setName(name); 
  ptr->setAge(age);
  ptr->setNext(this);
  return ptr;
}

template <typename T>
void Member_list<T>::operator-= (const char* name){
  Member_list *p = this -> getNext();
  Member_list *prev = this; 
  
  while(p != NULL){
    if(strcmp(name, p->getName()) == 0){ 
      prev -> setNext(p -> getNext());
      delete p;
      return ;
    }
    prev = p;
    p = p -> next;
  }
}

template <typename T>
const char* Member_list<T>::getName() const{
  return this -> name;
}

template <typename T>
void Member_list<T>::setName(const char* name){
  strcpy(this->name, name);
}

template <typename T>
T Member_list<T>::getAge() const{
  return this -> age;
}

template <typename T>
void Member_list<T>::setAge(const T age){
  this -> age = age;
}

template <typename T>
Member_list<T>* Member_list<T>::getNext() const {
  return next;
}

template <typename T>
void Member_list<T>::setNext(Member_list<T>* next){
  this->next = next;
}

template <typename T>
class Hashtable{
  Member_list<T>* hashtable[HASHSIZE];
  Member_list<T>* getMember(int hashval) const;        
  void setMember(int hashval, Member_list<T>* member); 
public:
  Hashtable();
  Member_list<T>* operator() (const char* c) const;
  int hash(const char* key) const;
  void insert(const char* name, const T age);
  void operator-= (const char* c);
};

template <typename T>
Member_list<T>* Hashtable<T>::getMember(int hashval) const {
  return hashtable[hashval] ;
}

template <typename T>
void Hashtable<T>::setMember(int hashval, Member_list<T>* member) {
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
  return getMember(hash(c)) -> operator() (c);
}

template <typename T>
int Hashtable<T>::hash(const char* key) const{
  int hashval = 0;
  while(*key != '\0'){
    hashval += *key;
    key++;
    }
  return hashval % HASHSIZE;
}

template <typename T>
void Hashtable<T>::insert(const char* name, const T age) {
  int hashval = hash(name);
  if(getMember(hashval) == NULL) {
    hashtable[hashval] = new Member_list<T>;
    hashtable[hashval]->setName(name); 
    hashtable[hashval]->setAge(age); 
  } else {
    Member_list<T>* new_member = hashtable[hashval]->insert(name,age); 
    if (new_member != NULL) {
      setMember(hashval , new_member);
    }
  }
}

template <typename T>
void Hashtable<T>::operator-= (const char* c) {
  int hashval = hash(c);
  if (getMember(hashval) != NULL) {
    if(strcmp(getMember(hashval)->getName(), c) == 0) { 
      Member_list<T>* to_delete = getMember(hashval);
      setMember(hashval,  getMember(hashval) ->getNext()); 
      delete to_delete;
    } else {
      getMember(hashval)->operator-= (c);
    }
  }
}

int main(){
  char word[1024];
  Member_list<int>* ptr;
  
  Hashtable<int> table;
  table.insert("takimoto",42);
  table.insert("katsurada" ,122);
  table.insert("matsuzawa" , 35);
  table.insert("ohmura" , 12);
  table-="takimoto";
  while(scanf("%s" , word)!= EOF){
    ptr = table(word);
    if(ptr!= NULL){
      printf("%s, %i\n" , ptr->getName(), ptr->getAge() );
    }
    else{
      printf("none\n");
    }
  }
  return 0;
}
