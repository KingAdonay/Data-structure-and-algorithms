from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'
        stack = []

        for s in tokens:
            if s in operators:
                num1 = stack.pop(len(stack) - 1)
                num2 = stack.pop(len(stack) - 1)

                if s == operators[0]:
                    stack.append(num2 + num1)
                elif s == operators[1]:
                    stack.append(num2 - num1)
                elif s == operators[2]:
                    stack.append(num2 * num1)
                elif s == operators[3]:
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(s))
        
        return stack[0]   
        
# Tests
solution = Solution()

# Testcase 1: ["2","1","+","3","*"]
val = solution.evalRPN(["2","1","+","3","*"])
print(val == 9)
# Testcase 2: ["4","13","5","/","+"]
val = solution.evalRPN(["4","13","5","/","+"])
print(val == 6)