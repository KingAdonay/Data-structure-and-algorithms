from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(log)
        
        return len(stack)
    
# Tests
sol = Solution()
# Testcase 1: ["d1/","d2/","../","d21/","./"]
ans = sol.minOperations(["d1/","d2/","../","d21/","./"])
print(ans == 2)
# Testcase 2: ["d1/","../","../","../"]
ans = sol.minOperations(["d1/","../","../","../"])
print(ans == 0)