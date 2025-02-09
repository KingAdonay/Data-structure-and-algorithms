from typing import List


class Solution:
    def getStack(self, s:str) -> List[str]:
        stack = []

        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = self.getStack(s)
        stack2 = self.getStack(t)

        return stack1 == stack2

        
# Tests
sol = Solution()
# Testcase 1: "ab#c", "ad#c"
print(True == sol.backspaceCompare("ab#c", "ad#c"))
# Testcase 2: "y#fo##f", "y#f#o##f"
print(True == sol.backspaceCompare("y#fo##f", "y#f#o##f"))