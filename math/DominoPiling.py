import math

def max_number_of_dominos():
    inputString = input()
    num_array = inputString.split(' ')

    m = int(num_array[0])
    n = int(num_array[1])

    num_of_dominos = math.floor((m*n)/2)
    print(num_of_dominos)


# Test
max_number_of_dominos()

# Testcases 1: 2 4 -> 4
# Testcases 2: 3 3 -> 4
# Testcases 3: 1 3 -> 1