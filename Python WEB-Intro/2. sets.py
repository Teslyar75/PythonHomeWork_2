"""
МНОЖИНИ (SETS) - Неупорядкована колекція унікальних елементів

Множина (set) – це тип даних, який зберігає неупорядковану колекцію унікальних елементів.
Множини автоматично видаляють дублікати і не підтримують індексацію.

Властивості множин:
- Зберігають тільки унікальні елементи (дублікати видаляються автоматично)
- Неупорядковані (не можна звертатися по індексу)
- Змінні (можна додавати/видаляти елементи)
- Швидкий пошук елементів
- Підтримують математичні операції над множинами

Використання:
- Видалення дубликатів зі списку
- Перевірка належності елемента
- Математичні операції (перетин, об'єднання тощо)
"""

# ============================================================
# СТВОРЕННЯ МНОЖИН
# ============================================================

# Порожня множина (ВАЖЛИВО: {} створює словник, не множину!)
empty_set = set()  # Правильно
print("Порожня множина:", empty_set, type(empty_set))

# Множина з елементами
set1 = {2, 3, 4, 5}
print("Множина set1:", set1)

# Автоматичне видалення дублікатів
set_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print("Множина з дублікатами (автоматично видалені):", set_with_duplicates)
# Output: {1, 2, 3, 4, 5}

# Створення множини зі списку (корисно для видалення дублікатів)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = set(list_with_duplicates)
print("Унікальні числа зі списку:", unique_numbers)

# Створення множини з рядка
set_from_string = set("Hello")
print("Множина з рядка:", set_from_string)  # Output: {'H', 'e', 'l', 'o'}

set2 = {6, 7, 8, 9}
print("Множина set2:", set2)

# ============================================================
# ОСНОВНІ ОПЕРАЦІЇ З МНОЖИНАМИ
# ============================================================

print("\n--- ОСНОВНІ ОПЕРАЦІЇ ---")

# Довжина множини
print("Кількість елементів:", len(set1))

# Перевірка наявності елемента (дуже швидка операція!)
print("3 є в множині?", 3 in set1)       # Output: True
print("10 є в множині?", 10 in set1)     # Output: False

# Ітерація по множині
print("Елементи множини:")
for item in set1:
    print(f"  {item}")

# ============================================================
# МАТЕМАТИЧНІ ОПЕРАЦІЇ НАД МНОЖИНАМИ
# ============================================================

print("\n--- МАТЕМАТИЧНІ ОПЕРАЦІЇ ---")

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# union(iterable) чи set1 | set2 – об'єднання множин (всі елементи з обох)
print("\nОБ'ЄДНАННЯ (Union):")
union1 = set1.union(set2)
union2 = set1 | set2
print(f"  {set1} ∪ {set2} = {union1}")
print(f"  setA ∪ setB = {setA | setB}")  # Output: {1,2,3,4,5,6,7,8}

# intersection(iterable) чи set1 & set2 – перетин множин (спільні елементи)
print("\nПЕРЕТИН (Intersection):")
intersection1 = setA.intersection(setB)
intersection2 = setA & setB
print(f"  {setA} ∩ {setB} = {intersection1}")  # Output: {4, 5}
print("  set1 ∩ {1,2,3,4,5,6,7,8} =", set1.intersection({1, 2, 3, 4, 5, 6, 7, 8}))

# difference(iterable) чи set1 - set2 – різниця множин (елементи з першої, яких немає в другій)
print("\nРІЗНИЦЯ (Difference):")
difference1 = setA.difference(setB)
difference2 = setA - setB
print(f"  {setA} - {setB} = {difference1}")  # Output: {1, 2, 3}
print(f"  {setB} - {setA} = {setB - setA}")  # Output: {6, 7, 8}
print("  set1 - {4,5,6,7,8} =", set1.difference({4, 5, 6, 7, 8}))

# symmetric_difference(iterable) чи set1 ^ set2 – симетрична різниця (елементи, що є тільки в одній з множин)
print("\nСИМЕТРИЧНА РІЗНИЦЯ (Symmetric Difference):")
sym_diff1 = setA.symmetric_difference(setB)
sym_diff2 = setA ^ setB
print(f"  {setA} △ {setB} = {sym_diff1}")  # Output: {1, 2, 3, 6, 7, 8}
print("  set1 △ {4,5,6,7,8} =", set1.symmetric_difference({4, 5, 6, 7, 8}))

# ============================================================
# МЕТОДИ ПЕРЕВІРКИ ВІДНОСИН МІЖ МНОЖИНАМИ
# ============================================================

print("\n--- ПЕРЕВІРКА ВІДНОСИН ---")

# isdisjoint(iterable) – перевіряє чи немає у множин спільних елементів
print(f"\n{set1} і {set2} не мають спільних елементів?", set1.isdisjoint(set2))  # Output: True
print(f"{setA} і {setB} не мають спільних елементів?", setA.isdisjoint(setB))  # Output: False

# issubset(iterable) чи set1 <= set2 – перевіряє чи є одна множина підмножиною іншої
subset_example = {2, 3}
print(f"\n{subset_example} є підмножиною {set1}?", subset_example.issubset(set1))  # Output: True
print(f"{set1} є підмножиною {{1,2,3,4,5}}?", set1.issubset({1, 2, 3, 4, 5}))  # Output: False
print(f"{subset_example} <= {set1}?", subset_example <= set1)  # Output: True

# issuperset(iterable) чи set1 >= set2 – перевіряє чи є одна множина надмножиною іншої
print(f"\n{set1} є надмножиною {subset_example}?", set1.issuperset(subset_example))  # Output: True
print(f"{set1} є надмножиною {set2}?", set1.issuperset(set2))  # Output: False
print(f"{set1} >= {subset_example}?", set1 >= subset_example)  # Output: True

# ============================================================
# МЕТОДИ ЗМІНИ МНОЖИН
# ============================================================

print("\n--- МЕТОДИ ЗМІНИ МНОЖИН ---")

# Створюємо копії для демонстрації
test_set = {1, 2, 3, 4, 5}
print("\nПочаткова множина:", test_set)

# add(value) – додає новий елемент у множину
test_set.add(6)
print("Після add(6):", test_set)

# Додавання елемента, який вже є (нічого не станеться)
test_set.add(3)
print("Після add(3) - дублікат:", test_set)

# update(iterable) – додає кілька елементів з іншої послідовності
test_set.update([7, 8, 9])
print("Після update([7, 8, 9]):", test_set)

# Можна передати кілька ітерованих об'єктів
test_set.update([10, 11], {12, 13})
print("Після update([10, 11], {12, 13}):", test_set)

# remove(value) – видаляє елемент з множини (викликає помилку, якщо елемента немає)
test_set.remove(6)
print("Після remove(6):", test_set)

# Спроба видалити неіснуючий елемент викличе помилку KeyError
try:
    test_set.remove(100)
except KeyError:
    print("Помилка: спроба видалити неіснуючий елемент через remove()")

# discard(value) – видаляє елемент з множини (БЕЗ помилки, якщо елемента немає)
test_set.discard(13)
print("Після discard(13):", test_set)

# Видалення неіснуючого елемента - помилки не буде
test_set.discard(100)
print("Після discard(100) - помилки немає:", test_set)

# pop() – видаляє і повертає випадковий елемент (множини неупорядковані!)
removed_element = test_set.pop()
print(f"pop() видалив елемент: {removed_element}")
print("Множина після pop():", test_set)

# clear() – очищення множини
test_set.clear()
print("Після clear():", test_set)

# ============================================================
# МЕТОДИ, ЩО ЗМІНЮЮТЬ МНОЖИНУ "НА МІСЦІ"
# ============================================================

print("\n--- МЕТОДИ ЗМІНИ НА МІСЦІ ---")

setX = {1, 2, 3, 4, 5}
setY = {4, 5, 6, 7, 8}

# intersection_update() – залишає тільки спільні елементи
setX_copy = setX.copy()
setX_copy.intersection_update(setY)
print(f"{setX} після intersection_update({setY}): {setX_copy}")

# difference_update() – видаляє елементи, які є в іншій множині
setX_copy = setX.copy()
setX_copy.difference_update(setY)
print(f"{setX} після difference_update({setY}): {setX_copy}")

# symmetric_difference_update() – залишає елементи, що є тільки в одній з множин
setX_copy = setX.copy()
setX_copy.symmetric_difference_update(setY)
print(f"{setX} після symmetric_difference_update({setY}): {setX_copy}")

# ============================================================
# FROZENSET - НЕЗМІННА МНОЖИНА
# ============================================================

print("\n--- FROZENSET (Незмінна множина) ---")

# frozenset – незмінна версія множини (може бути ключем словника!)
frozen = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", frozen)

# frozenset не має методів для зміни (add, remove, clear тощо)
# frozen.add(6)  # AttributeError!

# Але підтримує всі операції читання та математичні операції
print("3 є у frozenset?", 3 in frozen)
print("Об'єднання:", frozen | {5, 6, 7})

# frozenset як ключ словника
dict_with_frozenset_keys = {
    frozenset([1, 2]): "Група A",
    frozenset([3, 4]): "Група B"
}
print("Словник з frozenset ключами:", dict_with_frozenset_keys)

# ============================================================
# ПРАКТИЧНІ ПРИКЛАДИ
# ============================================================

print("\n--- ПРАКТИЧНІ ПРИКЛАДИ ---")

# 1. Видалення дублікатів зі списку
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
unique = list(set(numbers))
print(f"Список: {numbers}")
print(f"Без дублікатів: {unique}")

# 2. Знаходження унікальних слів у тексті
text = "hello world hello python python world"
unique_words = set(text.split())
print(f"\nТекст: {text}")
print(f"Унікальні слова: {unique_words}")

# 3. Знаходження спільних інтересів
alice_hobbies = {"читання", "плавання", "малювання", "програмування"}
bob_hobbies = {"футбол", "програмування", "плавання", "музика"}
common_hobbies = alice_hobbies & bob_hobbies
print(f"\nСпільні хобі Alice і Bob: {common_hobbies}")

# 4. Знаходження різниці (що є у однієї особи, але немає у іншої)
only_alice = alice_hobbies - bob_hobbies
only_bob = bob_hobbies - alice_hobbies
print(f"Тільки у Alice: {only_alice}")
print(f"Тільки у Bob: {only_bob}")

# 5. Перевірка чи всі елементи одного списку є в іншому
required_skills = {"Python", "SQL", "Git"}
candidate_skills = {"Python", "JavaScript", "SQL", "Git", "Docker"}
has_all_skills = required_skills.issubset(candidate_skills)
print(f"\nНеобхідні навички: {required_skills}")
print(f"Навички кандидата: {candidate_skills}")
print(f"Кандидат має всі необхідні навички? {has_all_skills}")

print("\n✓ Множини - потужний інструмент для роботи з унікальними елементами!")

