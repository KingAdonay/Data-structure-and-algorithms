from typing import List

'''
    287. Find the Duplicate Number
    
    This problem can be solved using bit manipulation by leveraging a bitset to track the numbers we have seen so far.
    As we iterate through the list of numbers, we create a mask for each number by left-shifting 1 by the value of the number.
    We then check if this mask is already set in our bitset. If it is, that means we have encountered this number before, and thus it is the duplicate.
    If not, we set the corresponding bit in our bitset to indicate that we have seen this number.
    
    Example: [1, 3, 4, 2, 2]
    Dry Run:
    num = 1 -> mask = 1 << 1 = 2 (10 in binary), bit_set = 0 | 2 = 2
    num = 3 -> mask = 1 << 3 = 8 (1000 in binary), bit_set = 2 | 8 = 10
    num = 4 -> mask = 1 << 4 = 16 (10000 in binary), bit_set = 10 | 16 = 26
    num = 2 -> mask = 1 << 2 = 4 (100 in binary), bit_set = 26 | 4 = 30
    num = 2 -> mask = 1 << 2 = 4 (100 in binary), bit_set & mask = 30 & 4 != 0 -> duplicate found: 2
    
    Time complexity: O(n), where n is the number of elements in the list. We make a single pass through the list.
    Space complexity: O(1) if we consider the bitset as a fixed size integer. However, this approach may not work for very large numbers due to integer size limitations.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bit_set = 0
        mask = 0
        for num in nums:
            mask = 1 << num

            if bit_set & mask:
                return num

            bit_set |= mask

        return 0
        
# Testcases:
sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]) == 2)
print(sol.findDuplicate([3,1,3,4,2]) == 3)