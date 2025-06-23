def count(word,letter):
    count = 0
    for parts in word:
        if parts == letter:
            count = count + 1
    return count

#print(count('banana','a'))

def count(word, letter, search):
    count = 0
    for parts in word[int(search):]:
            if parts == letter:
                count = count + 1
    return count

#print(count('banana','a',4))








                
