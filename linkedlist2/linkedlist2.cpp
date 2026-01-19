// leetcode linked list 實作
#include <iostream>

class MyLinkedList {
private:
    // 1. 定義節點結構 (Struct)
    // 這是鏈結串列的基本單位，包含數值 (val) 和指向下一個節點的指標 (next)
    struct Node {
        int val;
        Node* next;
        // 節點的建構子：方便我們用 new Node(val) 快速建立
        Node(int x) : val(x), next(nullptr) {}
    };

    Node* head; // 頭指標：永遠指向第一個節點
    int size;   // 目前串列的長度：方便判斷 index 是否合法

public:
    // 2. 初始化 (Constructor)
    MyLinkedList() {
        head = nullptr; // 一開始什麼都沒有，指向空
        size = 0;
    }
    
    // 3. 取得數值
    int get(int index) {
        // 檢查 index 是否越界
        if (index < 0 || index >= size) {
            return -1;
        }
        
        // 從頭開始走，走 index 步
        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }
    
    // 4. 在頭部加入
    void addAtHead(int val) {
        Node* newNode = new Node(val); // 建立新節點
        newNode->next = head;          // 新節點的下一個是原本的頭
        head = newNode;                // 更新頭指標，現在新節點是老大了
        size++;
    }
    
    // 5. 在尾部加入
    void addAtTail(int val) {
        // 如果目前是空的，等同於在頭部加入
        if (size == 0) {
            addAtHead(val);
            return;
        }
        
        // 否則，要先走到最後一個節點
        Node* curr = head;
        while (curr->next != nullptr) { // 當 next 不是空，代表還沒到底
            curr = curr->next;
        }
        
        // 此時 curr 是最後一個節點
        Node* newNode = new Node(val);
        curr->next = newNode; // 接上去
        size++;
    }
    
    // 6. 插入
    void addAtIndex(int index, int val) {
        // 處理特殊邊界情況
        if (index > size) return; // 超出範圍，不處理
        if (index <= 0) {         // 插在最前面
            addAtHead(val);
            return;
        }
        if (index == size) {      // 插在最後面
            addAtTail(val);
            return;
        }
        
        // 一般情況：要找到 index 的「前一個節點」(index - 1)
        Node* prev = head;
        for (int i = 0; i < index - 1; i++) {
            prev = prev->next;
        }
        
        // 開始接水管 (Pointer 操作)
        Node* newNode = new Node(val);
        newNode->next = prev->next; // 1. 新節點先抓住後面的
        prev->next = newNode;       // 2. 前面的節點抓住新節點
        size++;
    }
    
    // 7. 刪除特定位置
    void deleteAtIndex(int index) {
        // 檢查 index 是否合法
        if (index < 0 || index >= size) return;
        
        // 特殊情況：刪除頭部
        if (index == 0) {
            Node* temp = head; // 先暫存舊的頭
            head = head->next; // 頭指標往後移一位
            delete temp;       // 釋放舊頭的記憶體 (重要！C++需要手動釋放)
            size--;
            return;
        }
        
        // 一般情況：找到 index 的「前一個節點」(index - 1)
        Node* prev = head;
        for (int i = 0; i < index - 1; i++) {
            prev = prev->next;
        }
        
        // 執行刪除
        Node* target = prev->next; // 要刪除的目標
        prev->next = target->next; // 跳過目標，直接接下一位
        delete target;             // 釋放目標記憶體
        size--;
    }
};

int main(){
    MyLinkedList linkedList;
    linkedList.addAtHead(1);
    linkedList.addAtTail(3);
    linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
    int val1 = linkedList.get(1); // return 2
    linkedList.deleteAtIndex(1);  // now the linked list is 1->3
    int val2 = linkedList.get(1); // return 3

    std::cout << "Value at index 1 before deletion: " << val1 << std::endl;
    std::cout << "Value at index 1 after deletion: " << val2 << std::endl;

    return 0;
}