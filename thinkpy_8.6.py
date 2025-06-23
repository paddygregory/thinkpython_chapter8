def find(word,letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print(find('banana','a'))

def find(word, letter, search):
    index = int(search)
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('banana','a',3))
print(find('banana','a',4))



      








