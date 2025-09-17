class Solution:
    def fib(self, n: int) -> int:
        
        return self.helper_fun(n, {})
    
    def helper_fun(self, n: int, storage: dict) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n in storage:
            return storage[n]
        
        ans = self.helper_fun(n-1, storage) + self.helper_fun(n-2, storage)
        storage[n] = ans

        return ans

# Tests
sol = Solution()
# Testcase 1: 2
print(sol.fib(2) == 1)
# Testcase 2: 3
print(sol.fib(3) == 2)
# Testcase 3: 4
print(sol.fib(4) == 3)