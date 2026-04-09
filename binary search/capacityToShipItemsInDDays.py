class Solution:
    def can_ship_on_time(self, weights: List[int], capacity:int, days: int) -> bool:
        c = capacity
        d = days
        for weight in weights:
            if weight > capacity:
                return False
            
            c -= weight
            if c < 0:
                c = capacity - weight
                d -= 1

        return d > 0 and c >= 0
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = sum(weights)

        while left < right:
            capacity = (left + right) // 2
            if self.can_ship_on_time(weights, capacity, days):
                
                right = capacity
            else:
                left = capacity + 1

        return right
        
'''
Testcases

[1,2,3,4,5,6,7,8,9,10]
5
[3,2,2,4,1,4]
3
[1,2,3,1,1]
4

'''