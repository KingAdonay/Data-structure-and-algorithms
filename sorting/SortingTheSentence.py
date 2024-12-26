class Solution:
    def getOrderNum(self, strValue):
        charArr = list(strValue)
        order = charArr[len(charArr) - 1]
        return order

    def sortSentence(self, s: str) -> str:
        arr = s.split()
        
        for i, value in enumerate(arr):
            smallestOrderIdx = i
            smallestOrder = self.getOrderNum(value)

            for j in range(i, len(arr)):
                currentOrder = self.getOrderNum(arr[j])
                if (currentOrder < smallestOrder):
                    smallestOrder = currentOrder
                    smallestOrderIdx = j
            temp = arr[i]
            arr[i] = arr[smallestOrderIdx]
            arr[smallestOrderIdx] = temp
           
        strArr = ' '.join([ val.replace(val[len(val) - 1], '') for val in arr])
        
        return strArr
    
# Tests
# Testcase 1: "is2 sentence4 This1 a3"
# expected = "This is a sentence"

solution = Solution()
result = solution.sortSentence("is2 sentence4 This1 a3")
print(result == "This is a sentence")
