class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n >= -2 and n <= 2:
            return False
        
        return self.isPowerOfThree(n/3)
    
    def isPowerOfThreeOptimal(self, n: int) -> bool:
        
        return n > 0 and 3**19 % n == 0
        

# Tests
sol = Solution()
# Testcase 1:
n = 9
expected = True
print(expected == sol.isPowerOfThree(n))
print(expected == sol.isPowerOfThreeOptimal(n))
# Testcase 2:
n = 1
expected = True
print(expected == sol.isPowerOfThree(n))
print(expected == sol.isPowerOfThreeOptimal(n))
# Testcase 3:
n = -1
expected = False
print(expected == sol.isPowerOfThree(n))
print(expected == sol.isPowerOfThreeOptimal(n))
# Testcase 4:
n = 0
expected = False
print(expected == sol.isPowerOfThree(n))
print(expected == sol.isPowerOfThreeOptimal(n))
# Testcase 5:
n = 3 ** 19
expected = True
print(expected == sol.isPowerOfThree(n))
print(expected == sol.isPowerOfThreeOptimal(n))