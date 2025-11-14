"""
ДОМАШНЄ ЗАВДАННЯ 1 - РІШЕННЯ
Python Web Development Course

Всі 22 завдання з детальними коментарями та прикладами
"""

print("="*80)
print("ДОМАШНЄ ЗАВДАННЯ 1 - РІШЕННЯ")
print("="*80)

# ============================================================================
# ЗАВДАННЯ 1: Підрахунок кількості цифр у числі
# ============================================================================

def count_digits(number):
    """
    Підраховує кількість цифр у числі.
    
    Args:
        number: число (int або float)
    
    Returns:
        int: кількість цифр
    """
    # Перетворюємо на рядок, прибираємо мінус і крапку, рахуємо довжину
    return len(str(abs(number)).replace('.', ''))
# abs() — це вбудована функція Python, яка повертає абсолютне значення числа, 
# тобто відкидає знак мінус.
# 
# abs(x)
# Параметр x може бути як цілим (int), так і дійсним (float) числом.
#
# Приклади:
# abs(-5)      --> 5
# abs(10)      --> 10
# abs(-3.14)   --> 3.14
# 
# У контексті функції count_digits ми використовуємо abs(number), 
# щоб "відкинути" можливий мінус перед числом. 
# Це дозволяє однаково рахувати кількість цифр як у додатних, 
# так і у від’ємних чисел.


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 1: Підрахунок цифр у числі")
print("="*80)

print(f"count_digits(12345) = {count_digits(12345)}")           # 5
print(f"count_digits(-9876) = {count_digits(-9876)}")           # 4
print(f"count_digits(0) = {count_digits(0)}")                   # 1
print(f"count_digits(123.45) = {count_digits(123.45)}")         # 5


# ============================================================================
# ЗАВДАННЯ 2: Підрахунок повторень слів у рядку
# ============================================================================

def count_words(text):
    """
    Підраховує кількість повторень кожного слова в рядку.
    Ігнорує коми, крапки та інші розділові знаки.
    
    Args:
        text: вхідний рядок
    
    Returns:
        dict: словник {слово: кількість}
    """
    import string
    
    # Видаляємо пунктуацію
    translator = str.maketrans('', '', string.punctuation)
    # str.maketrans(from_string, to_string) - функція, яка 
    # створює словник для перетворення символів.
    # from_string - рядок символів, які потрібно замінити.
    # to_string - рядок символів, на які потрібно замінити.
    #
    # Приклади:
    # str.maketrans('a', 'b') --> {'a': 'b'}
    # str.maketrans('abc', '123') --> {'a': '1', 'b': '2', 'c': '3'}
    #
    # У контексті функції count_words ми використовуємо 
    # str.maketrans('', '', string.punctuation), 
    # щоб видалити всі розділові знаки.
    #
    # string.punctuation - рядок символів, які є розділовими знаками.
    #
    # Приклади:
    # string.punctuation --> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    #
    # У контексті функції count_words ми використовуємо 
    # string.punctuation, щоб видалити всі розділові знаки.
    clean_text = text.translate(translator)
    # translate(table) - метод, який застосовує словник перетворення 
    # до рядка.
    # table - словник перетворення символів.
    #
    # Розбиваємо на слова та переводимо в нижній регістр
    words = clean_text.lower().split()
    # split() - метод, який розбиває рядок на список підстрок.
    # lower() - метод, який переводить рядок в нижній регістр.
    
    # Підраховуємо повторення
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    # get(key, default) - метод, який повертає значення за ключем.
    # default - значення, яке повертається, якщо ключ не знайдено.
    # default = 0, якщо ключ не знайдено, то повертається 0.
    #
    # Приклади:
    # word_count.get('hello', 0) --> 0
    # word_count.get('hello', 1) --> 1
    # word_count.get('world', 0) --> 0
    # word_count.get('world', 1) --> 1
    #
    # У контексті функції count_words ми використовуємо 
    # word_count.get(word, 0), щоб отримати кількість повторень слова.
    # якщо слово не знайдено, то повертається 0.
    #
    # Приклади:
    # word_count.get('hello', 0) --> 0
    # word_count.get('hello', 1) --> 1
    # word_count.get('world', 0) --> 0
    # word_count.get('world', 1) --> 1
    #
    # У контексті функції count_words ми використовуємо 
    # word_count.get(word, 0), щоб отримати кількість повторень слова.
    return word_count


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 2: Підрахунок повторень слів")
print("="*80)

sample_text = "Hello, world! Hello Python. Python is great, Python is fun."
word_counts = count_words(sample_text)
print(f"Текст: {sample_text}")
print("\nРезультат:")
for word, count in sorted(word_counts.items()):
    print(f"  {word}: {count}")


# ============================================================================
# ЗАВДАННЯ 3: Фільтрація парних чисел та їх квадрати
# ============================================================================

def filter_and_square_evens(numbers):
    """
    Фільтрує парні числа і повертає їх квадрати.
    
    Args:
        numbers: список цілих чисел
    
    Returns:
        list: список квадратів парних чисел
    """
    # Фільтруємо парні числа
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    # filter(function, iterable) - функція, яка фільтрує елементи iterable.
    # function - функція, яка перевіряє кожен елемент iterable.
    # iterable - ітерований об'єкт, над яким буде проводитися фільтрація.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # filter(lambda x: x % 2 == 0, numbers), щоб отримати парні числа.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # filter(lambda x: x % 2 == 0, numbers), щоб отримати парні числа.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # filter(lambda x: x % 2 == 0, numbers), щоб отримати парні числа.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # filter(lambda x: x % 2 == 0, numbers), щоб отримати парні числа.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # filter(lambda x: x % 2 == 0, numbers), щоб отримати парні числа.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # filter(lambda x: x % 2 == 0, numbers), щоб отримати парні числа.
    #
    # Приклади:
    # filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) --> [2, 4]
    # filter(lambda x: x > 5, [1, 2, 3, 4, 5]) --> []
    #
    # У контексті функції filter_and_square_evens ми використовуємо 
    # Застосовуємо map для отримання квадратів
    squared = map(lambda x: x ** 2, even_numbers)
    
    return list(squared)


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 3: Квадрати парних чисел")
print("="*80)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_and_square_evens(numbers)
print(f"Вхідний список: {numbers}")
print(f"Парні числа: {[x for x in numbers if x % 2 == 0]}")
print(f"Квадрати парних: {result}")


# ============================================================================
# ЗАВДАННЯ 4: Студенти та оцінки
# ============================================================================

def analyze_students(students_dict):
    """
    Аналізує оцінки студентів: середній бал та студент з максимальною оцінкою.
    
    Args:
        students_dict: словник {студент: [оцінки]}
    
    Returns:
        tuple: (середні_бали, студент_з_макс_оцінкою)
    """
    # Середні бали
    # Створюємо новий словник, де для кожного студента обчислюємо середній бал
    average_grades = {}
    for student, grades in students_dict.items():
        # sum(grades) - сума всіх оцінок студента
        # len(grades) - кількість оцінок
        # Середній бал = сума / кількість
        average_grades[student] = sum(grades) / len(grades)
    
    # Студент з максимальною оцінкою
    # Ініціалізуємо змінні для пошуку максимуму
    max_grade = 0
    best_student = None
    
    # Проходимо по всіх студентах
    for student, grades in students_dict.items():
        # max(grades) - знаходимо найвищу оцінку студента
        student_max = max(grades)
        # Якщо ця оцінка більша за поточний максимум
        if student_max > max_grade:
            max_grade = student_max      # Оновлюємо максимальну оцінку
            best_student = student        # Запам'ятовуємо студента
    
    # Повертаємо кортеж: (словник середніх балів, (кращий студент, його макс. оцінка))
    return average_grades, (best_student, max_grade)


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 4: Аналіз студентів")
print("="*80)

students = {
    "Іван": [85, 90, 78, 92],
    "Марія": [95, 88, 91, 94],
    "Петро": [70, 75, 80, 72],
    "Анна": [98, 96, 100, 97]
}

averages, (best_student, max_grade) = analyze_students(students)

print("Середні бали:")
for student, avg in averages.items():
    print(f"  {student}: {avg:.2f}")

print(f"\nСтудент з максимальною оцінкою: {best_student} (оцінка: {max_grade})")


# ============================================================================
# ЗАВДАННЯ 5: Підрахунок символів у рядку
# ============================================================================

def count_characters(text):
    """
    Підраховує кількість повторень кожного символу в рядку.
    
    Args:
        text: вхідний рядок
    
    Returns:
        dict: словник {символ: кількість}
    """
    # Створюємо порожній словник для підрахунку символів
    char_count = {}
    
    # Проходимо по кожному символу в рядку
    for char in text:
        # get(char, 0) - повертає поточну кількість символу (або 0, якщо символу немає)
        # +1 - збільшуємо лічильник на 1
        # Ця техніка дозволяє безпечно працювати з словником без перевірки наявності ключа
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count
    
# Альтернативний спосіб через collections.Counter:
# from collections import Counter
# return dict(Counter(text))


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 5: Підрахунок символів")
print("="*80)

text = "Hello, World!"
char_counts = count_characters(text)
print(f"Текст: '{text}'")
print("Результат:")
for char, count in sorted(char_counts.items()):
    print(f"  '{char}': {count}")


# ============================================================================
# ЗАВДАННЯ 6: Фільтрація чисел з кортежу
# ============================================================================

def filter_numbers_from_tuple(data_tuple):
    """
    Повертає новий кортеж, що містить лише числа.
    
    Args:
        data_tuple: кортеж із різних типів даних
    
    Returns:
        tuple: кортеж лише з чисел
    """
    # Фільтруємо числа (int та float)
    # Ми створюємо новий кортеж із тих елементів data_tuple, 
    # які є числами.
    # isinstance(item, (int, float)) — перевіряє, 
    # чи є елемент цілим чи дійсним числом (int або float).
    # Додатково ми додаємо перевірку not isinstance(item, bool),
    #  бо у Python тип bool є підтипом int
    # (наприклад, isinstance(True, int) дає True), 
    # але логічні значення нам не підходять як числа для цієї задачі.
    # Тобто, ми не хочемо, щоб True чи False потрапили у результат.
    #
    # Приклади:
    # isinstance(1, (int, float)) --> True
    # isinstance(1.0, (int, float)) --> True
    # isinstance(True, (int, float)) --> False
    # isinstance(False, (int, float)) --> False
    #
    # У контексті функції filter_numbers_from_tuple ми використовуємо 
    # isinstance(item, (int, float)) і not isinstance(item, bool),
    # щоб отримати лише числа.
    #
    # Приклади:
    # filter_numbers_from_tuple((1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)) --> (1, 3.14, 42, 7.5, 100)
    # filter_numbers_from_tuple((True, False, "hello", "world", 42, 7.5, "Python", 100)) --> (42, 7.5, 100)
    #
    # У контексті функції filter_numbers_from_tuple ми використовуємо 
    # tuple(item for item in data_tuple if isinstance(item, (int, float)) and not isinstance(item, bool)),
    # щоб отримати лише числа.
    #
    # Приклади:
    # filter_numbers_from_tuple((1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)) --> (1, 3.14, 42, 7.5, 100)
    # filter_numbers_from_tuple((True, False, "hello", "world", 42, 7.5, "Python", 100)) --> (42, 7.5, 100)
    #
    # У контексті функції filter_numbers_from_tuple ми використовуємо 
    # tuple(item for item in data_tuple if isinstance(item, (int, float)) and not isinstance(item, bool)),
    # щоб отримати лише числа.
    #
    # Приклади:
    # filter_numbers_from_tuple((1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)) --> (1, 3.14, 42, 7.5, 100)
    # filter_numbers_from_tuple((True, False, "hello", "world", 42, 7.5, "Python", 100)) --> (42, 7.5, 100)
    #
    # У контексті функції filter_numbers_from_tuple ми використовуємо 
    # tuple(item for item in data_tuple if isinstance(item, (int, float)) and not isinstance(item, bool)),
    # щоб отримати лише числа.
    #
    # Приклади:
    # filter_numbers_from_tuple((1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)) --> (1, 3.14, 42, 7.5, 100)
    # filter_numbers_from_tuple((True, False, "hello", "world", 42, 7.5, "Python", 100)) --> (42, 7.5, 100)
    #
    # У контексті функції filter_numbers_from_tuple ми використовуємо 
    # tuple(item for item in data_tuple if isinstance(item, (int, float)) and not isinstance(item, bool)),
    # щоб отримати лише числа.
    #
    # Приклади:
    # filter_numbers_from_tuple((1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)) --> (1, 3.14, 42, 7.5, 100)
    # filter_numbers_from_tuple((True, False, "hello", "world", 42, 7.5, "Python", 100)) --> (42, 7.5, 100)
    #
    # У контексті функції filter_numbers_from_tuple ми використовуємо 
    # tuple(item for item in data_tuple if isinstance(item, (int, float)) and not isinstance(item, bool)),
    # щоб отримати лише числа.
    #
    # Приклади:
    # filter_numbers_from_tuple((1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)) --> (1, 3.14, 42, 7.5, 100)
    # filter_numbers_from_tuple((True, False, "hello", "world", 42, 7.5, "Python", 100)) --> (42, 7.5, 100)
    #
    numbers = tuple(
        item
        for item in data_tuple
        if isinstance(item, (int, float))  # беремо int або float
        and not isinstance(item, bool)     # але НЕ bool
    )
    return numbers


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 6: Фільтрація чисел з кортежу")
print("="*80)

mixed_tuple = (1, "hello", 3.14, "world", 42, True, 7.5, "Python", 100)
numbers_only = filter_numbers_from_tuple(mixed_tuple)
print(f"Вхідний кортеж: {mixed_tuple}")
print(f"Тільки числа: {numbers_only}")


# ============================================================================
# ЗАВДАННЯ 7: Сортування рядків за довжиною
# ============================================================================

def sort_by_length(strings):
    """
    Сортує список рядків за довжиною.
    
    Args:
        strings: список рядків
    
    Returns:
        list: відсортований список
    """
    # sorted(iterable, key=function) - сортує елементи за результатом функції key
    # key=len - використовуємо вбудовану функцію len() як критерій сортування
    # len() повертає довжину рядка, тому рядки будуть відсортовані від коротших до довших
    #
    # Приклади:
    # sorted(["abc", "a", "ab"], key=len) --> ["a", "ab", "abc"]
    # sorted(["Python", "is", "awesome"], key=len) --> ["is", "Python", "awesome"]
    #
    # Для сортування у зворотному порядку (від довших до коротших):
    # sorted(strings, key=len, reverse=True)
    return sorted(strings, key=len)


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 7: Сортування рядків за довжиною")
print("="*80)

words = ["Python", "is", "awesome", "and", "powerful"]
sorted_words = sort_by_length(words)
print(f"Оригінал: {words}")
print(f"Відсортовано: {sorted_words}")


# ============================================================================
# ЗАВДАННЯ 8: Сортування співробітників за зарплатою
# ============================================================================

def sort_employees_by_salary(employees):
    """
    Сортує співробітників за зарплатою (від більшої до меншої).
    
    Args:
        employees: список словників з даними про співробітників
    
    Returns:
        list: відсортований список співробітників
    """
    # sorted(iterable, key=lambda, reverse=True)
    # key=lambda emp: emp['зарплата'] - для кожного співробітника (словника) 
    # беремо значення за ключем 'зарплата' і сортуємо за цим значенням
    # reverse=True - сортування у зворотному порядку (від більшої до меншої)
    #
    # Приклади:
    # sorted([{"name": "A", "salary": 50000}, {"name": "B", "salary": 60000}], 
    #        key=lambda x: x['salary']) --> [A: 50000, B: 60000]
    #
    # sorted(..., reverse=True) --> [B: 60000, A: 50000]
    return sorted(employees, key=lambda emp: emp['зарплата'], reverse=True)


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 8: Сортування співробітників")
print("="*80)

employees = [
    {"ім'я": "Іван", "посада": "Програміст", "зарплата": 50000},
    {"ім'я": "Марія", "посада": "Менеджер", "зарплата": 60000},
    {"ім'я": "Петро", "посада": "Дизайнер", "зарплата": 45000},
    {"ім'я": "Анна", "посада": "Директор", "зарплата": 80000}
]

sorted_employees = sort_employees_by_salary(employees)
print("Співробітники (за зарплатою):")
for emp in sorted_employees:
    print(f"  {emp['ім\'я']}: {emp['посада']} - {emp['зарплата']} грн")


# ============================================================================
# ЗАВДАННЯ 9: Lambda для знаходження більшого числа
# ============================================================================

# Lambda-функція для знаходження максимуму
# lambda a, b: вираз - анонімна функція з двома параметрами a та b
# a if a > b else b - тернарний оператор (умовний вираз):
#   - якщо a > b, повертає a
#   - інакше повертає b
#
# Еквівалент звичайної функції:
# def max_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# Приклади:
# max_of_two(5, 3) --> 5
# max_of_two(2, 8) --> 8
max_of_two = lambda a, b: a if a > b else b

# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 9: Lambda для максимуму")
print("="*80)

print(f"max_of_two(10, 20) = {max_of_two(10, 20)}")
print(f"max_of_two(100, 50) = {max_of_two(100, 50)}")
print(f"max_of_two(-5, -10) = {max_of_two(-5, -10)}")


# ============================================================================
# ЗАВДАННЯ 10: Унікальні елементи у множину
# ============================================================================

def get_unique_elements(items_list):
    """
    Знаходить усі унікальні елементи в списку.
    
    Args:
        items_list: список елементів
    
    Returns:
        set: множина унікальних елементів
    """
    # set(iterable) - перетворює будь-яку послідовність на множину
    # Множина (set) автоматично видаляє всі дублікати
    # Це найпростіший спосіб отримати унікальні елементи
    #
    # Приклади:
    # set([1, 2, 2, 3, 3, 3]) --> {1, 2, 3}
    # set("hello") --> {'h', 'e', 'l', 'o'}
    #
    # Щоб зберегти порядок елементів (з Python 3.7+):
    # list(dict.fromkeys(items_list))
    return set(items_list)


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 10: Унікальні елементи")
print("="*80)

numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4, 7]
unique = get_unique_elements(numbers)
print(f"Список: {numbers}")
print(f"Унікальні: {sorted(unique)}")


# ============================================================================
# ЗАВДАННЯ 11: Словник квадратів та їх сума
# ============================================================================

def create_squares_dict_and_sum():
    """
    Створює словник квадратів чисел 1-10 та обчислює суму значень.
    
    Returns:
        tuple: (словник, сума)
    """
    # Dict comprehension: {ключ: значення for елемент in послідовність}
    # {x: x**2 for x in range(1, 11)} створює словник:
    # {1: 1, 2: 4, 3: 9, 4: 16, ..., 10: 100}
    squares_dict = {x: x**2 for x in range(1, 11)}
    
    # dict.values() - повертає всі значення словника
    # sum() - обчислює суму всіх значень
    # Сума квадратів від 1 до 10: 1+4+9+16+25+36+49+64+81+100 = 385
    total_sum = sum(squares_dict.values())
    
    return squares_dict, total_sum


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 11: Словник квадратів")
print("="*80)

squares, total = create_squares_dict_and_sum()
print("Словник квадратів:")
print(squares)
print(f"\nСума всіх значень: {total}")


# ============================================================================
# ЗАВДАННЯ 12: Числа більші за 10 і парні
# ============================================================================

def filter_greater_than_10_and_even(numbers):
    """
    Фільтрує числа, які більші за 10 і парні.
    
    Args:
        numbers: список чисел
    
    Returns:
        list: відфільтрований список
    """
    # List comprehension з умовою: [елемент for елемент in список if умова]
    # num > 10 - число повинно бути більше 10
    # and num % 2 == 0 - І (and) число повинно бути парним (остача від ділення на 2 дорівнює 0)
    #
    # Альтернативний спосіб через filter():
    # return list(filter(lambda num: num > 10 and num % 2 == 0, numbers))
    return [num for num in numbers if num > 10 and num % 2 == 0]


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 12: Числа > 10 та парні")
print("="*80)

numbers = [5, 12, 8, 15, 20, 7, 18, 11, 24, 9, 16]
filtered = filter_greater_than_10_and_even(numbers)
print(f"Вхідний список: {numbers}")
print(f"Результат: {filtered}")


# ============================================================================
# ЗАВДАННЯ 13: Сума чисел у кортежі
# ============================================================================

def sum_tuple(numbers_tuple):
    """
    Знаходить суму всіх чисел у кортежі.
    
    Args:
        numbers_tuple: кортеж чисел
    
    Returns:
        int/float: сума чисел
    """
    return sum(numbers_tuple)


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 13: Сума чисел у кортежі")
print("="*80)

numbers_tuple = (10, 20, 30, 40, 50)
total = sum_tuple(numbers_tuple)
print(f"Кортеж: {numbers_tuple}")
print(f"Сума: {total}")


# ============================================================================
# ЗАВДАННЯ 14: Lambda перевірка додатного числа
# ============================================================================

# Lambda для перевірки додатного числа
# lambda x: x > 0 - повертає True, якщо число додатне, інакше False
# Еквівалент:
# def is_positive(x):
#     return x > 0
#
# Приклади:
# is_positive(5) --> True
# is_positive(-3) --> False
# is_positive(0) --> False (нуль не є додатним числом)
is_positive = lambda x: x > 0

# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 14: Перевірка додатного числа")
print("="*80)

print(f"is_positive(10) = {is_positive(10)}")
print(f"is_positive(-5) = {is_positive(-5)}")
print(f"is_positive(0) = {is_positive(0)}")


# ============================================================================
# ЗАВДАННЯ 15: Люди старші за певний вік
# ============================================================================

def get_people_older_than(people_dict, age_limit):
    """
    Повертає список імен людей, старших за вказаний вік.
    
    Args:
        people_dict: словник {ім'я: вік}
        age_limit: граничний вік
    
    Returns:
        list: список імен
    """
    # List comprehension з розпакуванням словника
    # people_dict.items() - повертає пари (ім'я, вік)
    # for name, age in ... - розпаковуємо кожну пару
    # if age > age_limit - фільтруємо тільки тих, хто старший за граничний вік
    # name - зберігаємо тільки імена
    #
    # Альтернативний спосіб:
    # return [name for name in people_dict if people_dict[name] > age_limit]
    return [name for name, age in people_dict.items() if age > age_limit]


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 15: Люди старші за вік")
print("="*80)

people = {
    "Іван": 25,
    "Марія": 32,
    "Петро": 18,
    "Анна": 40,
    "Олег": 28
}

age_limit = 27
older_people = get_people_older_than(people, age_limit)
print(f"Всі люди: {people}")
print(f"Старші за {age_limit}: {older_people}")


# ============================================================================
# ЗАВДАННЯ 16: Максимум та мінімум у кортежі
# ============================================================================

def find_min_max(numbers_tuple):
    """
    Знаходить мінімальне та максимальне значення в кортежі.
    
    Args:
        numbers_tuple: кортеж чисел
    
    Returns:
        tuple: (мінімум, максимум)
    """
    return (min(numbers_tuple), max(numbers_tuple))


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 16: Мін/Макс у кортежі")
print("="*80)

numbers_tuple = (15, 3, 42, 7, 28, 91, 5, 63)
min_val, max_val = find_min_max(numbers_tuple)
print(f"Кортеж: {numbers_tuple}")
print(f"Мінімум: {min_val}")
print(f"Максимум: {max_val}")


# ============================================================================
# ЗАВДАННЯ 17: Числа, що діляться на 3
# ============================================================================

def filter_divisible_by_3(numbers):
    """
    Знаходить усі числа, які діляться на 3.
    
    Args:
        numbers: список чисел
    
    Returns:
        list: відфільтрований список
    """
    return list(filter(lambda x: x % 3 == 0, numbers))


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 17: Числа, що діляться на 3")
print("="*80)

numbers = [1, 3, 5, 6, 9, 12, 15, 18, 20, 21, 25, 27]
divisible_by_3 = filter_divisible_by_3(numbers)
print(f"Вхідний список: {numbers}")
print(f"Діляться на 3: {divisible_by_3}")


# ============================================================================
# ЗАВДАННЯ 18: Рядок у список кортежів (символ, індекс)
# ============================================================================

def string_to_indexed_tuples(text):
    """
    Перетворює рядок у список кортежів (символ, індекс).
    
    Args:
        text: вхідний рядок
    
    Returns:
        list: список кортежів
    """
    # enumerate(iterable) - повертає пари (індекс, елемент)
    # for index, char in enumerate(text) - розпаковуємо кожну пару
    # (char, index) - створюємо кортеж з символу та індексу
    #
    # Приклади:
    # string_to_indexed_tuples("abc") --> [('a', 0), ('b', 1), ('c', 2)]
    # string_to_indexed_tuples("Hi") --> [('H', 0), ('i', 1)]
    #
    # enumerate() дуже корисна для отримання індексу під час ітерації
    return [(char, index) for index, char in enumerate(text)]


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 18: Рядок → кортежі (символ, індекс)")
print("="*80)

text = "Python"
indexed = string_to_indexed_tuples(text)
print(f"Рядок: '{text}'")
print(f"Результат: {indexed}")


# ============================================================================
# ЗАВДАННЯ 19: Генератор чисел, що діляться на 3 або 5
# ============================================================================

def divisible_by_3_or_5(limit):
    """
    Генератор чисел, що діляться на 3 або 5, від 1 до limit.
    
    Args:
        limit: максимальне число
    
    Yields:
        int: числа, що діляться на 3 або 5
    """
    # Генератор - це функція, яка використовує yield замість return
    # yield "заморожує" функцію і повертає значення
    # При наступному виклику next() функція продовжує з того ж місця
    #
    # Переваги генераторів:
    # - Ефективність пам'яті (не зберігають всі значення одразу)
    # - Можливість роботи з нескінченними послідовностями
    #
    # Приклади використання:
    # gen = divisible_by_3_or_5(10)
    # next(gen) --> 3
    # next(gen) --> 5
    # next(gen) --> 6
    # list(divisible_by_3_or_5(15)) --> [3, 5, 6, 9, 10, 12, 15]
    for num in range(1, limit + 1):
        # num % 3 == 0 - ділиться на 3
        # or num % 5 == 0 - АБО ділиться на 5
        if num % 3 == 0 or num % 5 == 0:
            yield num  # Повертаємо число і "заморожуємо" функцію


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 19: Генератор чисел (÷3 або ÷5)")
print("="*80)

limit = 30
print(f"Числа від 1 до {limit}, що діляться на 3 або 5:")
print(list(divisible_by_3_or_5(limit)))


# ============================================================================
# ЗАВДАННЯ 20: Замикання з обмеженням викликів
# ============================================================================

def limit_calls(func, max_calls):
    """
    Замикання, яке обмежує кількість викликів функції.
    
    Args:
        func: функція для виклику
        max_calls: максимальна кількість викликів
    
    Returns:
        function: обгорнута функція
    """
    # Замикання (closure) - це функція, яка "запам'ятовує" змінні
    # з зовнішньої області видимості
    call_count = 0  # Ця змінна "живе" в замиканні
    
    def wrapper(*args, **kwargs):
        nonlocal call_count  # Дозволяє змінювати змінну зовнішньої функції
        
        # Перевіряємо, чи не перевищено ліміт викликів
        if call_count >= max_calls:
            return f"❌ ПОМИЛКА: Перевищено ліміт викликів ({max_calls})"
        
        call_count += 1  # Збільшуємо лічильник
        return func(*args, **kwargs)  # Викликаємо оригінальну функцію
    
    return wrapper  # Повертаємо функцію-обгортку
    
# Це приклад декоратора - шаблону проектування для розширення
# функціональності без зміни оригінального коду


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 20: Замикання з обмеженням викликів")
print("="*80)

def greet(name):
    return f"Привіт, {name}!"

limited_greet = limit_calls(greet, 3)

print(limited_greet("Іван"))   # Виклик 1
print(limited_greet("Марія"))  # Виклик 2
print(limited_greet("Петро"))  # Виклик 3
print(limited_greet("Анна"))   # Виклик 4 - помилка!


# ============================================================================
# ЗАВДАННЯ 21: Замикання для перевірки належності списку
# ============================================================================

def make_membership_checker(numbers_list):
    """
    Замикання, яке перевіряє належність числа до списку.
    
    Args:
        numbers_list: список чисел
    
    Returns:
        function: функція перевірки
    """
    # Внутрішня функція "запам'ятовує" numbers_list з зовнішньої функції
    def checker(number):
        # Перевіряємо, чи є число в списку
        # Оператор 'in' працює дуже швидко з множинами (set)
        # Для оптимізації можна було б використати: set(numbers_list)
        return number in numbers_list
    
    return checker
    
# Використання замикань дозволяє створювати "персоналізовані" функції
# Кожна повернута функція "пам'ятає" свій власний список чисел


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 21: Замикання для перевірки належності")
print("="*80)

allowed_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
is_allowed = make_membership_checker(allowed_numbers)

print(f"Дозволені числа: {allowed_numbers}")
print(f"is_allowed(5) = {is_allowed(5)}")    # True
print(f"is_allowed(10) = {is_allowed(10)}")  # False
print(f"is_allowed(13) = {is_allowed(13)}")  # True


# ============================================================================
# ЗАВДАННЯ 22: Замикання для форматування рядка
# ============================================================================

def make_formatter(template):
    """
    Замикання, яке форматує рядки за шаблоном.
    
    Args:
        template: шаблон рядка (з плейсхолдерами)
    
    Returns:
        function: функція форматування
    """
    # Внутрішня функція "запам'ятовує" template з зовнішньої функції
    def formatter(**kwargs):
        # **kwargs - дозволяє передати довільну кількість іменованих аргументів
        # template.format(**kwargs) - підставляє значення в плейсхолдери шаблону
        #
        # Приклад:
        # template = "Привіт, {name}!"
        # formatter(name="Іван") --> "Привіт, Іван!"
        return template.format(**kwargs)
    
    return formatter
    
# Це дуже корисний патерн для створення спеціалізованих функцій форматування
# Замість створення багатьох схожих функцій, ми створюємо одну фабрику,
# яка генерує потрібні нам функції з різними шаблонами


# Приклади використання
print("\n" + "="*80)
print("ЗАВДАННЯ 22: Замикання для форматування")
print("="*80)

# Різні шаблони
email_formatter = make_formatter("Пошта: {email}, Тема: {subject}")
person_formatter = make_formatter("Ім'я: {name}, Вік: {age}, Місто: {city}")
greeting_formatter = make_formatter("Вітаю, {name}! Сьогодні {day}, і погода {weather}.")

print("1. Email шаблон:")
print(email_formatter(email="user@example.com", subject="Важливо!"))

print("\n2. Персона шаблон:")
print(person_formatter(name="Іван", age=25, city="Київ"))

print("\n3. Привітання шаблон:")
print(greeting_formatter(name="Марія", day="понеділок", weather="сонячна"))


# ============================================================================
# ФІНАЛ
# ============================================================================

print("\n" + "="*80)
print("🎉 ВСЬОГО ЗАВДАНЬ ВИКОНАНО: 22/22")
print("="*80)
print("\n📚 Використані концепції:")
print("   • Функції та lambda-вирази")
print("   • Списки, кортежі, множини, словники")
print("   • List/Dict comprehensions")
print("   • map(), filter(), sorted()")
print("   • Генератори (yield)")
print("   • Замикання (closures)")
print("="*80)

