from typing import List

'''
    33. Search in Rotated Sorted Array

    Using a two step approach, we can first find the index of the smallest element in the array, which is the point of rotation. 
    Then, we can perform a binary search on the appropriate half of the array based on the target value.
    
    Time Complexity: O(log n) for finding the rotation point and O(log n) for the binary search, resulting in O(log n) overall.
    Space Complexity: O(1) since we are using only a constant amount of extra space.
'''

class Solution:
    def find_target_idx(self, nums: List[int], target: int, start:int, end:int) -> int:
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        rotated_end_idx = left

        ans1 = self.find_target_idx(nums, target, 0, rotated_end_idx)
        if ans1 != -1:
            return ans1
        
        return self.find_target_idx(nums, target, rotated_end_idx + 1, len(nums) - 1)

# Testcases
# Testcase 1: nums = [4,5,6,7,0,1,2], target = 0 -> 4
# Testcase 2: nums = [4,5,6,7,0,1,2], target = 3 -> -1
# Testcase 3: nums = [1], target = 0 -> -1