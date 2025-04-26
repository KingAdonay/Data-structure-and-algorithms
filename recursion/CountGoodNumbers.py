class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
    
    def myPow(self, x: int, exp: int) -> int:
        if x == 0:
            return 0
        
        res, num, expo = 1, x, exp
        
        while expo > 0:
            if expo % 2:
                res = (res * x)
            
            x = (x ** 2) % self.MOD
            expo = expo // 2

        return res
    
    def countGoodNumbers(self, n: int) -> int:
        
        num = n // 2
        
        even_count = self.myPow(5, num + 1 if n % 2 else num)
        prime_count = self.myPow(4, num)

        return (even_count * prime_count) % self.MOD


# Tests
sol = Solution()
# Testcase 1:
n = 1
expected = 5
print(expected == sol.countGoodNumbers(n))
# Testcase 2:
n = 4
expected = 400
print(expected == sol.countGoodNumbers(n))
# Testcase 2:
n = 806166225460393
expected = 643535977
print(expected == sol.countGoodNumbers(n))