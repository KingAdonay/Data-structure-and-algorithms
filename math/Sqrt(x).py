'''
 69. Sqrt(x)

 Implement sqrt(x) method without using pow method or ** operator.

 Time complexity: O(log n)
 Space complexity: O(1)
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        
        left, right = 2, x // 2
        
        while left <= right:
            num = left + (right - left) // 2
            
            res = num * num
            
            if res == x:
                return num
            elif res < x:
                left = num + 1
            else:
                right = num - 1
            
        return right

