from typing import List

'''
    455. Assign Cookies
    
    Use a greedy approach to assign cookies to children.
    Sort both the greed factors and cookie sizes.
    Start from the largest greed factor and the largest cookie size,
    and assign cookies to children if the cookie size is sufficient.
    
    Time complexity: O(n log n + m log m) where n is the number of children and m is the number of cookies
    Space complexity: O(1)
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0

        j = len(s) - 1
        for i in range(len(g)-1, -1, -1):
            if j > -1 and s[j] >= g[i]:
                count += 1
                j -= 1

        return count

# Testcases
solution = Solution()
print(solution.findContentChildren([1,2,3], [1,1]))  # 1
print(solution.findContentChildren([1,2], [1,2,3]))  # 2
print(solution.findContentChildren([10,9,8,7], [5,6,7,8]))  # 2
print(solution.findContentChildren([1,2,3], []))  # 0 
print(solution.findContentChildren([10,9,8,7], [10,9,8,7]))  # 4