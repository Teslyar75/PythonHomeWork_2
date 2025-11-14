"""
ОБЛАСТІ ВИДИМОСТІ (SCOPE) та ЗАМИКАННЯ (CLOSURES)

LEGB Rule - порядок пошуку змінних у Python:
- L (Local) - локальна область видимості функції
- E (Enclosing) - область видимості зовнішньої функції (для вкладених функцій)
- G (Global) - глобальна область видимості модуля
- B (Built-in) - вбудовані імена Python (print, len, etc.)

Замикання (Closure) - це функція, яка запам'ятовує значення зі своєї зовнішньої області видимості,
навіть якщо зовнішня функція вже завершила виконання.
"""

# ============================================================
# ОБЛАСТІ ВИДИМОСТІ (SCOPE)
# ============================================================

print("=== ОБЛАСТІ ВИДИМОСТІ ===\n")

# Глобальна змінна
x = 10
print(f"Глобальна x = {x}")

# Локальна змінна (не впливає на глобальну)
def sample():
    x = 5  # Локальна x (затінює глобальну)
    print(f"Локальна x всередині sample() = {x}")

sample()
print(f"Глобальна x після sample() = {x}")  # Глобальна x не змінилась

# Використання global для зміни глобальної змінної
def change_global():
    global x  # Вказуємо, що працюємо з глобальною x
    x = 20
    print(f"Змінено глобальну x на {x}")

change_global()
print(f"Глобальна x після change_global() = {x}")

# ============================================================
# NONLOCAL - для вкладених функцій
# ============================================================

print("\n" + "="*50)
print("=== NONLOCAL ===\n")

def outer_func():
    x = 10  # Зовнішня (enclosing) змінна
    print(f"Outer x = {x}")
    
    def inner_func():
        nonlocal x  # Посилаємось на x з зовнішньої функції
        x = 20      # Змінюємо x зовнішньої функції
        print(f"Inner x (після зміни) = {x}")
    
    inner_func()
    print(f"Outer x (після inner_func) = {x}")  # x змінилась!

outer_func()

# Приклад без nonlocal (створюється нова локальна змінна)
print("\n--- Без nonlocal ---")

def outer_func2():
    x = 10
    print(f"Outer x = {x}")
    
    def inner_func2():
        x = 20  # Створюється нова локальна змінна
        print(f"Inner x = {x}")
    
    inner_func2()
    print(f"Outer x (не змінилась) = {x}")

outer_func2()

# ============================================================
# ЗАМИКАННЯ (CLOSURES) - Основи
# ============================================================

print("\n" + "="*50)
print("=== ЗАМИКАННЯ (CLOSURES) ===\n")

# Замикання - функція, яка "запам'ятовує" змінні зовнішньої функції
def make_multiplier(n):
    """Повертає функцію, яка множить на n"""
    def multiplier(x):
        return x * n  # n запам'ятовується з зовнішньої функції!
    return multiplier

# Створюємо функції-множники
multiply_by_3 = make_multiplier(3)
multiply_by_5 = make_multiplier(5)
multiply_by_10 = make_multiplier(10)

# Кожна функція "запам'ятала" своє значення n
print(f"multiply_by_3(10) = {multiply_by_3(10)}")   # 30
print(f"multiply_by_5(10) = {multiply_by_5(10)}")   # 50
print(f"multiply_by_10(10) = {multiply_by_10(10)}") # 100

# ============================================================
# ЗАМИКАННЯ З ЗМІННИМИ СТАНАМИ
# ============================================================

print("\n=== ЗАМИКАННЯ ЗІ СТАНОМ ===\n")

# Лічильник з використанням замикання
def make_counter(start=0):
    """Створює лічильник, який починається з start"""
    count = start  # Ця змінна "живе" в замиканні
    
    def counter():
        nonlocal count  # Змінюємо змінну зовнішньої функції
        count += 1
        return count
    
    return counter

# Створюємо незалежні лічильники
counter1 = make_counter(0)
counter2 = make_counter(100)

print("Counter 1:", counter1())  # 1
print("Counter 1:", counter1())  # 2
print("Counter 1:", counter1())  # 3

print("Counter 2:", counter2())  # 101
print("Counter 2:", counter2())  # 102

print("Counter 1:", counter1())  # 4 (незалежний від counter2!)

# Зворотній лічильник
def outer(max_value):
    """Створює зворотній лічильник від max_value"""
    def inner():
        nonlocal max_value
        max_value -= 1
        print(f"Count: {max_value}")
    return inner

countdown = outer(10)
print("\nЗворотній відлік:")
countdown()  # 9
countdown()  # 8
countdown()  # 7
countdown()  # 6
countdown()  # 5

# ============================================================
# ЗАМИКАННЯ З ДЕКІЛЬКОМА ФУНКЦІЯМИ
# ============================================================

print("\n" + "="*50)
print("=== ЗАМИКАННЯ З ДЕКІЛЬКОМА ФУНКЦІЯМИ ===\n")

# Створення "об'єкта" через замикання
def make_storage():
    """Створює сховище з приватними даними"""
    data = []  # Приватна змінна
    
    # Функції для роботи зі сховищем
    def push(value):
        data.append(value)
        return f"Додано: {value}"
    
    def show():
        return f"Storage: {data}"
    
    def remove(item):
        if item in data:
            data.remove(item)
            return f"Видалено: {item}"
        return f"Елемент {item} не знайдено"
    
    def size():
        return len(data)
    
    # Повертаємо словник функцій
    return {
        'push': push,
        'show': show,
        'remove': remove,
        'size': size
    }

# Створюємо сховище
storage = make_storage()

print(storage['push']("Hello"))
print(storage['push']("World"))
print(storage['push']("Python"))
print(storage['show']())
print(f"Розмір: {storage['size']()}")
print(storage['remove']("World"))
print(storage['show']())

# Альтернативний спосіб (повернення кортежу функцій)
def make_storage2():
    data = []
    
    push_data = lambda value: data.append(value)
    print_data = lambda: print("Storage:", data)
    
    def remove_item(item):
        if item in data:
            data.remove(item)
    
    return (push_data, print_data, remove_item)

print("\n--- Альтернативний спосіб ---")
push, show, remove = make_storage2()

push("Apple")
push("Banana")
show()
remove("Apple")
show()

# ============================================================
# ПРАКТИЧНІ ПРИКЛАДИ ЗАМИКАНЬ
# ============================================================

print("\n" + "="*50)
print("=== ПРАКТИЧНІ ПРИКЛАДИ ===\n")

# 1. Генератор HTML-тегів
def make_tag(tag):
    """Створює функцію для генерації HTML-тегу"""
    def wrapper(content):
        return f"<{tag}>{content}</{tag}>"
    return wrapper

h1 = make_tag("h1")
p = make_tag("p")
div = make_tag("div")

print("HTML теги:")
print(h1("Заголовок"))
print(p("Параграф тексту"))
print(div("Контент div"))

# 2. Створення функцій-валідаторів
def make_validator(min_value, max_value):
    """Створює функцію-валідатор для діапазону"""
    def validate(value):
        if value < min_value:
            return f"Занадто мало! Мінімум: {min_value}"
        elif value > max_value:
            return f"Занадто багато! Максимум: {max_value}"
        else:
            return "OK"
    return validate

age_validator = make_validator(18, 100)
percentage_validator = make_validator(0, 100)

print("\nВалідація віку:")
print(f"15: {age_validator(15)}")
print(f"25: {age_validator(25)}")
print(f"150: {age_validator(150)}")

print("\nВалідація відсотків:")
print(f"50: {percentage_validator(50)}")
print(f"101: {percentage_validator(101)}")

# 3. Калькулятор з історією
def make_calculator():
    """Створює калькулятор з історією операцій"""
    history = []
    
    def add(a, b):
        result = a + b
        history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(a, b):
        result = a - b
        history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(a, b):
        result = a * b
        history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history():
        return history.copy()
    
    def clear_history():
        history.clear()
    
    return {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'history': get_history,
        'clear': clear_history
    }

print("\n--- Калькулятор з історією ---")
calc = make_calculator()

print(f"5 + 3 = {calc['add'](5, 3)}")
print(f"10 - 4 = {calc['subtract'](10, 4)}")
print(f"7 * 6 = {calc['multiply'](7, 6)}")

print("\nІсторія операцій:")
for operation in calc['history']():
    print(f"  {operation}")

# 4. Обмеження частоти викликів (Rate Limiter)
import time

def make_rate_limiter(max_calls, time_period):
    """Створює обмежувач частоти викликів функції"""
    calls = []
    
    def rate_limited_function(func):
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            
            # Видаляємо старі виклики
            calls = [call_time for call_time in calls if now - call_time < time_period]
            
            if len(calls) >= max_calls:
                return f"Перевищено ліміт! Максимум {max_calls} викликів за {time_period} секунд"
            
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return rate_limited_function

@make_rate_limiter(3, 5)  # Максимум 3 виклики за 5 секунд
def send_message(msg):
    return f"Відправлено: {msg}"

print("\n--- Rate Limiter ---")
print(send_message("Повідомлення 1"))
print(send_message("Повідомлення 2"))
print(send_message("Повідомлення 3"))
print(send_message("Повідомлення 4"))  # Має бути відхилено

# ============================================================
# РІЗНИЦЯ МІЖ GLOBAL, NONLOCAL та ЗВИЧАЙНИМ ДОСТУПОМ
# ============================================================

print("\n" + "="*50)
print("=== GLOBAL vs NONLOCAL vs ЗВИЧАЙНИЙ ДОСТУП ===\n")

# Для змінних об'єктів (list, dict) можна викликати методи без global/nonlocal
data = ["Hello"]

def func():
    # Для списків не потрібен global, якщо ми НЕ перепризначаємо змінну
    data.append("World")  # Модифікація об'єкта - працює
    print("data всередині func():", data)

func()
print("data після func():", data)  # Змінилась!

# Але перепризначення вимагає global
def func2():
    global data
    data = ["New", "List"]  # Перепризначення змінної
    print("data всередині func2():", data)

func2()
print("data після func2():", data)

# ============================================================
# ДЕКОРАТОРИ (як приклад замикань)
# ============================================================

print("\n" + "="*50)
print("=== ДЕКОРАТОРИ (ПРИКЛАД ЗАМИКАНЬ) ===\n")

# Декоратор - це функція, яка приймає функцію і повертає нову функцію
def logger(func):
    """Декоратор для логування викликів функції"""
    def wrapper(*args, **kwargs):
        print(f"📝 Виклик функції: {func.__name__}")
        print(f"   Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"   Результат: {result}")
        return result
    return wrapper

@logger  # Еквівалентно: greet = logger(greet)
def greet(name):
    return f"Привіт, {name}!"

@logger
def add(a, b):
    return a + b

print("Виклик декорованих функцій:\n")
greet("Іван")
print()
add(5, 3)

# Декоратор з параметрами
def repeat(times):
    """Декоратор для повторення виконання функції"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    return "Hello!"

print("\n--- Декоратор з параметрами ---")
print(say_hello())

print("\n✓ Замикання - потужний механізм для інкапсуляції стану та створення декораторів!")