### Завдання 1 Ім'я змінної
value_input = input("Введіть ім'я змінної: ")

if value_input.isdigit() or value_input[0].isdigit():
    result = False

elif any(char.isupper() or (char != '_' and not char.isidentifier()) for char in value_input):
    result = False

else:
    keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
                'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try',
                'while', 'with', 'yield']
    result = value_input not in keywords and not value_input[0].isdigit()

print(result)

### Завдання 2 Модифікувати калькулятор
while True:
    number_1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    number_2 = float(input("Введите второе число: "))

    result = 0

    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        if number_2 == 0:
            print("Делить на ноль нельзя")
        else:
            result = number_1 / number_2
    else:
        print('Ошибка')

    print("Результат:", result)

    user_input = input("Хотите продолжить? (y/n): ")
    if user_input.lower() != 'y':
        break
