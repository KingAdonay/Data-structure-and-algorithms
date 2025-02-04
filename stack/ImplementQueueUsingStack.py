class MyQueue:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.bottom = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            val = self.stack[self.bottom]
            self.stack[self.bottom] = None
            self.bottom += 1
            return val

    def peek(self) -> int:
        if self.size > 0:
            return self.stack[self.bottom]
        
        return None

    def empty(self) -> bool:
        return self.size <= 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# output
# [null,null,null,1,1,false]