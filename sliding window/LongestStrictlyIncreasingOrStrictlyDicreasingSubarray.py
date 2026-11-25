'''
3105. Longest structly increasing or strictly dicreasing subarray

Using dynamic sliding window approach

Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def helper(comparison_func):
            n = len(nums)
            left = 0
            max_len = 0
            for i in range(1, n):
                num = nums[i]
                if not comparison_func(nums[i - 1], num):
                    max_len = max(max_len, i - left)
                    left = i
            
            return max(max_len, n - left)
        
        return max(helper(lambda x, y : y > x), helper(lambda x, y : x > y))
            
            
'''
Testcases:
nums=[1,4,3,3,2] -> 2
nums=[3,3,3] -> 1
nums=[4,1,3,3,3] -> 2
'''