from typing import List
'''
    14. Longest common prefix
    
    Start with the first string as the prefix and iteatively shorten it until all strings match the prefix.
    
    Time Complexity: O(N * M) where N is the number of strings and M is the length of the longest string.
    Space Complexity: O(1)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            while prefix and not word.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
    
# Testcases
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]) == 'fl')  # Output: "fl
print(sol.longestCommonPrefix(["dog","racecar","car"]) == '')     # Output: ""
print(sol.longestCommonPrefix(["interspecies","interstellar","interstate"]) == 'inters')  # Output: "inters"
print(sol.longestCommonPrefix(["throne","throne"]) == 'throne')  # Output: "throne"
print(sol.longestCommonPrefix([""]) == '')  # Output: ""