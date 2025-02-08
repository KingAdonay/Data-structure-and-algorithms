class Node:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value

class MinStack:

    def __init__(self):
        self.minn = float('inf')
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minn = val
            self.stack.append(Node(val, val))
        else:
            self.minn = min(self.minn, val)
            self.stack.append(Node(val, self.minn))
        
    def pop(self) -> None:
        n = len(self.stack)
        if n > 0:
            self.stack.pop(n - 1)
            if len(self.stack) > 0:
                self.minn = self.stack[len(self.stack) - 1].min_value

    def top(self) -> int:
        n = len(self.stack)
        if n > 0:
            return self.stack[n - 1].value

    def getMin(self) -> int:
        n = len(self.stack)
        if n > 0:
            return self.stack[n - 1].min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Testcases: 
# actions: ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
# arguments: [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
# result: [null,null,null,-10,-10,null,-20,-20,-20,-20,null,null,null,-10,null,null,-7,-10,null]