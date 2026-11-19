'''
408. Valid word abbreviation

Approach: go through the abbreviation string and check:
    - positional character equality
    - for digita check if the length of word created from abbreviation does not exceed the actual word length
    - digits ahould not start with 0
    
Time complexity: log(A), A being lemgth of abbr
Space complexity: log(1)
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        W = len(word)
        A = len(abbr)
        
        i = 0
        j = 0
        while i < A and j < W:
            abbr_count = ''
            while i < A and abbr[i].isdigit():
                abbr_count += abbr[i]
                i += 1
            
            if len(abbr_count) and abbr_count[0] == '0':
                return False
            
            if len(abbr_count):
                num = int(abbr_count)
                j += num
                if j > W:
                    return False
            
            else:
                if abbr[i] != word[j]:
                    return False
                
                i += 1
                j += 1
        
        return i == A and j == W
        
'''
Tests

"apple", "a2e" -> False
"internationalization", "i12iz4n" -> True
"internationalization", "i012iz4n" -> False
"internationalization", "i66iz4n" -> False
'''