#include <iostream>

// // Linked List 單向與雙向實作
// struct Node{
//     int val;
//     Node* next;
// };

// struct doubleNode{
//     int val;
//     doubleNode* next;
//     doubleNode* prev;
// };


// int main(){
//     Node* head = new Node();
//     head->val = 10;
//     head->next = new Node();
//     head->next->val = 20;
//     head->next->next = nullptr;
//     std::cout << "Single way linked list: " << head->val << " " << head->next->val << std::endl;

//     doubleNode* dhead = new doubleNode();
//     dhead->val = 10;
//     dhead->next = new doubleNode();
//     dhead->next->val = 20;
//     dhead->next->prev = dhead;
//     dhead->next->next = nullptr;
//     std::cout << "Double way linked list: " << dhead->val << " " << dhead->next->val << " " << dhead->next->prev->val << std::endl;

//     delete head->next;
//     delete head;
//     delete dhead->next;
//     delete dhead;
    
//     return 0;
// }


// Gemini 進階版本

struct Node {
    int val;
    Node* next;
    Node(int v) : val(v), next(nullptr) {} // 加入建構子，讓初始化更方便
};

struct doubleNode {
    int val;
    doubleNode* next;
    doubleNode* prev;
    doubleNode(int v) : val(v), next(nullptr), prev(nullptr) {} // 同樣加入建構子
};

int main() {
    // 1. Singly Linked List
    Node* head = new Node(10);      // 直接在 new 時給值
    head->next = new Node(20);
    
    std::cout << "Singly: " << head->val << " -> " << head->next->val << std::endl;

    // 2. Doubly Linked List
    doubleNode* dhead = new doubleNode(10);
    doubleNode* dnode1 = new doubleNode(20);
    
    // 串接
    dhead->next = dnode1;
    dnode1->prev = dhead;


    std::cout << "Doubly: " << dhead->val << " <-> " << dhead->next->val << " (prev check: " << dhead->next->prev->val << ")" << std::endl;

    delete head->next;
    delete head;
    
    delete dhead->next;
    delete dhead;       

    return 0;
}