class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        cache = {}
        def helper(ans: str, a_count: int, b_count: int, conc_a: int, conc_b: int) -> str:
            n = len(ans)
            key = (ans, a_count, b_count)

            if a_count > a or b_count > b:
                return ''
            
            if conc_a == 3 or conc_b == 3:
                return ''
            
            if n == (a + b):
                return ans
            
            if key in cache:
                return cache[key]
            
            res1 = helper(ans + 'a', a_count + 1, b_count, conc_a + 1, 0)
            res2 = helper(ans + 'b', a_count, b_count + 1, 0, conc_b + 1)

            cache[key] = res1 if res1 else res2

            return cache[key]
        
        return helper('', 0, 0, 0, 0)
            

            
# Testcases
solution = Solution()
print(solution.strWithout3a3b(1, 2))  # "bab"
print(solution.strWithout3a3b(4, 1))  # "aabaa
print(solution.strWithout3a3b(2, 4))  # "bbabb"
print(solution.strWithout3a3b(0, 0))  # ""
print(solution.strWithout3a3b(3, 3))  # "ababab"
print(solution.strWithout3a3b(27, 33)) # Memory Limit Exceeded for bigger number inputs like 27, 33.
