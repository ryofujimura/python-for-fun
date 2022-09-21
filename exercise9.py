'''
Write a function called find_censored_words() that accepts a list of strings and a list of special characters as its arguments, and prints all censored words from it one by one in separate lines.

A word is considered to be censored if it has at least one character from the special_chars list. You can use the word_list variable to test your function.

'''
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
word_list = ['se#$et', 'Ver*%&$lo', 'di$#^$nt', 'c*%e', 'is', '#%$#@!@#$%^$#']

def find_censored_words(word_list, special_chars):
    for word in word_list:
        for char in word:
            if char in special_chars:
                print(word)
                break

find_censored_words(word_list, special_chars)

print("--------------")
'''That was a good one! As you can see, we've left the find_censored_words() implementation in the Code Editor. Assuming that the function arguments don't change, modify the function and make it return a new list with words that do not have any of the special characters.

Also, rename the function to be called return_non_censored_words(). Again, you can use the word_list variable to test your function.
'''
word_list = ['Well', 'w#@l', 'n$#@r', 'done', 'g$%e', 'u%', 'keep', 'it', 'up']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']

def return_non_censored_words(word_list, special_chars):
    new_list = []
    for word in word_list:
        for char in word:
            if char in special_chars:
                break
        else:
            new_list.append(word)
    for i in new_list:
        print(i)

print(return_non_censored_words(word_list, special_chars))
