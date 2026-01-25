from typing import List
'''
    724. Find Pivot Index
    
    Intuition:
    The problem is that we have to find the index where the sum of the numbers to the left of the index are equal to 
    the numbers to the right of the index.
    That means at each index we have to know the sum of numbers to the left and right of the index to compare and decide.
    
    Approach:
    Use sliding window to keep track of the sum of the left and right sides for each index.
    First find the sum of all values in the nums, which will be the right sum window, left window will be zero at start.
    For each index, shrink the right window by the number at i and check if the sum of the left side equals with the right sum.
    If not, extend the left window by the number at i.
    
    Time complexity: O(n), n being the length of nums
    Space complexity: O(1)
    
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i, num in enumerate(nums):
            right_sum -= num
            if right_sum == left_sum:
                return i
            left_sum += num
        
        return -1