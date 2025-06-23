# EXERCISE ONE

text='banana'
# print(text.count('a'))

# EXERCISE TWO
def is_palindrome(word):
    if word == word[::-1]:
        return 'this is a palindrome'
#print(is_palindrome('racecar'))
#print(is_palindrome('banana'))

#EXERCISE THREE
def rotate_word(word,n):
    for letter in word:
        number=ord(letter)+n
        print(chr(number),end='')

#rotate_word('cheer',7)
#rotate_word('melon',-10)
rotate_word('cheer',7)

    
