import string

phrase = input()

for char in string.punctuation:
    phrase = phrase.replace(char, '')
print(phrase.lower())
