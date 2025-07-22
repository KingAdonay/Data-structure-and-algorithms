class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurance = {} # O(26) -> constant space {a: 2, b: 4, c: 3}
        for idx, char in enumerate(s):
            last_occurance[char] = idx
        
        used = set() # O(26) -> constant space
        stack = [] # [a,b,...] -> O(n) space
        for idx, char in enumerate(s):
            if char not in used:
                while stack and stack[-1] > char and last_occurance[stack[-1]] > idx:
                    used.discard(stack.pop())
                
                stack.append(char)
                used.add(char)
        
        return ''.join(stack)

# Tests
sol = Solution()
# Testcase 1:
print(sol.removeDuplicateLetters("bcabc") == "abc")
# Testcase 2:
print(sol.removeDuplicateLetters("cbacdcbc") == "acdb")
# Testcase 3:
print(sol.removeDuplicateLetters("aabbcbbaa") == "abc")
# Testcase 4:
print(sol.removeDuplicateLetters("abacb") == "abc")