from typing import List

'''
    17. Letter Combinations of a Phone Number
    
    Create a mapping of digit to letters as on a phone keypad.
    Use backtracking to generate all possible combinations of letters for the given digits.
    Start with an empty prefix and for each digit, append each corresponding letter to the prefix and
    recursively call the function for the next digit.
    When the prefix length matches the length of the input digits, add it to the result list.
    
    Time Complexity: O(n * 4^m), where n is the number of digits and 4 is the maximum number of letters for a digit (like '7' and '9').
    Space Complexity: O(n), where n is the length of the input digits (for the recursion stack).
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        
        if not digits:
            return res

        def backtrack(i: int, prefix: str):
            if len(prefix) == len(digits):
                res.append(prefix)
                return
            
            for c in keypad[digits[i]]:
                backtrack(i + 1, prefix + c)
        
        backtrack(0, '')

        return res
    
# Testcases:
sol = Solution()
print(sol.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
print(sol.letterCombinations("") == [])
print(sol.letterCombinations("2") == ["a", "b", "c"])   