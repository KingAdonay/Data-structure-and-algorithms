class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        min_char = ord('a')
        n = len(palindrome)
        min_ord = float('inf')
        min_position = -1
        for i in range(n//2):
            for j in range(min_char, min_char + 26):
                if chr(j) != palindrome[i]:
                    if j < min_ord:
                        min_ord = j
                        min_position = i
                    break
        
        if min_position != -1:
            if min_ord > ord(palindrome[min_position]):
                min_position = n - 1 - min_position
            
            return f"{palindrome[:min_position]}{chr(min_ord)}{palindrome[min_position + 1:]}"

        return ''
                
                
# Tests
sol = Solution()
# Testcase 1: aabbaa
print(sol.breakPalindrome('aabbaa') == 'aaabaa')
# Testcase 2: a
print(sol.breakPalindrome('a') == '')
# Testcase 3: aabbaa
print(sol.breakPalindrome('abccba') == 'aaccba')
# Testcase 4: aabbaa
print(sol.breakPalindrome('aa') == 'ab')