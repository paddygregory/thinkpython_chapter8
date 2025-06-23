def check(word):
    if word == 'banana':
        print('All right, bananas.')
    else:
        print('I am not sure what you are talking about.')

#check('banana')

def banana(word):
    if word < 'banana':
        print('Your word,' + word + ', comes before banana.')
    elif word > 'banana':
        print('Your word,' + word + ', comes after banana.')
    else:
        print('All right, bananas.')

banana('apple')

