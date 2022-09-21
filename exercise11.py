'''Create a function find_short_long_word(words_list). The function should return the tuple of the shortest word in the list and the longest word in the list (in that order). If there are multiple words with minimum length, you should return the first shortest word in the list. And if there are multiple words with maximum length in the list, you should return the last longest word in the list.
'''

def find_short_long_word(words_list):
    short = words_list[0]
    long = words_list[0]
    for word in words_list:
        if len(word) < len(short):
            short = word
        if len(word) >= len(long):
            long = word
    return (short, long)

print(find_short_long_word(['hello', 'hi', 'hey', 'hola', 'bonjour', 'namaste', 'aloha', 'ciao', 'howdy']))