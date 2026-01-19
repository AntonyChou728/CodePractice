// Last update: 2026/01/19

#include <iostream>

struct Node{
    int val;
    Node* next;
    Node(int v) : val(v), next(nullptr) {}
};

class reversedLinkedList {
private:
    Node* head; 
    int size;
public:
    reversedLinkedList() {
        head = nullptr; 
        size = 0;
    }
    void addAtHead(int val) {
        Node* newNode = new Node(val); 
        newNode->next = head;          
        head = newNode;                
        size++;
    }
    void reverse() {
        Node* prev = nullptr;           
        Node* curr = head;              
        while (curr != nullptr) {
            Node* nextTemp = curr->next; // 暫存下一個節點
            curr->next = prev;          // 反轉指標
            prev = curr;                // prev標向前走一步
            curr = nextTemp;            // curr指標向前走一步
        }
        head = prev; // 更新頭指標
    }
    
// 圖解:
// (前路是空的)      (目前在這裡)
//    nullptr           3  ->  2  ->  1  ->  nullptr
//     (prev)         (curr)
//---------------------------------------------
// 開始反轉指標     nullptr  <-  3       2  ->  1  ->  nullptr
//                           (prev)   (curr)
//---------------------------------------------
//    nullptr  <-  3  <-  2           1  ->  nullptr
//                      (prev)      (curr)
//---------------------------------------------
//    nullptr  <-  3  <-  2  <-  1           nullptr
//                             (prev)        (curr)
// 最終串列 1 -> 2 -> 3 -> nullptr
    
    void printList() {
        Node* curr = head;
        while (curr != nullptr) {
            std::cout << curr->val << " ";
            curr = curr->next;
        }
        std::cout << std::endl;
    }
};

int main(){
    reversedLinkedList rll;
    rll.addAtHead(1);
    rll.addAtHead(2);
    rll.addAtHead(3);
    std::cout << "Original list: ";
    rll.printList();
    rll.reverse();
    std::cout << "Reversed list: ";
    rll.printList();
    return 0;
}