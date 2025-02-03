def type_word(keyboard, word):
    dic = {}
    n = len(word)
    
    if n < 1:
        return 0
    
    for i, key in enumerate(keyboard):
        dic[key] = i + 1
    
    time = 0
    prev_char = word[0]
    for i in range(1, n):
        time += abs(dic[word[i]] - dic[prev_char])
        prev_char = word[i]
        
    return time
 
if __name__ == '__main__':
    num_of_cases = int(input())
    keyboards = []
    words = []
    
    i = 0
    while i < num_of_cases:
        keyboard = input()
        word = input()
        
        keyboards.append(keyboard)
        words.append(word)
        i += 1
    
    i = 0
    while i < num_of_cases:
        time_taken = type_word(keyboards[i], words[i])
        print(time_taken)
        i += 1


# Inputs and results for test

# 5
# abcdefghijklmnopqrstuvwxyz
# hello
# abcdefghijklmnopqrstuvwxyz
# i
# abcdefghijklmnopqrstuvwxyz
# codeforces
# qwertyuiopasdfghjklzxcvbnm
# qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
# qwertyuiopasdfghjklzxcvbnm
# abacaba
# 13
# 0
# 68
# 0
# 74