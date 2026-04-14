class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m*n
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in range(1, m + 1):
                count += n if n < mid // i else mid // i
            
            if count >= k:
                right = mid
            else :
                left = mid + 1
        
        return left
    
# Testcases
# Testcase 1: m = 3, n = 3, k = 5 -> 3
# Testcase 2: m = 2, n = 3, k = 6 -> 6
# Testcase 3: m = 3, n = 3, k = 8 -> 6