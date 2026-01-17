'''
    984. String Without AAA or BBB
    
    Use a greedy approach to construct an array with no three consecutive 'a's or 'b's.
    First, determine which character is more frequent.
    Then, create pairs of the more frequent character and distribute the less frequent character among them.
    
    Time complexity: O(a + b) where a is the count of 'a's and b is the count of 'b's
    Space complexity: O(a + b)
'''

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        A, B = 'a', 'b'

        base_char, separator_char, base_count, separator_count = (A, B, a, b) if a > b else (B, A, b, a)

        ans = []
        doubles = base_count // 2
        remainder = base_count % 2

        for _ in range(doubles):
            ans.append(base_char * 2)
        
        if remainder:
            ans.append(base_char)
        
        i = 0
        while separator_count > 0:
            ans[i] += separator_char
            i = (i + 1) % len(ans)
            separator_count -= 1
        
        return ''.join(ans)

# Testcases
solution = Solution()
print(solution.strWithout3a3b(1, 2))  # "bab"
print(solution.strWithout3a3b(4, 1))  # "aabaa"
print(solution.strWithout3a3b(2, 4))  # "bbabb"
print(solution.strWithout3a3b(0, 0))  # ""
print(solution.strWithout3a3b(4, 6))  # "bbaabbabba"
print(solution.strWithout3a3b(27, 33)) # "bbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbabbabbabbabbabbaba"