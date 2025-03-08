from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) -1
        maxx = 0

        while i <= j:
            h=height[i]
            if height[i]<= height[j]:
                h=height[i]
                i += 1
            else:
                h = height[j]
                j -= 1

            area = h * (j-i+1)
            maxx=max(maxx,area)
            
        return maxx

# Tests
sol = Solution()
# Testcase 1: [1,8,6,2,5,4,8,3,7], expected = 49
print(49 == sol.maxArea([1,8,6,2,5,4,8,3,7]))
# Testcase 2: [1,1], expected = 1
print(1 == sol.maxArea([1,1]))