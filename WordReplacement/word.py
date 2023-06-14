#introduces us to replace method in python
#the program is case sensitive to the words entered to be replaced

def replace_word():
    str = "Hello guys, I am Emmanuel. Nice to meet you all."
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()