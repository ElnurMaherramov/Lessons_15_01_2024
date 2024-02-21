### Завдання 1 Генераторна функція
def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

### Завдання 2 Перевірити чи є парним чи ні
def is_even(digit):
    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')