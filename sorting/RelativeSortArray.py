from collections import defaultdict
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        count_dic = defaultdict(int)
        other_values = []
        res = []

        for num in arr1:
            if num not in arr2_set:
                other_values.append(num)
            count_dic[num] += 1
        
        other_values.sort()

        for num in arr2:
            for i in range(count_dic[num]):
                res.append(num)
           
        return res + other_values
            
# Tests
solution = Solution()
# Testcase 1: 
num1 = [26,21,11,20,50,34,1,18]
num2 = [21,11,26,20]
expected = [21,11,26,20,1,18,34,50]

actual = solution.relativeSortArray(num1, num2)
print(actual == expected)