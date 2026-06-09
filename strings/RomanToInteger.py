'''
    13. Roman to Integer
    
    Create a symbols dictionary that maps each Roman numeral (including the special cases) to its corresponding decimal value.
    Create a double_char array that contains the special cases of Roman numerals that consist of two characters (e.g., "CM", "CD", "XC", "XL", "IX", "IV").
    Initialize a variable num to store the resulting integer value.
    Iterate through the input string s from right to left:
        For each character, check if it forms a double character with the previous character (i.e., if the current character and the previous character together are in the double_char array).
        If it forms a double character, add the corresponding decimal value from the symbols dictionary to num and skip the previous character in the next iteration.
        If it does not form a double character, add the corresponding decimal value from the symbols dictionary to num.
    Return the resulting num.
    
    Time complexity: O(n), where n is the length of the input string s.
    Space complexity: O(1), since the symbols dictionary and double_char array have a constant size.
'''

class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        double_char = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']

        i = len(s) - 1
        num = 0
        while i >= 0:
            is_double = False
            if i > 0:
                is_double = s[i-1] + s[i] in double_char
            
            roman = s[i - 1] + s[i] if is_double else s[i]
            num += symbols[roman]

            if is_double:
                i -= 2
            else:
                i -= 1
        
        return num
    

# Testcases
sol = Solution()
# Testcase 1: s = "III" -> 3
print(sol.romanToInt("III") == 3) # 3
# Testcase 2: s = "IV" -> 4
print(sol.romanToInt("IV") == 4) # 4
# Testcase 3: s = "IX" -> 9
print(sol.romanToInt("IX") == 9) # 9
# Testcase 4: s = "LVIII" -> 58
print(sol.romanToInt("LVIII") == 58) # 58
# Testcase 5: s = "MCMXCIV" -> 1994
print(sol.romanToInt("MCMXCIV") == 1994) # 1994
# Testcase 6: s = "MMMDCCXLIX" -> 3749
print(sol.romanToInt("MMMDCCXLIX") == 3749) # 3749