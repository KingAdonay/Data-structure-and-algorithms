'''
    12. Integer to Roman

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Create a symbols array that contains the decimal value and the corresponding Roman numeral for each symbol.
    Create a can_repeat array that contains the symbols that can be repeated up to three times (I, X, C, M).
    Initialize an empty string roman to store the resulting Roman numeral.
    Iterate through the symbols array:
        For each symbol, calculate how many times it can be repeated by dividing num by the decimal value of the symbol.
        If the symbol can be repeated (i.e., it is in the can_repeat array), limit the repeat count to a maximum of 3.
        If the symbol cannot be repeated, limit the repeat count to a maximum of 1.
        Append the corresponding Roman numeral to the roman string based on the repeat count.
        Subtract the total value of the repeated symbols from num.
    Return the resulting roman string.
    
    Time complexity: O(1), since the number of symbols is constant.
    Space complexity: O(1), since the number of symbols is constant.
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        can_repeat = ['I', 'X', 'C', 'M']

        i = 0
        roman = ''
        
        while i < len(symbols):
            decimal, char = symbols[i]

            repeat = min(3, num // decimal)
            if char not in can_repeat:
                repeat = min(1, num // decimal)
            
            roman += char * repeat
            num -= decimal * repeat

            i += 1
                
        return roman

# Testcases
sol = Solution()

# Testcase 1: num = 3 -> "III"
print(sol.intToRoman(3) == "III") # "III"
# Testcase 2: num = 4 -> "IV"
print(sol.intToRoman(4) == "IV") # "IV"
# Testcase 3: num = 9 -> "IX"
print(sol.intToRoman(9) == "IX") # "IX"
# Testcase 4: num = 58 -> "LVIII"
print(sol.intToRoman(58) == "LVIII") # "LVIII"
# Testcase 5: num = 1994 -> "MCMXCIV"
print(sol.intToRoman(1994) == "MCMXCIV") # "MCMXCIV"
# Testcase 6: num = 3749 -> "MMMDCCXLIX"
print(sol.intToRoman(3749) == "MMMDCCXLIX") # "MMMDCCXLIX"