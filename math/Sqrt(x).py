'''
 69. Sqrt(x)

 Implement sqrt(x) method without using pow method or ** operator.

 Time complexity: O(logn)
 Space complexity: O(1)
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        num = x >> 1
        while num > 0:
            n = num * num
            if n == x:
                return num
            
            if n < x:
                while (num + 1) * (num + 1) <= x:
                    num += 1
                
                return num
            
            
            num = num >> 1
            
        return num

