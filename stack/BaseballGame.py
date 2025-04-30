from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if stack and val == 'C':
                stack.pop()
            elif stack and val == 'D':
                d = stack[-1] * 2
                stack.append(d)
            elif len(stack) > 1 and val == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(val))
       
        sum = 0
        for i in range(len(stack)):
            sum += stack[i]
        
        return sum

# Tests
sol = Solution()
# Testcase 1: ["5","2","C","D","+"]
sum = sol.calPoints(["5","2","C","D","+"])
print(sum == 30)
# Testcase 2: ["5","-2","4","C","D","9","+","+"]
sum = sol.calPoints(["5","-2","4","C","D","9","+","+"])
# print(sum == 27)  