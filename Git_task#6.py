# Problem: Write a Python program that counts the frequency of each word in a given string.
#  The program should ignore case and punctuation.

text = "Hello world! Hello everyone. Welcome to the world of Python."
text = text.replace("!","").replace(".","").lower().split()

for i in text:
    print(f"'{i}': {text.count(i)},",end=" ")








