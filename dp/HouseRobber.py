from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        arr = [nums[0], max(nums[0], nums[1])]
        for idx in range(2, n):
            arr.append(max(arr[idx-1], arr[idx-2] + nums[idx]))
        
        return arr[n-1]


# Tests
sol = Solution()
# Testcase 1: [1,2,3,1]
print(sol.rob([1,2,3,1]) == 4)
# Testcase 2: [2, 1, 1, 2]
print(sol.rob([2,1,1,2]) == 4)
# Testcase 3: [2,7,9,3,1]
print(sol.rob([2,7,9,3,1]) == 12)