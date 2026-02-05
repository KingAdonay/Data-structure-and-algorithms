from typing import List

'''
    565. Array Nesting
    
    Intuition:
    We are asked to create a set from the array by visiting each value in the array,
    and using that value as an index on the next iteration and stopping only when that value is in the set,
    we can assume there is going to be a cycle.
    
    If there is a cycle that means the set for every element in set is going to have the same elemnts and same length.
    
    Approach:
    - Use dfs to traverse through every element until a cycle is detected, while keeping count of the number of elements visted
    - Mark the visited elements visited so that we dont have to check the cycle again, or mark the number in place as -1 to reduce the space complexity
    - Update max length on wvery iteration with the count returned from the dfs function for each index
    - Return max sum
    
    Complexity:
    - Time complexity: O(n), n being the length of nums
    - Space complexity: O(n), space used for the recursion stack
'''

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        def dfs(i, cnt):
            if nums[i] == -1:
                return cnt

            next, nums[i] = nums[i], -1

            return dfs(next, cnt + 1)

        for i in range(n):
            max_len = max(max_len, dfs(i, 0))

        return max_len

# Testcases:
sol = Solution()
print(sol.arrayNesting([5,4,0,3,1,6,2]) == 4)