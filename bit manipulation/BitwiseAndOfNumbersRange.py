'''
    201. Bitwise AND of Numbers Range
    
    Use bit manipulation to find the bitwise AND of all numbers in the inclusive range [left, right].
    The key observation is that the bits that differ between left and right will eventually become zero in the AND operation.
    Therefore, we can right-shift both left and right until they are equal, counting the number of shifts.
    Once they are equal, we left-shift the result back by the number of shifts to restore the common bits.
    
    Time complexity: O(log n), where n is the difference between left and right. In the worst case, we may need to shift log n times.
    Space complexity: O(1), using a constant amount of space.
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        
        return left << count
    
# Testcases:
sol = Solution()
print(sol.rangeBitwiseAnd(5, 7) == 4)
print(sol.rangeBitwiseAnd(0, 1) == 0)
print(sol.rangeBitwiseAnd(1, 2147483647) == 0)