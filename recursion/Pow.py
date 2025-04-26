class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^-n = 1 / x^n, x^n = x ^ n/2 * x ^ n/2, (x * x) ^ n = x^n * x^n
        def helper(x: float, n: int):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = helper(x * x, n // 2)
        
            return x * res if n % 2 else res

        res = helper(x, abs(n))
    
        return 1 / res if n < 0 else res
    
# Tests
sol = Solution()

# Testcase 1:
x = 2.00000
n = 10
expected = 1024.00000
print(expected == sol.myPow(x, n))
# Testcase 2:
x = 2.00000
n = -2
expected = 0.25000
print(expected == sol.myPow(x, n))
# Testcase 3:
x = 2.00000
n = -200000000
expected = 0
print(expected == sol.myPow(x, n))