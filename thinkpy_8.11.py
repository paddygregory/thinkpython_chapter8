def is_reverse(word1, word2):
    i = 0
    j = len(word2) - 1
    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

# print(is_reverse('pots','stop'))

# print(is_reverse('banana','ananab'))
