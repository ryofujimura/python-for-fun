'''
As you can see, we've prepared the text variable in the Code Editor. This variable contains quite a long string of characters. Your task is to iterate over the characters of the string, count the number of uppercase letters and lowercase letters, and print the result:
'''

text = "ABgvddVICJSdkeprsmgn UTPDvndhtuwPOTNRSjfisuRNSUesajdsa"
LOWERCASE = 0
UPPERCASE = 0

for i in text:
    if i.islower():
        LOWERCASE += 1
    elif i.isupper():
        UPPERCASE += 1
    else:
        pass

print("Uppercase: ", UPPERCASE)
print("Lowercase: ", LOWERCASE)
