from typing import Optional


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def findNodeAtIndex(self, index: int) -> Optional[Node]:
        node = self.head

        i = 0
        while node and i < index:
            node = node.next
            i += 1
        
        return node
    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0 or not self.head:
            return -1

        curr = self.findNodeAtIndex(index)
 
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.size == 0:
            self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail:
            self.tail.next = node
        self.tail = node

        if self.size == 0:
            self.head = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return None
    
        if index == 0:
            self.addAtHead(val)
            return None
        
        prev_index = index - 1
        if prev_index >= 0 and index < self.size:
            prev = self.findNodeAtIndex(prev_index)
            node = Node(val, prev.next)
            prev.next = node
            self.size += 1
    def deleteHead(self) -> None:
        if self.head:
            curr = self.head
            self.head = self.head.next
            if self.size == 1:
                self.tail = self.head
            curr.next = None
            self.size -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.deleteHead()
            return None
        prev_index = index - 1
        if prev_index >= 0 and prev_index < self.size - 1:
            prev_node = self.findNodeAtIndex(prev_index)
            curr = prev_node.next
            prev_node.next = curr.next
            curr.next = None
            
            if index == self.size - 1:
                self.tail = prev_node
            
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)