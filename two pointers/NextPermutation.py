'''
    31. Next Permutation
    
    Approach: Two Pointers
    - The idea is to find the first number from the back that breaks the monotonically increasing pattern. 
    This number is called the pivot. Then, we find the first number from the back that is greater than the 
    pivot and swap them. Finally, we reverse the numbers after the pivot to get the next permutation.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
'''
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        pivot = n - 1

        while pivot > 0 and nums[pivot] <= nums[pivot - 1]:
            pivot -= 1
        
        if pivot > 0:
            swapping_idx = n - 1
            # pivot - 1 is the first number breaking the monotonically increasing pattern from the back
            while swapping_idx > 0 and nums[swapping_idx] <= nums[pivot - 1]:
                swapping_idx -= 1
            
            # swap
            nums[pivot - 1], nums[swapping_idx] = nums[swapping_idx], nums[pivot - 1]
        
        # To minimise the num size, reverse the nums from the pivot
        left = pivot
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

            
# Test case
solution = Solution()
nums = [1, 2, 3]
solution.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
