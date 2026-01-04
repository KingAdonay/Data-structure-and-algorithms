from typing import List

'''
    90. Subsets II
    
    To handle duplicates in the input set while generating all possible subsets using bit manipulation,
    we can first sort the input list. Sorting ensures that duplicate elements are adjacent.
    As we generate each subset using bit manipulation, we can use a set to keep track of the subsets we have already added to the result list.
    Before adding a new subset to the result list, we convert it to a tuple (which is hashable) and check if it is already in the set.
    If it is not in the set, we add it to both the result list and the set.
    This approach ensures that we only include unique subsets in the final result.
    
    Time complexity: O(n * 2^n), where n is the number of elements in the set. We generate 2^n subsets, and for each subset, we may need to iterate through n elements.
    Space complexity: O(n * 2^n) for storing all unique subsets in the result list and the set.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        nums.sort()
        
        added = set()
        for i in range(1 << n):
            temp = []
            for j in range(n):
                if i & (1 << j) :
                    temp.append(nums[j])
            key = tuple(temp)
            if key not in added:
                added.add(key)
                res.append(temp)
        return res

# Testcases:
sol = Solution()
print(sol.subsetsWithDup([1,2,2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])
print(sol.subsetsWithDup([0]) == [[], [0]])
print(sol.subsetsWithDup([4,4,4,1,4]) == [[], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4], [4, 4, 4, 4], [1, 4, 4, 4, 4]])