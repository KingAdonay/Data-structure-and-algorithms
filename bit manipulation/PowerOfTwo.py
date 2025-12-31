'''
    231. Power of Two
    
    Use bit manipulation to determine if a number is a power of two.
    A number n is a power of two if it is greater than zero and there is only one bit set in its binary representation.
    This can be checked using the expression n & (n - 1). If n is a power of two, this expression will be zero.
    
    N - 1 flips all the bits after the rightmost set bit of N including the rightmost set bit.
    Therefore, performing a bitwise AND between N and N - 1 will result in zero if there is only one set bit in N.
    
    Time complexity: O(1), since the operation involves a constant number of bit manipulations.
    Space complexity: O(1), using a constant amount of space.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1)) == 0

# Testcases:
sol = Solution()
print(sol.isPowerOfTwo(1) == True)
print(sol.isPowerOfTwo(16) == True)
print(sol.isPowerOfTwo(3) == False)
print(sol.isPowerOfTwo(0) == False)
print(sol.isPowerOfTwo(-2) == False)