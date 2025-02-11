class QueueNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head = None
        self.tail = None
        

    def insertFront(self, value: int) -> bool:
        if self.size < self.max_size:
            node = QueueNode(value, self.head, None)
            if self.size > 0:
                self.head.prev = node
            self.head = node
            if self.size == 0:
                self.tail = node
            
            self.size += 1
            return True
        
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.max_size:
            node = QueueNode(value, None, self.tail)
            if self.size > 0:
                self.tail.next = node
            
            self.tail = node
            
            if self.size == 0:
                self.head = node
            
            self.size += 1

            return True
        
        return False
        

    def deleteFront(self) -> bool:
        if self.size > 0:
            next = self.head.next
            self.head.next = None
            if next != None:
                next.prev = None
            
            self.head = next
            
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            prev = self.tail.prev
            self.tail.prev = None

            if prev != None:
                prev.next = None

            self.tail = prev
            self.size -= 1
            return True
        return False
        

    def getFront(self) -> int:
        if self.size > 0:
            return self.head.val

        return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.tail.val
        
        return -1
        
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        
        return False
        

    def isFull(self) -> bool:
        if self.size == self.max_size:
            return True
        
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# Testcase 1: 
# operations: ["MyCircularDeque","insertFront","getFront","isEmpty","deleteFront","insertLast","getRear","insertLast","insertFront","deleteLast","insertLast","isEmpty"]
# inputs: [[8],[5],[],[],[],[3],[],[7],[7],[],[4],[]]