from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        i, j = 0, 0
        first_window_sum = 0
        max_sum = 0

        while j < firstLen - 1:
            first_window_sum += nums[j]
            j += 1
        
        while j < n:
            first_window_sum += nums[j]
            i2, j2 = 0, 0
            if i <= secondLen - 1 <= j or 0 <= j <= secondLen - 1:
                i2, j2 = j + 1, j+ 1
            second_window_sum = 0
            k = 0
            while j2 < n and k < secondLen - 1:
                second_window_sum += nums[j2]
                j2 += 1
                k+=1
            
            while j2 < n:
                second_window_sum += nums[j2]
                if not (i <= j2 <= j or i2 <= j <= j2):
                    max_sum = max(max_sum, first_window_sum + second_window_sum)
                second_window_sum -= nums[i2]
                i2 += 1
                j2 += 1

            first_window_sum -= nums[i]
            i += 1
            j += 1
        
        return max_sum
    
# Tests
sol = Solution()
# Testcase 1:
nums = [0,6,5,2,2,5,1,9,4]
length1, length2 = 1, 2
print(sol.maxSumTwoNoOverlap(nums, length1, length2) == 20)
# Testcase 2:
nums = [3,8,1,3,2,1,8,9,0]
length1, length2 = 3, 2
print(sol.maxSumTwoNoOverlap(nums, length1, length2) == 29)
# Testcase 3:
nums = [2,1,5,6,0,9,5,0,3,8]
length1, length2 = 4, 3
print(sol.maxSumTwoNoOverlap(nums, length1, length2) == 31)