from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1,7,3,6,5,6]
        # [1,8,11,17,22,28]
        # [28,27,20,17,11,6]
        # find the prefix sum from the left and the right side until the selected idx

        # n = len(nums)
        # prefix_sum_left = [0] * n
        # prefix_sum_right = [0] * n
        # prev = 0
        # for idx, num in enumerate(nums):
        #     prefix_sum_left[idx] = prev + num
        #     prev = prefix_sum_left[idx]
        # prev = 0
        # for i in range(n - 1, -1, -1):
        #     num = nums[i]
        #     prefix_sum_right[i] = prev + num
        #     prev = prefix_sum_right[i]
        
        # for i in range(n):
        #     left_sum, right_sum = 0, 0
        #     if i > 0:
        #         left_sum = prefix_sum_left[i-1]
        #     if i - n + 1 < 0:
        #         right_sum = prefix_sum_right[i - n + 1]
            
        #     if left_sum == right_sum:
        #         return i

        # return -1

        summ = sum(nums)
        prefix_sum = 0
        for idx, num in enumerate(nums):
            right = summ - prefix_sum - num
            if right == prefix_sum:
                return idx
            
            prefix_sum += num
        
        return -1

# Tests
sol = Solution()
# Testcase 1: [1,7,3,6,5,6]
print(sol.pivotIndex([1,7,3,6,5,6]) == 3)
# Testcase 2: [1,2,3]
print(sol.pivotIndex([1,2,3]) == -1)
# Testcase 3: [2,1,-1]
print(sol.pivotIndex([2,1,-1]) == 0)

