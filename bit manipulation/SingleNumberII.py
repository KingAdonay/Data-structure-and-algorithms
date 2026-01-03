from typing import List

'''
    137. Single Number II
    
    One approach to solve the problem is to use a counter dictionary to keep track of the occurrences of each number in the array,
    and then return the number that occured only once. However, this approach uses extra space.
    A more efficient approach is to use bit manipulation to achieve the same result with constant space complexity.
    The idea is to use two variables, ones and twos, to keep track of the bits that have appeared once and twice respectively.
    For each number in the array, we update ones and twos using bitwise operations.
    The expression ones = (ones ^ num) & ~twos updates ones to include bits that have appeared once, while removing bits that have appeared twice.
    Similarly, the expression twos = (twos ^ num) & ~ones updates twos to include bits that have appeared twice, while removing bits that have appeared once.
    After processing all numbers in the array, ones will contain the bits of the number that appeared only once.
    
    Time complexity: O(n), where n is the number of elements in the array. We iterate through the array once.
    Space complexity: O(1), using a constant amount of space.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        
        return ones

# Testcases:
sol = Solution()
print(sol.singleNumber([2,2,3,2]) == 3)
print(sol.singleNumber([0,1,0,1,0,1,99]) == 99)
print(sol.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]) == -4)