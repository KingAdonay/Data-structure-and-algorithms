from typing import List

'''
    78. Subsets
    
    Use backtracking to generate all possible subsets of a set.
    The approach involves recursively building subsets by including or excluding each element.
    Starting with an empty subset, we iterate through the elements of the set.
    For each element, we have two choices: either include it in the current subset or skip it.
    We use a helper function to manage the recursion, appending the current subset to the result list at each step.
    The recursion continues until we have considered all elements in the set.
    
    Time complexity: O(2^n)
    Space complexity: O(n)
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(arr, i):
            res.append(arr)

            for j in range(i, n):
                helper(arr + [nums[j]], j + 1)
        
        helper([], 0)
        return res

# Testcases:
sol = Solution()
print(sol.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
print(sol.subsets([0]) == [[], [0]])