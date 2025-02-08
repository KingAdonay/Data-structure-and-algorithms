class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        starts = []

        n = len(s)

        for i in range(n):
            if s[i] == '(':
                starts.append(len(stack))
            elif s[i] == ')':
                if len(starts) > 0:
                    start_idx = starts.pop(-1)

                    if len(stack) > 0:
                        right = len(stack) - 1
                        left = start_idx
                        while left < right:
                            stack[left], stack[right] = stack[right], stack[left]
                            left += 1
                            right -= 1 
            else:
                stack.append(s[i])
        
        return ''.join(stack)
    
# Tests
sol = Solution()
# Testcase 1: "(abcd)"
string = sol.reverseParentheses("(abcd)")
print(string == 'dcba')
# Testcase 2: "(u(love)i)"
string = sol.reverseParentheses("(u(love)i)")
print(string == 'iloveu')
# Testcase 3: "(ed(et(oc))el)"
string = sol.reverseParentheses("(ed(et(oc))el)")
print(string == 'leetcode')