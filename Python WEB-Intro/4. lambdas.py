"""
LAMBDA-ФУНКЦІЇ та ФУНКЦІЇ ВИЩОГО ПОРЯДКУ

Lambda-функції - це анонімні (безіменні) функції, які визначаються в один рядок.
Вони корисні для створення простих функцій "на льоту" без необхідності формального визначення.

Синтаксис: lambda аргументи: вираз

Функції вищого порядку - функції, які приймають інші функції як параметри або повертають функції.
Приклади: map(), filter(), sorted(), reduce()
"""

# ============================================================
# ЗВИЧАЙНІ ФУНКЦІЇ (для порівняння)
# ============================================================

print("=== ЗВИЧАЙНІ ФУНКЦІЇ ===\n")

# Проста функція без параметрів
def sample():
    print("Hello, world")
    
sample()

# Функція з параметрами
def sample2(a, b):
    return a + b

print("sample2(1, 2) =", sample2(1, 2))  # Output: 3

# Функція з анотацією типів
def sample3(a: int, b: int) -> int:
    """Додає два цілих числа"""
    return a + b

result1 = sample3(a=10, b=20)  # Іменовані аргументи
result2 = sample3(1, b=2)      # Змішані аргументи
print(f"sample3(10, 20) = {result1}")
print(f"sample3(1, b=2) = {result2}")

# ============================================================
# *args та **kwargs
# ============================================================

print("\n=== *args та **kwargs ===\n")

# *args - дозволяє передати довільну кількість позиційних аргументів (tuple)
# **kwargs - дозволяє передати довільну кількість іменованих аргументів (dict)

def sample4(*args, **kwargs):
    print("Тип args:", type(args))    # <class 'tuple'>
    print("Тип kwargs:", type(kwargs))  # <class 'dict'>
    
    print("\nПозиційні аргументи (*args):")
    for item in args:
        print(f"  Arg: {item}")
    
    print("\nІменовані аргументи (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

print("Виклик 1:")
sample4(1, "Hello", 3, 4, [5, 6, 7], name='Joe', surname='Due', d={"key1": "value1", "key2": "value2"})

print("\n" + "="*50)
print("Виклик 2 з розпакуванням:")
# Розпакування з * та **
sample4(1, *"Hello", 3, 4, *[5, 6, 7], name='Joe', surname='Due', **{"key1": "value1", "key2": "value2"})

# Практичний приклад
def print_info(*args, **kwargs):
    print("\nІнформація:")
    for item in args:
        print(f"  - {item}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\n" + "="*50)
print_info(1, 2, 3, 4, 5, 6, name="Іван", age=18, city="Київ")

# ============================================================
# LAMBDA-ФУНКЦІЇ - Основи
# ============================================================

print("\n" + "="*50)
print("=== LAMBDA-ФУНКЦІЇ ===\n")

# Lambda без параметрів
greeting_lambda = lambda: print("Hello from lambda")
greeting_lambda()  # Output: Hello from lambda

# Lambda з одним параметром
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")  # Output: 25

# Lambda з кількома параметрами
add = lambda x, y: x + y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Ділення на нуль!"

print(f"add(3, 4) = {add(3, 4)}")          # 7
print(f"multiply(3, 4) = {multiply(3, 4)}")  # 12
print(f"divide(10, 2) = {divide(10, 2)}")    # 5.0

# Порівняння: звичайна функція vs lambda
def greeting_func():
    print("Hello from function")

greeting_func()
greeting_lambda()

# Lambda може містити тільки ОДИН вираз (не може містити statements)
# Lambda автоматично повертає результат виразу

# ============================================================
# LAMBDA ЯК ПАРАМЕТР ФУНКЦІЇ
# ============================================================

print("\n=== LAMBDA ЯК ПАРАМЕТР ===\n")

# Функція, яка приймає іншу функцію як параметр
def operation(value1, value2, func):
    """Застосовує функцію func до двох значень"""
    return func(value1, value2)

# Передача lambda як параметра
result_add = operation(12, 10, lambda x, y: x + y)
result_sub = operation(12, 10, lambda x, y: x - y)
result_mul = operation(12, 10, lambda x, y: x * y)
result_pow = operation(12, 10, lambda x, y: x ** y)

print(f"12 + 10 = {result_add}")
print(f"12 - 10 = {result_sub}")
print(f"12 * 10 = {result_mul}")
print(f"12 ^ 10 = {result_pow}")

# ============================================================
# ПОВЕРНЕННЯ LAMBDA З ФУНКЦІЇ
# ============================================================

print("\n=== ПОВЕРНЕННЯ LAMBDA ===\n")

# Функція, яка повертає lambda (замикання)
def selectOperation(operation_name):
    """Повертає відповідну lambda-функцію за назвою операції"""
    if operation_name == "sum":
        return lambda x, y: x + y
    elif operation_name == "dif":
        return lambda x, y: x - y  # ВИПРАВЛЕНО: було x+y
    elif operation_name == "mul":
        return lambda x, y: x * y
    elif operation_name == "div":
        return lambda x, y: x / y if y != 0 else "Помилка: ділення на нуль"
    else:
        return lambda x, y: "Невідома операція"

# Використання
sum_func = selectOperation("sum")
dif_func = selectOperation("dif")
mul_func = selectOperation("mul")

print(f"sum_func(12, 10) = {sum_func(12, 10)}")  # 22
print(f"dif_func(12, 10) = {dif_func(12, 10)}")  # 2
print(f"mul_func(12, 10) = {mul_func(12, 10)}")  # 120

# ============================================================
# MAP() - Застосування функції до кожного елемента
# ============================================================

print("\n=== MAP() ===\n")

numbers = [1, 2, 3, 4, 5]

# map(func, iterable) - застосовує функцію до кожного елемента
squared = list(map(lambda x: x ** 2, numbers))
print(f"Оригінал: {numbers}")
print(f"Квадрати: {squared}")

# map з кількома ітерованими об'єктами
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"\n{list1}")
print(f"{list2}")
print(f"Суми: {sums}")

# Практичні приклади
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(f"\nІмена: {names}")
print(f"Капіталізовані: {capitalized}")

# map з вбудованими функціями
strings = ["1", "2", "3", "4", "5"]
integers = list(map(int, strings))
print(f"\nРядки: {strings}")
print(f"Числа: {integers}")

# ============================================================
# FILTER() - Фільтрація елементів
# ============================================================

print("\n=== FILTER() ===\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(func, iterable) - залишає тільки ті елементи, для яких func повертає True
even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Числа: {numbers}")
print(f"Парні: {even}")
print(f"Непарні: {odd}")

# Фільтрація за умовою
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Більше 5: {greater_than_5}")

# Практичний приклад: фільтрація рядків
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"\nСлова: {words}")
print(f"Довгі слова (>5): {long_words}")

# Фільтрація None та False значень
mixed = [0, 1, False, True, "", "hello", None, [], [1, 2]]
truthy = list(filter(None, mixed))  # Залишає тільки "truthy" значення
print(f"\nЗмішаний список: {mixed}")
print(f"Truthy значення: {truthy}")

# ============================================================
# SORTED() - Сортування зі своєю функцією
# ============================================================

print("\n=== SORTED() та SORT() ===\n")

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6, 10]

# sorted(iterable, key=func, reverse=True|False)
# key - функція, яка визначає за чим сортувати

# Звичайне сортування
sorted_asc = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)
print(f"Оригінал: {numbers}")
print(f"За зростанням: {sorted_asc}")
print(f"За спаданням: {sorted_desc}")

# Сортування за залишком від ділення
sorted_by_mod = sorted(numbers, key=lambda x: x % 3)
print(f"За залишком від ділення на 3: {sorted_by_mod}")

# Сортування за паритетом (парні перші)
sorted_by_parity = sorted(numbers, key=lambda x: x % 2)
print(f"Парні перші: {sorted_by_parity}")

# Сортування рядків
words = ["Python", "java", "C++", "ruby", "JavaScript"]
sorted_default = sorted(words)  # За ASCII (великі літери перші)
sorted_case_insensitive = sorted(words, key=lambda s: s.lower())
sorted_by_length = sorted(words, key=len)

print(f"\nСлова: {words}")
print(f"За алфавітом (default): {sorted_default}")
print(f"Без врахування регістру: {sorted_case_insensitive}")
print(f"За довжиною: {sorted_by_length}")

# Сортування складних об'єктів
students = [
    ("Іван", 85),
    ("Марія", 92),
    ("Петро", 78),
    ("Анна", 95)
]
sorted_by_name = sorted(students, key=lambda student: student[0])
sorted_by_grade = sorted(students, key=lambda student: student[1], reverse=True)

print(f"\nСтуденти: {students}")
print(f"За ім'ям: {sorted_by_name}")
print(f"За оцінкою: {sorted_by_grade}")

# list.sort() - сортує список "на місці" (змінює оригінальний список)
l = [5, 2, 8, 1, 9]
print(f"\nОригінальний список: {l}")
l.sort(key=lambda x: x % 2 == 0, reverse=True)
print(f"Після sort(key=lambda x: x%2==0, reverse=True): {l}")

# ============================================================
# REDUCE() - Згортка послідовності
# ============================================================

print("\n=== REDUCE() ===\n")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# reduce(func, iterable, initial) - застосовує функцію кумулятивно
# func повинна приймати 2 аргументи: акумулятор та поточний елемент

# Сума всіх елементів
total = reduce(lambda acc, x: acc + x, numbers)
print(f"Числа: {numbers}")
print(f"Сума (через reduce): {total}")

# Добуток всіх елементів
product = reduce(lambda acc, x: acc * x, numbers)
print(f"Добуток: {product}")

# Максимальне значення
maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(f"Максимум: {maximum}")

# З початковим значенням
total_with_initial = reduce(lambda acc, x: acc + x, numbers, 100)
print(f"Сума з початковим значенням 100: {total_with_initial}")

# Практичний приклад: об'єднання рядків
words = ["Hello", "World", "Python"]
sentence = reduce(lambda acc, word: acc + " " + word, words)
print(f"\nСлова: {words}")
print(f"Речення: {sentence}")

# ============================================================
# ZIP() - Об'єднання кількох послідовностей
# ============================================================

print("\n=== ZIP() ===\n")

names = ["Іван", "Марія", "Петро"]
ages = [25, 30, 35]
cities = ["Київ", "Львів", "Одеса"]

# zip() об'єднує кілька послідовностей в кортежі
combined = list(zip(names, ages, cities))
print("Об'єднання:")
for person in combined:
    print(f"  {person}")

# Використання з dict()
person_dict = dict(zip(names, ages))
print(f"\nСловник: {person_dict}")

# Розпакування zip
zipped = list(zip(names, ages))
unzipped_names, unzipped_ages = zip(*zipped)
print(f"\nЗапаковано: {zipped}")
print(f"Розпаковані імена: {unzipped_names}")
print(f"Розпаковані віки: {unzipped_ages}")

# ============================================================
# КОМБІНУВАННЯ MAP, FILTER, REDUCE
# ============================================================

print("\n=== КОМБІНУВАННЯ ===\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Знайти суму квадратів парних чисел
result = reduce(
    lambda acc, x: acc + x,  # Сума
    map(
        lambda x: x ** 2,     # Квадрат
        filter(
            lambda x: x % 2 == 0,  # Тільки парні
            numbers
        )
    )
)

print(f"Числа: {numbers}")
print(f"Сума квадратів парних чисел: {result}")
# Пояснення: [2, 4, 6, 8, 10] -> [4, 16, 36, 64, 100] -> 220

# Те ж саме, але більш читабельно
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x ** 2, even_numbers)
total = reduce(lambda acc, x: acc + x, squared)
print(f"Покроково: {total}")

# ============================================================
# ПРАКТИЧНІ ПРИКЛАДИ
# ============================================================

print("\n=== ПРАКТИЧНІ ПРИКЛАДИ ===\n")

# 1. Перетворення списку словників
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

names = list(map(lambda user: user["name"], users))
adults = list(filter(lambda user: user["age"] >= 30, users))

print("Користувачі:", users)
print("Імена:", names)
print("Дорослі (>=30):", adults)

# 2. Обробка матриці
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = reduce(lambda acc, row: acc + row, matrix)
print(f"\nМатриця: {matrix}")
print(f"Плаский список: {flattened}")

# 3. Ланцюжок обробки даних
prices = [100, 200, 150, 300, 250]
# Знижка 10%, потім ПДВ 20%, тільки ціни > 150
final_prices = list(map(
    lambda x: x * 1.2,  # ПДВ +20%
    map(
        lambda x: x * 0.9,  # Знижка -10%
        filter(lambda x: x > 150, prices)  # Тільки > 150
    )
))

print(f"\nПочаткові ціни: {prices}")
print(f"Фінальні ціни (>150, -10%, +20% ПДВ): {final_prices}")

print("\n✓ Lambda-функції - потужний інструмент для написання компактного коду!")



