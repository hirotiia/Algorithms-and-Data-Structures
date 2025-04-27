l = ['Mon', 'tue', 'Wed', 'thu', 'Fri', 'sat', 'Sun']

def change_words(words, fn):
    for word in words:
        print(fn(word))


change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())