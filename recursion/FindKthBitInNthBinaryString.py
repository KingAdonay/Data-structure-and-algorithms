class Solution:
    def invert(self, s: str) -> str:
        dic = {'0': '1', '1': '0'}
        inverted_s = ''

        for c in s:
            inverted_s += dic[c]
        
        return inverted_s
    
    def reverse(self, s: str) -> str:
        return s[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return '0'
            
            s_prev = helper(n - 1)
            
            return s_prev + '1' + self.reverse(self.invert(s_prev))
        
        s = helper(n)

        return s[k - 1]
    
# Tests
sol = Solution()
# Testcase 1:
n = 20
k = 1048575
expected = '1'
print(expected == sol.findKthBit(n, k))
# Testcase 2:
n = 4
k = 11
expected = '1'
print(expected == sol.findKthBit(n, k))
# Testcase 3:
n = 3
k = 1
expected = '0'
print(expected == sol.findKthBit(n, k))