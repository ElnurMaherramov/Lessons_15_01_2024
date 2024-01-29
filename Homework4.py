### Завдання 1

value_1 = [0, 1, 0, 12, 3]
value_2 = [0]
value_3 = [1, 0, 13, 0, 0, 0, 5]
value_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

value_1.sort(reverse=True, key=bool)
value_2.sort(reverse=True, key=bool)
value_3.sort(reverse=True, key=bool)
value_4.sort(reverse=True, key=bool)

print(f"{value_1}\n{value_2}\n{value_3}\n{value_4}")

### Завдання 2

number_1 = [1, 3, 5]
number_2 = [6]
number_3 = []

dop_number = 0
for parni in range(0, len(number_1), 2):
    dop_number += number_1[parni]
if number_1:
    print(dop_number * number_1[-1])
else:
    print(0)

dop_number = 0
for parni in range(0, len(number_2), 2):
    dop_number += number_2[parni]
if number_2:
    print(dop_number * number_2[-1])
else:
    print(0)

dop_number = 0
for parni in range(0, len(number_3), 2):
    dop_number += number_3[parni]
if number_3:
    print(dop_number * number_3[-1])
else:
    print(0)

