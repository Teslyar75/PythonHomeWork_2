"""
ГЕНЕРАТОРИ (GENERATORS) - Ефективна робота з послідовностями

Генератор - це функція, яка повертає ітератор за допомогою ключового слова yield.
На відміну від звичайних функцій, генератори не зберігають всі значення в пам'яті,
а генерують їх "на льоту" при кожному виклику next().

Переваги генераторів:
- Ефективне використання пам'яті (лінива обробка)
- Можливість працювати з нескінченними послідовностями
- Зручний синтаксис для створення ітераторів
- Можливість підтримки стану між викликами

Використання:
- Обробка великих файлів
- Робота з потоками даних
- Створення нескінченних послідовностей
- Pipeline обробки даних
"""

# ============================================================
# ІТЕРАТОРИ vs ГЕНЕРАТОРИ
# ============================================================

print("=== ІТЕРАТОРИ vs ГЕНЕРАТОРИ ===\n")

# Звичайний список (всі елементи в пам'яті)
regular_list = [1, 2, 3, 4, 5]
print("Звичайний список:", regular_list)
print("Розмір у пам'яті:", regular_list.__sizeof__(), "байт")

# Ітератор зі списку
list_iter = iter(regular_list)
print("\nІтератор:")
print("next(list_iter):", next(list_iter))  # 1
print("next(list_iter):", next(list_iter))  # 2
print("next(list_iter):", next(list_iter))  # 3

# Коли елементи закінчаться - StopIteration
# print(next(list_iter))  # 4
# print(next(list_iter))  # 5
# print(next(list_iter))  # StopIteration!

# Цикл for автоматично обробляє StopIteration
print("\nІтерація через for:")
for item in [1, 2, 3]:
    print(f"  {item}")

# ============================================================
# СТВОРЕННЯ ГЕНЕРАТОРІВ (yield)
# ============================================================

print("\n" + "="*50)
print("=== СТВОРЕННЯ ГЕНЕРАТОРІВ ===\n")

# Звичайна функція - повертає все одразу
def counter_function(stop):
    """Звичайна функція - повертає результат одразу"""
    counter = 0
    for _ in range(stop):
        counter += 1
    return counter

print("Звичайна функція:")
result = counter_function(10)
print(f"counter_function(10) = {result}\n")

# Функція-генератор - повертає значення по одному
def counter_generator(stop):
    """Генератор - повертає значення по одному через yield"""
    counter = 0
    while counter < stop:
        counter += 1
        yield counter  # "Заморожує" функцію і повертає значення

print("Функція-генератор:")
gen = counter_generator(5)
print(f"Тип: {type(gen)}")  # <class 'generator'>
print(f"gen = counter_generator(5): {gen}")

print("\nВиклики next():")
print(f"next(gen) = {next(gen)}")  # 1
print(f"next(gen) = {next(gen)}")  # 2
print(f"next(gen) = {next(gen)}")  # 3

print("\nЗалишок через цикл:")
for value in gen:
    print(f"  {value}")  # 4, 5

# ============================================================
# ПРИКЛАДИ ГЕНЕРАТОРІВ
# ============================================================

print("\n" + "="*50)
print("=== ПРИКЛАДИ ГЕНЕРАТОРІВ ===\n")

# 1. Нескінченний генератор
def infinite_counter():
    """Нескінченний лічильник"""
    n = 0
    while True:
        yield n
        n += 1

print("--- Нескінченний лічильник ---")
counter = infinite_counter()
print(f"next() викликів: {next(counter)}, {next(counter)}, {next(counter)}")

# 2. Генератор квадратів
def squares_generator(n):
    """Генерує квадрати чисел від 1 до n"""
    for i in range(1, n + 1):
        yield i ** 2

print("\n--- Квадрати чисел 1-5 ---")
for square in squares_generator(5):
    print(f"  {square}")

# 3. Генератор Фібоначчі
def fibonacci_generator():
    """Нескінченний генератор чисел Фібоначчі"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n--- Числа Фібоначчі ---")
fib = fibonacci_generator()
print("Перші 10 чисел Фібоначчі:")
for i in range(10):
    print(f"  {next(fib)}", end=" ")
print("\n")

# 4. Генератор парних чисел
def even_numbers(start, end):
    """Генерує парні числа в діапазоні"""
    for n in range(start, end + 1):
        if n % 2 == 0:
            yield n

print("--- Парні числа від 1 до 20 ---")
print(list(even_numbers(1, 20)))

# 5. Зворотній лічильник
def countdown(n):
    """Зворотній відлік від n до 1"""
    while n > 0:
        yield n
        n -= 1
    yield "Пуск!"

print("\n--- Зворотній відлік ---")
for value in countdown(5):
    print(f"  {value}")

# ============================================================
# GENERATOR EXPRESSIONS - Генераторні вирази
# ============================================================

print("\n" + "="*50)
print("=== GENERATOR EXPRESSIONS ===\n")

# Синтаксис: (вираз for елемент in послідовність)
# Схожі на list comprehensions, але з круглими дужками

# List comprehension - створює список в пам'яті
list_comp = [x ** 2 for x in range(10)]
print("List comprehension:", list_comp)
print("Розмір у пам'яті:", list_comp.__sizeof__(), "байт")

# Generator expression - створює генератор
gen_exp = (x ** 2 for x in range(10))
print("\nGenerator expression:", gen_exp)
print("Розмір у пам'яті:", gen_exp.__sizeof__(), "байт")
print("Значення:", list(gen_exp))

# Генератор парних квадратів
even_squares = (x ** 2 for x in range(20) if x % 2 == 0)
print("\nПарні квадрати:", list(even_squares))

# Використання з функціями
print("\nСума квадратів 1-10:")
print(sum(x ** 2 for x in range(1, 11)))

print("Максимальне значення:")
print(max(x ** 2 for x in range(1, 11)))

# ============================================================
# МЕТОДИ ГЕНЕРАТОРІВ: send(), throw(), close()
# ============================================================

print("\n" + "="*50)
print("=== МЕТОДИ ГЕНЕРАТОРІВ ===\n")

# send() - дозволяє відправити значення в генератор
def echo_generator():
    """Генератор, який приймає значення через send()"""
    print("Генератор запущено")
    while True:
        received = yield  # Отримує значення від send()
        if received is None:
            break
        print(f"  Отримано: {received}")
        yield f"Відповідь: {received.upper()}"

print("--- send() ---")
gen = echo_generator()
next(gen)  # Ініціалізація генератора (до першого yield)
print(gen.send("hello"))
next(gen)  # Переходимо до наступного yield
print(gen.send("world"))

# Приклад з накопиченням значень
def accumulator():
    """Генератор-акумулятор"""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

print("\n--- Акумулятор ---")
acc = accumulator()
print(f"Початок: {next(acc)}")  # 0
print(f"Додаємо 5: {acc.send(5)}")  # 5
print(f"Додаємо 10: {acc.send(10)}")  # 15
print(f"Додаємо 7: {acc.send(7)}")  # 22

# throw() - викидає виняток всередині генератора
def error_handling_generator():
    """Генератор з обробкою помилок"""
    try:
        while True:
            value = yield
            print(f"  Отримано: {value}")
    except ValueError as e:
        print(f"  Помилка оброблена: {e}")
        yield "Генератор відновлено"

print("\n--- throw() ---")
gen = error_handling_generator()
next(gen)
gen.send(10)
gen.send(20)
try:
    gen.throw(ValueError, "Тестова помилка")
    print(next(gen))
except StopIteration:
    print("  Генератор завершено")

# close() - закриває генератор
def closeable_generator():
    """Генератор, який можна закрити"""
    try:
        while True:
            value = yield
            print(f"  Оброблено: {value}")
    finally:
        print("  Генератор закрито (finally)")

print("\n--- close() ---")
gen = closeable_generator()
next(gen)
gen.send(1)
gen.send(2)
gen.close()
print("Генератор закрито")

# ============================================================
# ПРАКТИЧНІ ПРИКЛАДИ
# ============================================================

print("\n" + "="*50)
print("=== ПРАКТИЧНІ ПРИКЛАДИ ===\n")

# 1. Читання великих файлів
def read_file_lines(filepath):
    """Генератор для читання файлу по рядках"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"Файл {filepath} не знайдено")
        yield None

# Створимо тестовий файл
print("--- Читання файлу ---")
test_file = "test_generator_file.txt"
with open(test_file, 'w', encoding='utf-8') as f:
    f.write("Рядок 1\n")
    f.write("Рядок 2\n")
    f.write("Рядок 3\n")

print(f"Створено файл {test_file}")
for line in read_file_lines(test_file):
    if line:
        print(f"  {line}")

# Видалимо тестовий файл
import os
os.remove(test_file)
print(f"Файл {test_file} видалено\n")

# 2. Батчування даних
def batch_generator(data, batch_size):
    """Розбиває дані на батчі"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

print("--- Батчування ---")
data = list(range(1, 21))
print(f"Дані: {data}")
print(f"Батчі по 5:")
for batch in batch_generator(data, 5):
    print(f"  {batch}")

# 3. Pipeline обробки даних
def numbers():
    """Генератор чисел"""
    for i in range(1, 11):
        yield i

def square(numbers):
    """Піднімає числа до квадрату"""
    for n in numbers:
        yield n ** 2

def even_only(numbers):
    """Фільтрує тільки парні"""
    for n in numbers:
        if n % 2 == 0:
            yield n

print("\n--- Pipeline обробки ---")
pipeline = even_only(square(numbers()))
print("Парні квадрати чисел 1-10:")
print(list(pipeline))

# 4. Генератор простих чисел
def prime_generator(limit):
    """Генерує прості числа до limit"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

print("\n--- Прості числа ---")
print("Прості числа до 50:")
print(list(prime_generator(50)))

# 5. Генератор діапазонів (з кроком)
def custom_range(start, stop, step=1):
    """Власна реалізація range()"""
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step

print("\n--- Власний range ---")
print("custom_range(0, 10, 2):", list(custom_range(0, 10, 2)))
print("custom_range(10, 0, -2):", list(custom_range(10, 0, -2)))

# 6. Генератор для пагінації
def paginate(items, page_size):
    """Розбиває список на сторінки"""
    for i in range(0, len(items), page_size):
        yield {
            'page': i // page_size + 1,
            'items': items[i:i + page_size]
        }

print("\n--- Пагінація ---")
items = [f"Елемент {i}" for i in range(1, 26)]
print("Пагінація 25 елементів по 10 на сторінку:")
for page_data in paginate(items, 10):
    print(f"  Сторінка {page_data['page']}: {len(page_data['items'])} елементів")

# 7. Генератор для симуляції даних
def data_stream_simulator(num_records):
    """Симулює потік даних (наприклад, від сенсора)"""
    import random
    for i in range(num_records):
        yield {
            'id': i + 1,
            'temperature': round(random.uniform(18.0, 26.0), 2),
            'humidity': round(random.uniform(40.0, 70.0), 2)
        }

print("\n--- Симуляція потоку даних ---")
print("Перші 5 записів з сенсора:")
for i, data in enumerate(data_stream_simulator(5)):
    print(f"  {data}")

# ============================================================
# YIELD FROM (Python 3.3+)
# ============================================================

print("\n" + "="*50)
print("=== YIELD FROM ===\n")

# yield from дозволяє делегувати генерацію іншому генератору
def generator1():
    """Перший генератор"""
    yield 1
    yield 2
    yield 3

def generator2():
    """Другий генератор"""
    yield 4
    yield 5
    yield 6

# Без yield from
def combined_old():
    """Об'єднання генераторів (старий спосіб)"""
    for value in generator1():
        yield value
    for value in generator2():
        yield value

# З yield from
def combined_new():
    """Об'єднання генераторів (з yield from)"""
    yield from generator1()
    yield from generator2()

print("Без yield from:", list(combined_old()))
print("З yield from:", list(combined_new()))

# Приклад з деревом
def traverse_tree(tree):
    """Обхід дерева (рекурсивно)"""
    yield tree['value']
    for child in tree.get('children', []):
        yield from traverse_tree(child)

tree = {
    'value': 1,
    'children': [
        {'value': 2, 'children': [
            {'value': 4},
            {'value': 5}
        ]},
        {'value': 3, 'children': [
            {'value': 6}
        ]}
    ]
}

print("\nОбхід дерева:")
print(list(traverse_tree(tree)))

# ============================================================
# ПОРІВНЯННЯ: СПИСОК vs ГЕНЕРАТОР
# ============================================================

print("\n" + "="*50)
print("=== ПОРІВНЯННЯ: СПИСОК vs ГЕНЕРАТОР ===\n")

import sys

# Список (всі елементи в пам'яті)
large_list = [x ** 2 for x in range(1000)]
print(f"Список 1000 елементів:")
print(f"  Розмір: {sys.getsizeof(large_list)} байт")

# Генератор (генерує по одному)
large_gen = (x ** 2 for x in range(1000))
print(f"\nГенератор 1000 елементів:")
print(f"  Розмір: {sys.getsizeof(large_gen)} байт")

print(f"\nЕкономія пам'яті: {sys.getsizeof(large_list) - sys.getsizeof(large_gen)} байт")

# ============================================================
# КОЛИ ВИКОРИСТОВУВАТИ ГЕНЕРАТОРИ
# ============================================================

print("\n" + "="*50)
print("=== КОЛИ ВИКОРИСТОВУВАТИ ГЕНЕРАТОРИ ===\n")

tips = """
ВИКОРИСТОВУЙТЕ ГЕНЕРАТОРИ, КОЛИ:
✓ Працюєте з великими даними
✓ Не потрібен повторний доступ до даних
✓ Обробляєте потоки даних
✓ Потрібна лінива обробка (lazy evaluation)
✓ Працюєте з нескінченними послідовностями

ВИКОРИСТОВУЙТЕ СПИСКИ, КОЛИ:
✓ Потрібен множинний доступ до даних
✓ Потрібна індексація
✓ Дані невеликі
✓ Потрібно змінювати дані
✓ Потрібен len() або інші операції зі списками
"""

print(tips)

print("\n✓ Генератори - потужний інструмент для ефективної роботи з даними!")