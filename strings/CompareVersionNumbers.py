'''
    165. Compare Version Numbers
    
    Split the version numbers by the dot character and compare each corresponding segment as integers.
    If one version has fewer segments, treat the missing segments as zeros.
    
    Time Complexity: O(m + n), where m and n are the lengths of version1 and version2 respectively.
    Space Complexity: O(1), as we are using only constant extra space.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            n1 = int(v1[i])
            n2 = int(v2[j])

            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
            
            i += 1
            j += 1
        
        while i < len(v1):
            n1 = int(v1[i])
            if n1 > 0:
                return 1
            i += 1
        
        while j < len(v2):
            n2 = int(v2[j])
            if n2 > 0:
                return -1
            j += 1
        
        return 0

# Testcases:
sol = Solution()
print(sol.compareVersion("1.01", "1.001") == 0)
print(sol.compareVersion("1.0", "1.0.0") == 0)
print(sol.compareVersion("0.1", "1.1") == -1)
print(sol.compareVersion("1.0.1", "1") == 1)