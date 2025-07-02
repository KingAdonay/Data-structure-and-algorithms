from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        # -> store prefix only without self
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix = nums[i] * prefix

        # <- multiply prefix with suffix except self
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = nums[i] * suffix

        return answer

# Tests
sol = Solution()
# Testcase 1:
print(sol.productExceptSelf([0,0,1]) == [0,0,0])
# Testcase 2:
print(sol.productExceptSelf([1,2,3,4]) == [24,12,8,6])
# Testcase 3:
print(sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])