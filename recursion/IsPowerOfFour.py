import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n < 1:
            return False
        
        return self.isPowerOfFour(n / 4)
    
    def isPowerOfFourOptimal(self, n: int) -> bool:
        
        return n > 0 and math.log(n, 4) % 1 == 0

# Tests
sol = Solution()
# Testcase 1:
n = 16
expected = True
print(expected == sol.isPowerOfFour(n))
print(expected == sol.isPowerOfFourOptimal(n))
# Testcase 2:
n = 5
expected = False
print(expected == sol.isPowerOfFour(n))
print(expected == sol.isPowerOfFourOptimal(n))
# Testcase 3:
n = 64
expected = True
print(expected == sol.isPowerOfFour(n))
print(expected == sol.isPowerOfFourOptimal(n))
# Testcase 4:
n = 1
expected = True
print(expected == sol.isPowerOfFour(n))
print(expected == sol.isPowerOfFourOptimal(n))
# Testcase 5:
n = 8
expected = False
print(expected == sol.isPowerOfFour(n))
print(expected == sol.isPowerOfFourOptimal(n))
# Testcase 6:
n = 4 ** 15
expected = True
print(expected == sol.isPowerOfFour(n))
print(expected == sol.isPowerOfFourOptimal(n))