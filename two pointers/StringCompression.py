from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","a","b","b","c","c","c"]
        n = len(chars)
        write = 0
        read = 0
        while read < n:
            curr_char = chars[read]
            count = 0

            while read < n and curr_char == chars[read]:
                count += 1
                read += 1
            
            
            chars[write] = curr_char
            write += 1
            if count > 1:
                count_str = str(count)
                for s in count_str:
                    chars[write] = s
                    write += 1

        return write


# Tests
sol = Solution()
# Testcase 1: ["a","a","b","b","c","c","c"] => ["a","2","b","2","c","3"]
chars = ["a","a","b","b","c","c","c"]
count = sol.compress(chars)
print(chars[:count] == ["a","2","b","2","c","3"])
# Testcase 2: ["a","b","b","b","b","b","b","b","b","b","b","b","b"] => ["a","b","1","2"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
count = sol.compress(chars)
print(chars[:count] == ["a","b","1","2"])