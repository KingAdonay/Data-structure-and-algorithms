# The function accepts INTEGER_ARRAY a as parameter.

def countSwaps(a):
    # Write your code here
    count = 0
    length = len(a)
    for i in range(length):
        for j in range(length - i - 1 ):
            if a[j] > a[j + 1]:
                # swap
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                count += 1
    
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[length - 1]}")

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split())) # Example input: 1 2 3 

    countSwaps(a)

# Tests

# Testcase 1: 5 4 7 2 1 
# expected: 
# Array is sorted in 8 swaps.
# First Element: 1
# Last Element: 7

# Testcase 2: 3 2 1 
# expected: 
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
