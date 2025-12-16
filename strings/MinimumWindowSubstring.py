from collections import Counter, defaultdict

'''
    76. Minimum Window Substring
    
    Use a sliding window approach with two pointers.
    
    Use a counter to track the characters needed from  t and a dictionary to track extra (duplicate) characters in the current window.
    Expand the right pointer, and decrease the count in the conter for each character found, if not included in the counter, add it to extras.
    When all characters are found (counter is empty), try to contract the window from the left to find the minimum window.
    Update the minimum window substring whenever a valid window is found.
    
    Time complexity: O(m + n), where m is the length of s and n is the length of t.
    Space complexity: O(k), where k is the number of unique characters in t.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        extras = defaultdict(int)
        sett = set(t)
        st = ''
        left = 0
        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] == 0:
                    del counter[s[right]]
            elif s[right] in sett:
                extras[s[right]] += 1
            
            while not counter and left <= right:
                st = s[left:right + 1] if not st or len(st) > (right - left) + 1 else st
                if s[left] in sett and extras[s[left]] == 0:
                    if s[left] not in counter:
                        counter[s[left]] = 0
                    counter[s[left]] += 1
                elif s[left] in sett:
                    extras[s[left]] -= 1

                left += 1
        return st

# Testcases:
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC") == "BANC")
print(sol.minWindow("a", "a") == "a")
print(sol.minWindow("a", "aa") == "")
print(sol.minWindow("ab", "A") == "")
print(sol.minWindow("aaflslflsldkalskaaa", "aaa") == "aaa")
print(sol.minWindow("aa", "aa") == "aa")
print(sol.minWindow("a", "b") == "")