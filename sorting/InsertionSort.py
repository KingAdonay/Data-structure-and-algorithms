def printArr(arr):
    print(' '.join([str(x) for x in arr]))

def insertionSort1(n, arr):
    # Write your code here
    i = 0
    while i < n:
        j = i
        current = arr[i]
        
        while j > 0:
            if arr[j - 1] > current:
                arr[j] = arr[j-1]
            else:
                break
            printArr(arr)
            j = j - 1
            
        arr[j] = current
        i += 1
    printArr(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Tests

# Testcase1: 
# 
# n = 5
# arr = 2 4 6 8 3
# 
# 2 4 6 8 8 
# 2 4 6 6 8 
# 2 4 4 6 8 
# 2 3 4 6 8 