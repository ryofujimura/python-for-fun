'''
Create a function named mind_your_tone() that accepts a string as its argument and checks whether the whole string is uppercase. If it is, then the function should return the string in lowercase. Otherwise, it should return the original text.
'''

def mind_your_tone(text):
    if text.isupper():
        return text.lower()
    else:
        return text

print(mind_your_tone("HELLO"))