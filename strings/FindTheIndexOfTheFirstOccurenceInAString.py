'''
    28. Find the Index of the First Occurrence in a String
    
    Use a fixed length sliding window to check if the current substring is equal to the needle.
    If so, return the starting index of the substring, if not, after exhausting all possibilities, return -1.
    
    Time complexity: O(n * m), where n is the length of the haystack and m is the length of the needle. This is because we are checking each substring of the haystack against the needle.
    Space complexity: O(m) for the sliding window substring.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1
        
        cur = haystack[0:len(needle)]
        for i in range(len(needle), len(haystack)):
            if cur == needle:
                return i - len(needle)
            
            cur += haystack[i]
            cur = cur[-len(needle):]
        
        return len(haystack) - len(needle) if cur == needle else -1
    
# Testcases:
s = Solution()
print(s.strStr("hello", "ll") == 2)
print(s.strStr("aaaaa", "bba") == -1)
print(s.strStr("a", "a") == 0)
print(s.strStr("mississippi", "issip") == 4)