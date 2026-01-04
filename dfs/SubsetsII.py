from typing import List

'''
    90. Subsets II
    
    To handle duplicates in the input set while generating all possible subsets using backtracking,
    we can first sort the input list. Sorting ensures that duplicate elements are adjacent.
    As we recursively build subsets, we can skip over duplicate elements to avoid generating the same subset multiple times.
    Specifically, when we encounter a duplicate element, we only include it in the current subset if it is the first occurrence at the current recursive level.
    This approach ensures that we only include unique subsets in the final result.
    
    Time complexity: O(n * 2^n), where n is the number of elements in the set. We generate 2^n subsets, and for each subset, we may need to iterate through n elements.
    Space complexity: O(n * 2^n) for storing all unique subsets in the result list.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        nums.sort()

        def helper(arr, i):
            res.append(arr)
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                helper(arr + [nums[j]], j + 1)
        
        helper([], 0)
        return res
    
# Testcases:
sol = Solution()
print(sol.subsetsWithDup([1,2,2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]])
print(sol.subsetsWithDup([0]) == [[], [0]])
print(sol.subsetsWithDup([4,4,4,1,4]) == [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])