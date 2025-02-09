from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        mapping = {}

        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)

        while stack:
            mapping[stack.pop()] = -1
        
        for n in nums1:
            ans.append(mapping[n])
        
        return ans
    
# Tests
sol = Solution()
# Testcase 1: [1,3,5,2,4], [6,5,4,3,2,1,7]
ans = sol.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
print([7,7,7,7,7] == ans)
# Testcase 2: [2,4], [1,2,3,4]
ans = sol.nextGreaterElement([2,4], [1,2,3,4])
print([3, -1] == ans)