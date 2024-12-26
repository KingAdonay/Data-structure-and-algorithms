class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            smallestValueIdx = i
            for j in range(i, len(arr)):
                if(arr[j] < arr[smallestValueIdx]):
                    smallestValueIdx = j
                
            temp = arr[i]
            arr[i] = arr[smallestValueIdx]
            arr[smallestValueIdx] = temp
    
    def checkValues(self, actualValue, expectedValue):
        for i, value in enumerate(actualValue):
            if (expectedValue[i] != value):
                print("Test failed.")
                return
        print("Test passed.")


# Tests

# Testcase 1: [4, 1, 3, 9, 7]
# expected: [1, 3, 4, 7, 9]
solution = Solution()

arr = [4, 1, 3, 9, 7]
solution.selectionSort(arr)
expectedValue = [1, 3, 4, 7, 9]
solution.checkValues(arr, expectedValue)

