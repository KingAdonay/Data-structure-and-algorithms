from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        i, j = 0, 0
        stack = []

        while i < n:
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
            i += 1
        
        while j < n:
            if stack and stack[-1] == popped[j]:
                stack.pop()
            else:
                return False
            
            j += 1

        
        return True
            

# Tests
sol = Solution()
# Testcase 1:
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(sol.validateStackSequences(pushed, popped) == False)
# Testcase 2:
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(sol.validateStackSequences(pushed, popped) == True)
# Testcase 3:
pushed = [0,2,1]
popped = [0,1,2]
print(sol.validateStackSequences(pushed, popped) == True)
