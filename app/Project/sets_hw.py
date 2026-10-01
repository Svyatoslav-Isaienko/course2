print("=" * 40, "Завдання 1", "=" * 40)

numbers = [10, 20, 10, 30, 20, 40, 10, 50]
numbers_set = set(numbers)

print("Початковий список:", numbers)
print("Множина:", numbers_set)
print("Кількість унікальних чисел:", len(numbers_set))
print("Чи є 30 у множині:", 30 in numbers_set)
print("Чи є 100 у множині:", 100 in numbers_set)



print("\n" + "=" * 40, "Завдання 2", "=" * 40)

data = [15, "Python", 15, True, "Python", 3.14, False, True]
data_set = set(data)
print("Множина:", data_set)


data_set.add("Redis")
print("Після додавання 'Redis':", data_set)

data_set.add(100)
print("Після додавання 100:", data_set)

data_set.remove("Python")
print("Після видалення 'Python':", data_set)

print("Чи є True:", True in data_set)
print("Чи є False:", False in data_set)



print("\n" + "=" * 40, "Завдання 3", "=" * 40)

python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"}

union_operator = python_students | redis_students
union_method = python_students.union(redis_students)

print("Python або Redis (оператор |):", union_operator)
print("Python або Redis (.union()):  ", union_method)
print("Результати однакові:", union_operator == union_method)



print("\n" + "=" * 40, "Завдання 4", "=" * 40)

intersection_operator = python_students & redis_students
intersection_method = python_students.intersection(redis_students)

print("Python і Redis (оператор &):      ", intersection_operator)
print("Python і Redis (.intersection()): ", intersection_method)
print("Результати однакові:", intersection_operator == intersection_method)



print("\n" + "=" * 40, "Завдання 5", "=" * 40)

all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students_2 = {"Anna", "Oleh", "Ivan"}

diff_operator = all_students - python_students_2
diff_method = all_students.difference(python_students_2)

print("Ще не вивчають Python (оператор -):    ", diff_operator)
print("Ще не вивчають Python (.difference()): ", diff_method)
print("Результати однакові:", diff_operator == diff_method)


print("\n" + "=" * 40, "Завдання 6", "=" * 40)

numbers6 = {10, 20, 30}
print("Початкова множина:", numbers6)

numbers6.add(40)
print("Після add(40):", numbers6)


print("Після повторного add(40):", numbers6)

numbers6.update([50, 60, 70])
print("Після update([50, 60, 70]):", numbers6)

numbers6.remove(20)
print("Після remove(20):", numbers6)


numbers6.discard(100)
print("Після discard(100) (елемента не було, помилки немає):", numbers6)

popped = numbers6.pop()
print("Видалений pop() елемент:", popped)
print("Остаточна множина:", numbers6)