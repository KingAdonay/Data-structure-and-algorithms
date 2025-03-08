class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        count = 0

        i = 0
        if k == n:
            return "0"

        while i < n:
            while stack and stack[-1] > int(num[i]) and count < k:
                stack.pop()

                count += 1
            if count == k:
                break
            if not stack and num[i] == "0":
                i += 1
                continue
            stack.append(int(num[i]))
            i += 1
        
        while count < k:
            if stack:
                stack.pop()
            count += 1
        st = ""
        if stack:
            st="".join([str(ele) for ele in stack])
        
        right_st=num[i:]
        ans = (st + right_st).lstrip("0")

        if ans:
            return ans
        
        return "0"
    

# Tests
sol = Solution()
# Testcase 1: "1432219", k = 3
print("1219" == sol.removeKdigits("1432219", 3))
# Testcase 2: "10200", k = 1
print("200" == sol.removeKdigits("10200", 1))
# Testcase 3: "10", k = 2
print("0" == sol.removeKdigits("10", 2))
# Testcase 4: "10", k = 2
print("0" == sol.removeKdigits("100001", 2))