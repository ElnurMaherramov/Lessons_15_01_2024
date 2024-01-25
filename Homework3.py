### Завдання 1 Найпростіший калькулятор ###

number_1 = float(input())
operator = input()
number_2 = float(input())
if operator == '+':
    print(number_1 + number_2)
elif operator == '-':
    print(number_1 - number_2)
elif operator == '*':
    print(number_1 * number_2)
elif operator == '/':
    if number_2 == 0:
        print('На ноль делить нельзя')
    print(number_1 / number_2)
else:
    print('Ошибка')

### Завдання 2 Перемістити елемент у списку ###

value_list_1 = [12, 3, 4, 10]
value_list_2 = [1]
value_list_3 = []
value_list_4 = [12, 3, 4, 10, 8]

if value_list_1:
    value_list_1.insert(0, value_list_1[-1])
    value_list_1.pop()

if value_list_2:
    value_list_2.insert(0, value_list_2[-1])
    value_list_2.pop()

if value_list_3:
    value_list_3.insert(0, value_list_3[-1])
    value_list_3.pop()

if value_list_4:
    value_list_4.insert(0, value_list_4[-1])
    value_list_4.pop()

print('\n', value_list_1, '\n', value_list_2, '\n', value_list_3, '\n', value_list_4)