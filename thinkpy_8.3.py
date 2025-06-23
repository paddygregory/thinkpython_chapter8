fruit = 'banana'

def index(fruit):
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(letter)
        index = index + 1

# index(fruit)

# for letter in fruit:
#     print(letter)

def backwards(word):
    index = len(word)-1
    while index >= 0:
        print(word[index])
        index = index - 1
    


# backwards('hola')

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter + suffix)















