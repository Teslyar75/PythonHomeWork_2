"""
СЛОВНИКИ (DICTIONARIES) - Колекція пар ключ-значення

Словник (dict) – це неупорядкована (з Python 3.7+ зберігає порядок вставки) колекція пар ключ-значення.
Ключі повинні бути унікальними та незмінними (immutable), значення можуть бути будь-якого типу.

Властивості словників:
- Неупорядковані (до Python 3.7) / упорядковані за вставкою (з Python 3.7+)
- Змінні (можна додавати, видаляти, змінювати елементи)
- Ключі повинні бути унікальними
- Дуже швидкий доступ до елементів за ключем (O(1))
- Ключі можуть бути тільки незмінними типами (int, str, tuple, але не list)

Використання:
- Зберігання даних з іменованими полями
- Кеш та індекси
- Конфігурації та налаштування
- JSON-подібні структури даних
"""

# ============================================================
# СТВОРЕННЯ СЛОВНИКІВ
# ============================================================

print("=== СТВОРЕННЯ СЛОВНИКІВ ===\n")

# Порожній словник
d1 = {}
d2 = dict()
print("Порожні словники:", d1, d2)

# Словник з елементами
person = {"name": "Іван", "age": 25, "city": "Київ"}
print("Словник person:", person)

# Різні способи створення
# 1. Літерали
dict1 = {"a": 1, "b": 2, "c": 3}

# 2. Конструктор dict()
dict2 = dict(a=1, b=2, c=3)  # Ключі без лапок!

# 3. З списку кортежів
dict3 = dict([("a", 1), ("b", 2), ("c", 3)])

# 4. З двох списків через zip()
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict4 = dict(zip(keys, values))

print("\nРізні способи створення:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)
print("dict4:", dict4)

# Словник з різними типами даних
mixed_dict = {
    "string": "текст",
    "number": 42,
    "float": 3.14,
    "list": [1, 2, 3],
    "dict": {"nested": "словник"},
    "tuple": (1, 2, 3),
    "bool": True,
    "none": None
}
print("\nЗмішаний словник:", mixed_dict)

# Незмінні ключі (можна використовувати)
valid_keys = {
    42: "int ключ",
    3.14: "float ключ",
    "string": "str ключ",
    (1, 2): "tuple ключ",
    True: "bool ключ"  # True == 1, тому перезапише значення для 42!
}
print("\nРізні типи ключів:", valid_keys)

# НЕ можна використовувати змінні типи як ключі
# invalid = {[1, 2]: "значення"}  # TypeError: unhashable type: 'list'
# invalid = {{1: 2}: "значення"}  # TypeError: unhashable type: 'dict'

# ============================================================
# ДОСТУП ДО ЕЛЕМЕНТІВ
# ============================================================

print("\n=== ДОСТУП ДО ЕЛЕМЕНТІВ ===\n")

d1 = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Доступ через []
print("d1['key1'] =", d1["key1"])  # Output: value1

# Якщо ключ не існує - KeyError
try:
    print(d1["неіснуючий_ключ"])
except KeyError:
    print("KeyError: ключ не знайдено")

# Доступ через get() - безпечніший спосіб
print("\nd1.get('key1') =", d1.get("key1"))  # Output: value1
print("d1.get('неіснуючий') =", d1.get("неіснуючий"))  # Output: None
print("d1.get('неіснуючий', 'default') =", d1.get("неіснуючий", "default"))  # Output: default

# Перевірка наявності ключа
print("\n'key1' in d1:", "key1" in d1)  # True
print("'key99' in d1:", "key99" in d1)  # False

# len() - повертає кількість пар ключ-значення
length = len(d1)
print("\nДовжина словника:", length)

# ============================================================
# ЗМІНА ТА ДОДАВАННЯ ЕЛЕМЕНТІВ
# ============================================================

print("\n=== ЗМІНА ТА ДОДАВАННЯ ===\n")

d1 = {"key1": "value1"}
print("Початковий словник:", d1)

# Зміна значення існуючого ключа
d1["key1"] = "new_value1"
print("Після зміни key1:", d1)

# Додавання нового ключа
# Якщо спробувати надати значення для ключа, якого не існує - створюється новий елемент
d1["key2"] = "Hello"
print("Після додавання key2:", d1)

d1["key3"] = "World"
d1["key4"] = 123
print("Після додавання key3 та key4:", d1)

# ============================================================
# МЕТОДИ СЛОВНИКІВ
# ============================================================

print("\n=== ОСНОВНІ МЕТОДИ ===\n")

# --- get(key, default) ---
print("--- get() ---")
d = {"name": "Іван", "age": 25}
print("d.get('name'):", d.get("name"))
print("d.get('email'):", d.get("email"))  # None
print("d.get('email', 'немає email'):", d.get("email", "немає email"))

# --- setdefault(key, default) ---
print("\n--- setdefault() ---")
# Якщо ключ існує - повертає значення, якщо ні - створює з default значенням
d = {"name": "Іван"}
print("Початковий словник:", d)

result1 = d.setdefault("name", "Петро")
print("d.setdefault('name', 'Петро'):", result1)  # Іван (вже існує)

result2 = d.setdefault("age", 25)
print("d.setdefault('age', 25):", result2)  # 25 (додано новий)
print("Словник після setdefault:", d)

# --- update(other_dict) ---
print("\n--- update() ---")
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}  # b перезапише значення в d1
print("d1:", d1)
print("d2:", d2)

d1.update(d2)
print("d1.update(d2):", d1)  # {'a': 1, 'b': 20, 'c': 3}

# update може приймати різні формати
d = {"x": 1}
d.update({"y": 2})  # Словник
d.update([("z", 3)])  # Список кортежів
d.update(w=4)  # Іменовані аргументи
print("d після різних update:", d)

# --- fromkeys(keys, value) ---
print("\n--- fromkeys() ---")
# Створює словник з послідовності ключів з однаковим значенням
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print("dict.fromkeys(['a', 'b', 'c'], 0):", d)

# Без значення - створює з None
d = dict.fromkeys(["x", "y", "z"])
print("dict.fromkeys(['x', 'y', 'z']):", d)

# ============================================================
# МЕТОДИ ДЛЯ ІТЕРАЦІЇ
# ============================================================

print("\n=== МЕТОДИ ДЛЯ ІТЕРАЦІЇ ===\n")

person = {"name": "Іван", "age": 25, "city": "Київ"}

# --- keys() ---
print("--- keys() ---")
print("person.keys():", person.keys())
for key in person.keys():
    print(f"  Ключ: {key}")

# --- values() ---
print("\n--- values() ---")
print("person.values():", person.values())
for value in person.values():
    print(f"  Значення: {value}")

# --- items() ---
print("\n--- items() ---")
print("person.items():", person.items())
for key, value in person.items():
    print(f"  {key}: {value}")

# Якщо передати просто словник до циклу - будуть ключі
print("\nПростий цикл по словнику (тільки ключі):")
for key in person:
    print(f"  {key}")

# ============================================================
# МЕТОДИ ВИДАЛЕННЯ
# ============================================================

print("\n=== МЕТОДИ ВИДАЛЕННЯ ===\n")

# --- pop(key, default) ---
print("--- pop() ---")
d = {"a": 1, "b": 2, "c": 3}
print("Початковий словник:", d)

removed = d.pop("b")
print("d.pop('b'):", removed)  # 2
print("Словник після pop:", d)

# Якщо ключ не існує - можна передати default
removed = d.pop("z", "не знайдено")
print("d.pop('z', 'не знайдено'):", removed)

# Без default - KeyError
try:
    d.pop("неіснуючий_ключ")
except KeyError:
    print("KeyError: ключ не знайдено (без default)")

# --- popitem() ---
print("\n--- popitem() ---")
d = {"a": 1, "b": 2, "c": 3}
print("Початковий словник:", d)

removed = d.popitem()  # Видаляє та повертає останню пару (з Python 3.7+)
print("d.popitem():", removed)
print("Словник після popitem:", d)

# --- del ---
print("\n--- del ---")
d = {"a": 1, "b": 2, "c": 3}
print("Початковий словник:", d)

del d["b"]  # Видаляє елемент за ключем
print("Після del d['b']:", d)

# Якщо ключ не існує - KeyError
try:
    del d["неіснуючий"]
except KeyError:
    print("KeyError: ключ не існує")

# --- clear() ---
print("\n--- clear() ---")
d = {"a": 1, "b": 2, "c": 3}
print("Перед clear:", d)
d.clear()
print("Після clear:", d)  # {}

# ============================================================
# КОПІЮВАННЯ СЛОВНИКІВ
# ============================================================

print("\n=== КОПІЮВАННЯ ===\n")

# Просте присвоєння НЕ створює копію!
d1 = {"a": 1, "b": 2}
d2 = d1  # Це посилання, не копія!
d2["c"] = 3
print("d1:", d1)  # {'a': 1, 'b': 2, 'c': 3} - змінився теж!
print("d2:", d2)  # {'a': 1, 'b': 2, 'c': 3}

# copy() – створює поверхневу копію
d1 = {"a": 1, "b": 2}
d2 = d1.copy()
d2["c"] = 3
print("\nПісля copy():")
print("d1:", d1)  # {'a': 1, 'b': 2} - не змінився
print("d2:", d2)  # {'a': 1, 'b': 2, 'c': 3}

# Поверхнева vs глибока копія
import copy

nested = {"a": [1, 2, 3], "b": [4, 5, 6]}
shallow = nested.copy()
deep = copy.deepcopy(nested)

nested["a"][0] = 999
print("\nПісля зміни nested['a'][0] = 999:")
print("Оригінал:", nested)   # {'a': [999, 2, 3], 'b': [4, 5, 6]}
print("Shallow:", shallow)    # {'a': [999, 2, 3], 'b': [4, 5, 6]} - змінився!
print("Deep:", deep)          # {'a': [1, 2, 3], 'b': [4, 5, 6]} - не змінився

# ============================================================
# DICT COMPREHENSIONS - Генератори словників
# ============================================================

print("\n=== DICT COMPREHENSIONS ===\n")

# Базовий синтаксис: {ключ: значення for елемент in послідовність}

# Словник квадратів
squares = {x: x**2 for x in range(1, 6)}
print("Квадрати:", squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# З умовою
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Квадрати парних:", even_squares)

# Перетворення словника
prices = {"apple": 100, "banana": 50, "orange": 75}
discounted = {fruit: price * 0.9 for fruit, price in prices.items()}
print("\nПочаткові ціни:", prices)
print("Зі знижкою 10%:", discounted)

# Інверсія словника (ключі <-> значення)
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print("\nОригінал:", original)
print("Інвертований:", inverted)

# З умовою if-else
numbers = {x: ("парне" if x % 2 == 0 else "непарне") for x in range(1, 6)}
print("\nПарність:", numbers)

# З enumerate
words = ["яблуко", "банан", "апельсин"]
word_dict = {index: word for index, word in enumerate(words)}
print("\nСловник з enumerate:", word_dict)

# ============================================================
# ВКЛАДЕНІ СЛОВНИКИ
# ============================================================

print("\n=== ВКЛАДЕНІ СЛОВНИКИ ===\n")

# Словник словників
users = {
    "user1": {"name": "Іван", "age": 25, "city": "Київ"},
    "user2": {"name": "Марія", "age": 30, "city": "Львів"},
    "user3": {"name": "Петро", "age": 35, "city": "Одеса"}
}

print("Всі користувачі:")
for user_id, user_data in users.items():
    print(f"  {user_id}: {user_data}")

# Доступ до вкладених даних
print("\nІм'я user1:", users["user1"]["name"])
print("Вік user2:", users["user2"]["age"])

# Безпечний доступ
email = users.get("user1", {}).get("email", "немає email")
print("Email user1:", email)

# ============================================================
# СОРТУВАННЯ СЛОВНИКІВ
# ============================================================

print("\n=== СОРТУВАННЯ ===\n")

scores = {"Іван": 85, "Марія": 92, "Петро": 78, "Анна": 95}

# Сортування за ключами
sorted_by_keys = dict(sorted(scores.items()))
print("За ключами:", sorted_by_keys)

# Сортування за значеннями
sorted_by_values = dict(sorted(scores.items(), key=lambda item: item[1]))
print("За значеннями (зростання):", sorted_by_values)

# Сортування за значеннями (спадання)
sorted_by_values_desc = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print("За значеннями (спадання):", sorted_by_values_desc)

# ============================================================
# ОБ'ЄДНАННЯ СЛОВНИКІВ
# ============================================================

print("\n=== ОБ'ЄДНАННЯ СЛОВНИКІВ ===\n")

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"b": 20, "e": 5}  # b перезапише значення

# 1. Через update()
result = d1.copy()
result.update(d2)
result.update(d3)
print("Через update():", result)

# 2. Через {**dict1, **dict2} (Python 3.5+)
merged = {**d1, **d2, **d3}
print("Через **:", merged)

# 3. Через оператор | (Python 3.9+)
try:
    merged = d1 | d2 | d3
    print("Через | :", merged)
except TypeError:
    print("Оператор | доступний з Python 3.9+")

# ============================================================
# ПРАКТИЧНІ ПРИКЛАДИ
# ============================================================

print("\n=== ПРАКТИЧНІ ПРИКЛАДИ ===\n")

# 1. Підрахунок частоти елементів
text = "hello world hello python world"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Частота слів:", word_count)

# Те ж саме через dict comprehension
words = text.split()
word_count2 = {word: words.count(word) for word in set(words)}
print("Частота (comprehension):", word_count2)

# 2. Групування даних
students = [
    {"name": "Іван", "grade": "A"},
    {"name": "Марія", "grade": "B"},
    {"name": "Петро", "grade": "A"},
    {"name": "Анна", "grade": "B"}
]

grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])

print("\nГрупування студентів за оцінками:", grouped)

# 3. Кешування результатів функцій
cache = {}
def expensive_function(n):
    if n in cache:
        print(f"  Взято з кешу: {n}")
        return cache[n]
    print(f"  Обчислення: {n}")
    result = n ** 2
    cache[n] = result
    return result

print("\nКешування:")
print("Результат:", expensive_function(5))
print("Результат:", expensive_function(3))
print("Результат:", expensive_function(5))  # З кешу!
print("Кеш:", cache)

# 4. Інвертування словника (для унікальних значень)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print("\nІнверсія:", original, "->", inverted)

# 5. Фільтрація словника
data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
filtered = {k: v for k, v in data.items() if v > 2}
print("\nФільтрація (v > 2):", filtered)

print("\n✓ Словники - найпотужніша структура даних у Python!")

