class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        i = 0
        max_len = 0
        for idx, c in enumerate(s):
            while c in letters and i < idx:
                letters.remove(s[i])
                i += 1
            letters.add(c)
            max_len = max(max_len, len(letters))
        
        return max_len

# Tests
sol = Solution()
# Testcase 1:
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s) == 3)
# Testcase 2:
s = "bbbbb"
print(sol.lengthOfLongestSubstring(s) == 1)
# Testcase 3:
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s) == 3)
# Testcase 4:
s = " "
print(sol.lengthOfLongestSubstring(s) == 1)