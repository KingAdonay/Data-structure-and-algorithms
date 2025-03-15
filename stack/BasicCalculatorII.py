
class Solution:
    def evaluate(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            return num1 // num2
        
    def calculate(self, s: str) -> int:
        string = s.replace(' ', '')
        n = len(string)
    
        operator_priority = {
            "+": 0,
            "-": 0,
            "*": 1,
            "/": 1,
            "eol": 0
        }

        stack = []
        st = ""
        for i, char in enumerate(string):
            if char in operator_priority:
                st = ""
                continue
            
            if i < n-1 and string[i + 1] not in operator_priority:
                st += char
                continue
            
            st += char
            op = string[i + 1] if i < n-1 else "eol"
            num = int(st)

            while stack and operator_priority[stack[-1][1]] >= operator_priority[op]:
                last_num = stack.pop()
                num = self.evaluate(last_num[0], num, last_num[1])
            
            stack.append((num, op))
            

        while len(stack) > 1:
            num1 = stack.pop()
            num2 = stack.pop()
            num = self.evaluate(num2[0], num1, num2[1])
            stack.append((num, num1[1]))
        
        return stack[0][0]

# Tests
sol = Solution()
# Tescase 1: s = "3+2*2" result = 7
print(7 == sol.calculate("3+2*2"))
# Testcase 2: s = " 3/2 " result = 1
print(1 == sol.calculate(" 3/2 "))
# Testcase 3: s = " 3+5 / 2 " result = 5
print(5 == sol.calculate(" 3+5 / 2 "))
# Testcase 4: s = "32+6*2/3" result = 36
print(36 == sol.calculate("32+6*2/3"))
