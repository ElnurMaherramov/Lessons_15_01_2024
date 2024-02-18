### Завдання 1
def popular_words(text, words):
    words_list = text.lower().split()

    popularity_words = {}

    for word in words:
        popularity_words[word] = words_list.count(word)

    return popularity_words


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')

### Завдання 2
def difference(*args):
    if not args:
        return 0

    min_number = min(args)
    max_number = max(args)

    return round(max_number - min_number, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')