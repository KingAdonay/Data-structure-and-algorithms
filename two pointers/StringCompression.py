from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","a","b","b","c","c","c"]
        n = len(chars)
        i = 0
        curr_char = chars[0]
        count = 0
        for c in chars:
            if curr_char == c:
                count += 1
            else:
                chars[i] = curr_char
                i += 1
                if count > 1:
                    count_str = str(count)
                    for s in count_str:
                        chars[i] = s
                        i+=1
                curr_char = c
                count = 1
        if curr_char:
            chars[i] = curr_char
            i += 1
            if count > 1:
                count_str = str(count)
                for s in count_str:
                    chars[i] = s
                    i+=1
        return i

# Tests
sol = Solution()
# Testcase 1: ["a","a","b","b","c","c","c"] => ["a","2","b","2","c","3"]
# Testcase 2: ["a","b","b","b","b","b","b","b","b","b","b","b","b"] => ["a","b","1","2"]