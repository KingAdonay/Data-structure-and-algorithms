class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        stack = []
        mapp = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        i = 0
        while i < n:
            if s[i] in mapp:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    open_par = stack.pop(len(stack) - 1)
                    if mapp[open_par] != s[i]:
                        return False
                else:
                    return False
                
            i += 1
        
        if len(stack) != 0:
            return False
        
        return True

# Tests
solution = Solution()

# Testcase 1: "()" to be True
print(solution.isValid('()'))
# Testcase 2: "()[]{}" to be True
print(solution.isValid("()[]{}"))
# Testcase 4: "([])" to be True
print(solution.isValid("([])"))
# Testcase 4: "(]" to be False
print(solution.isValid("(]"))
# Testcase 5: "((" to be False
print(solution.isValid("(("))
# Testcase 6: ")" to be False
print(solution.isValid(")"))
