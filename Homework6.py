### Завдання 1

people = [{"name": "John", "age": 15},
          {"name": "Tom", "age": 15},
          {"name": "Timmy", "age": 35},
          {"name": "Jack", "age": 45}
]

min_age = min(person["age"] for person in people)

young_names = [person["name"] for person in people if person["age"] == min_age]

print("Самые молодые:", young_names)

max_name = max(len(person["name"]) for person in people)

longest_names = [person["name"] for person in people if len(person["name"]) == max_name]

print("Самые длинные имена:", longest_names)

age_people = sum(person["age"] for person in people)

avg_age = age_people / len(people)

print("Средний возраст:", avg_age)

### Завдання 2

my_dict_1 = {'Number_1': 1,
             'Number_2': 2,
             'Number_3': 3
}
my_dict_2 = {'Number_2': 4,
             'Number_3': 5,
             'Number_4': 6
}

my_keys = [key for key in my_dict_1.keys() if key in my_dict_2]

print("Ключи, которые есть в обоих словарях:", my_keys)

unique_keys_in_1_dict = [key for key in my_dict_1.keys() if key not in my_dict_2]

print("Ключи, которые есть только в первом словаре:", unique_keys_in_1_dict)

new_dict = {key: my_dict_1[key] for key in my_dict_1.keys() if key not in my_dict_2}

print("Новый словарь:", new_dict)

new_general_dict = {}

for key in my_dict_1.keys():
    if key in my_dict_2:
        new_general_dict[key] = [my_dict_1[key], my_dict_2[key]]
    else:
        new_general_dict[key] = my_dict_1[key]

for key in my_dict_2.keys():
    if key not in my_dict_1:
        new_general_dict[key] = my_dict_2[key]

print("Объединенный новый словарь:", new_general_dict)