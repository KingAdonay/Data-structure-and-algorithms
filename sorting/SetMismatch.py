from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        sett = set(nums)

        duplicate = nums[0]
        missing = n

        i = 1
        while i < n:
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
                break

            i += 1
        
        j = 1
        while j <= n:
            if j not in sett:
                missing = j
                break
                
            j += 1
        
        return [duplicate, missing]
    
# Tests
solution = Solution()
# Testcase 1: [1,5,3,2,2,7,6,4,8,9]
nums = [1,5,3,2,2,7,6,4,8,9]
ans = solution.findErrorNums(nums)
print(ans == [2, 10])

# Testcase 2: [1,2,2,4]
nums = [1,2,2,4]
ans = solution.findErrorNums(nums)
print(ans == [2, 3])
