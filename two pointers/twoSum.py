from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                break
            if summ < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]

# Tests
# Testcase 1: [2,7,11,15], 9
sol = Solution()
print(sol.twoSum([2,7,11,15], 9) == [1,2])
# Testcase 2: [2,3,4], 6
sol = Solution()
print(sol.twoSum([2,3,4], 6) == [1,3])