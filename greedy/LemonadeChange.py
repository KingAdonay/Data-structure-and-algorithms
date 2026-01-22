from typing import List

'''
    860. Lemonade Change
    
    Use a greedy approach to give change using the largest bills first.
    Track the count of $5 and $10 bills to make change.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        net_pay = 5
        bill_count = { 5: 0, 10: 0, 20: 0}

        net_total = 0
        for bill in bills:
            change = bill - net_pay
            while change > 0 and net_total > 0:
                if change >= 10 and bill_count[10]:
                    change -= 10
                    bill_count[10] -= 1
                    net_total -= 10
                elif bill_count[5]:
                    change -= 5
                    bill_count[5] -= 1
                    net_total -= 5
                else:
                    break
            
            if change:
                return False
            
            net_total += bill
            bill_count[bill] += 1
        
        return True
    
# Testcases:
sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]) == True)
print(sol.lemonadeChange([5,5,10]) == True)
print(sol.lemonadeChange([10,10]) == False)
print(sol.lemonadeChange([5,5,10,10,20]) == False)