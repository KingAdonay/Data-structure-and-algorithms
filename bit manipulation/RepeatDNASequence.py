from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        res = []
        sub_s = s[:10]
        dic = defaultdict(int)
        dic[sub_s] += 1
        for i in range(10, n):
            sub_s = s[i - 9:i + 1]
            dic[sub_s] += 1

        for key, value in dic.items():
            if value > 1:
                res.append(key)

        return res