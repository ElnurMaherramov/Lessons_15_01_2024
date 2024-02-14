### Завдання 1
def add_one(some_list):
    num = int(''.join(map(str, some_list))) + 1
    result = [int(digit) for digit in str(num)]
    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

### Завдання 2

def find_unique_value(some_list):
    for num in some_list:
        if some_list.count(num) == 1:
            return num
    return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")