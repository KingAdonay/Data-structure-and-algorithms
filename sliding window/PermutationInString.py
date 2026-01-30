'''
    567. Permutation in String
    
    Intuition:
    To determine if one string's permutation is a substring of another, we can use a sliding window approach
    combined with frequency counting. We maintain frequency counts of characters in the first string and compare
    them with the frequency counts of characters in the current window of the second string.
    If at any point the frequency counts match, it indicates that a permutation of the first string exists as a
    substring in the second string.
    
    Approach:
    1. Create frequency arrays for both strings.
    2. Initialize the frequency array for the first window of the second string.
    3. Slide the window across the second string, updating the frequency array and checking for matches.
    4. If a match is found, return True; otherwise, return False after checking all windows.
    
    Time complexity: O(M + N), where M and N are the lengths of s1 and s2 respectively.
    Space complexity: O(1), since the frequency arrays have a fixed size of 26 (for lowercase English letters).
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        n, m = len(s1), len(s2)

        if m < n:
            return False
        
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        for i in range(n):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s2_freq == s1_freq:
            return True
            
        for i in range(n, m):
            s2_freq[ord(s2[i - n]) - ord('a')] -= 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

            if s1_freq == s2_freq:
                return True
        
        return False