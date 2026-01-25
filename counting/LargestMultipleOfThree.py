from typing import List

'''
    1363. Largest Multiple of Three

    This problem can be solved by counting the occurrences of each digit and then removing the minimum number of digits to make the sum divisible by 3.
    If the sum of digits modulo 3 is 1, we remove one digit from [1, 4, 7] or two digits from [2, 5, 8].
    If the sum of digits modulo 3 is 2, we remove one digit from [2, 5, 8] or two digits from [1, 4, 7].
    After removing the required digits, we construct the largest possible number by placing digits in descending order.
    
    Example: [8, 1, 9]
    Dry Run:
    counts = [0,1,0,0,0,0,0,0,1,1]
    summ = 18, remainder = 0
    st = '9' * 1 + '8' * 1 + '1' * 1 = '981'
    
    Time complexity: O(n), where n is the number of digits. We make a single pass to count digits and another pass to construct the result.
    Space complexity: O(1), since the counts array has a fixed size of 10.
'''
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        n = len(digits)
        counts = [0] * 10
        summ = 0
        for digit in digits:
            counts[digit] += 1
            summ += digit

        remainder = summ % 3

        if remainder == 1:
            removed = False
            for i in [1, 4, 7]:
                if counts[i] > 0:
                    counts[i] -= 1
                    removed = True
                    break
            if not removed:
                remove_count = 0
                for i in [2, 5, 8]:
                    while counts[i] > 0 and remove_count < 2:
                        counts[i] -= 1
                        remove_count += 1
        elif remainder == 2:
            removed = False
            for i in [2, 5, 8]:
                if counts[i] > 0:
                    counts[i] -= 1
                    removed = True
                    break
            if not removed:
                remove_count = 0
                for i in [1, 4, 7]:
                    while counts[i] > 0 and remove_count < 2:
                        counts[i] -= 1
                        remove_count += 1
        
        st = ''
        for i in range(9, -1, -1):
            if counts[i] > 0:
                st += str(i) * counts[i]
        
        if st and st[0] == '0':
            return '0'
        
        return st