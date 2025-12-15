'''
    5. Longest Palindromic Substring
    
    Use the expand around center technique to find the longest palindromic substring.
    For each character in the string, consider it as the center of a palindrome and expand outwards
    to find the longest palindrome for both odd-length and even-length palindromes.
    
    Time Complexity: O(n^2), where n is the length of the input string.
    Space Complexity: O(1), as we are using only constant extra space.
'''

class Solution:
    def get_palindrome_str(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            odd_p = self.get_palindrome_str(s, i, i)
            even_p = self.get_palindrome_str(s, i, i + 1)
            
            new_p = odd_p if len(odd_p) > len(even_p) else even_p
            if len(new_p) > len(p):
                p = new_p
        
        return p

# Testcases:
sol = Solution()
print(sol.longestPalindrome("babad") in ["bab", "aba"])
print(sol.longestPalindrome("cbbd") == "bb")
print(sol.longestPalindrome("a") == "a")
print(sol.longestPalindrome("ac") in ["a", "c"])