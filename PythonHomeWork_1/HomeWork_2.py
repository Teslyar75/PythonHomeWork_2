from functools import partial  # Імпорт для створення частково застосованих функцій
import json  # Імпорт для роботи з JSON файлами
import os  # Імпорт для роботи з файловою системою

"""
1. Створіть клас Book, який має такі властивості:
- назва книги
- автор книги
- кількість сторінок
Додайте методи:
-аксесори(властивості)
-метод, який виводить інформацію про книгу
-метод, який повертає True, якщо кількість сторінок більша за 300, інакше False.
"""
class Book:  # Оголошення класу Book (Книга)
    def __init__(self, title, author, pages):   # Метод ініціалізації (конструктор), приймає назву, автора і кількість сторінок
        self.title = title      # Встановлює атрибут (через setter) назву книги
        self.author = author    # Встановлює атрибут (через setter) автора книги
        self.pages = pages      # Встановлює атрибут кількість сторінок (через setter)
    @property
    def title(self):            # Гетер для властивості title (назва)
        return self._title      # Повертає значення "приватного" атрибута _title
    @title.setter
    def title(self, value):     # Сетер для властивості title (назва)
        self._title = value     # Встановлює значення "приватного" атрибута _title
    @property
    def author(self):           # Гетер для властивості author (автор)
        return self._author     # Повертає значення "приватного" атрибута _author
    @author.setter
    def author(self, value):    # Сетер для властивості author (автор)
        self._author = value    # Встановлює значення "приватного" атрибута _author
    @property
    def pages(self):            # Гетер для властивості pages (кількість сторінок)
        return self._pages      # Повертає значення "приватного" атрибута _pages
    @pages.setter
    def pages(self, value):     # Сетер для властивості pages (кількість сторінок)
        self._pages = value     # Встановлює значення "приватного" атрибута _pages
    def display_info(self):     # Метод для виведення інформації про книгу
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Кількість сторінок: {self.pages}")
    def is_long_book(self):     # Метод, який повертає True, якщо кількість сторінок більша за 300
        return self.pages > 300  # Повертає True, якщо pages > 300, інакше False


"""2. Напишіть клас-декоратор, який кешує результати методів класу, 
використовуючи аргументи методу як ключ для кешу. Якщо метод викликається 
з тими ж аргументами, повертайте вже обчислений результат з кешу. 
Якщо ні — обчислюйте і зберігайте результат у кеш.
"""
class CacheMethod:  # Клас-декоратор для кешування результатів методів
    def __init__(self, func):  # Ініціалізація декоратора, приймає функцію/метод
        self.func = func        # Зберігає посилання на метод
        self.cache = {}         # Словник для зберігання кешованих результатів
    
    def __call__(self, instance, *args, **kwargs):  # Викликається при виклику методу
        # Створюємо ключ для кешу: id екземпляра + аргументи + ключові аргументи
        cache_key = (id(instance), args, tuple(sorted(kwargs.items())))
        
        # Перевіряємо, чи є результат у кеші
        if cache_key in self.cache:
            return self.cache[cache_key]  # Повертаємо кешований результат
        
        # Якщо результату немає в кеші, викликаємо метод і зберігаємо результат
        result = self.func(instance, *args, **kwargs)
        self.cache[cache_key] = result
        return result
    
    def __get__(self, instance, owner):  # Метод для підтримки дескрипторного протоколу
        # Це дозволяє декоратору працювати як метод класу
        if instance is None:
            return self
        # Повертаємо обгортку, яка зберігає посилання на екземпляр
        return partial(self.__call__, instance)

"""3. Створіть класи Book і Library, які будуть взаємодіяти між собою.
Клас Book:
назва  
автор
кількість сторінок
ідентифікатор книги
Методи:
виводити інформацію про книгу

Клас Library:
список книг у бібліотеці
Методи:
використовуйте перевантажені операції:
- додати книгу до бібліотеки 
- видалити книгу за ідентифікатором
шукати книгу за назвою та повертати її інформацію
"""
class Book:  # Клас Book для третього завдання
    def __init__(self, title, author, pages, book_id):  # Конструктор класу Book
        self.title = title          # Назва книги
        self.author = author        # Автор книги
        self.pages = pages          # Кількість сторінок
        self.book_id = book_id      # Ідентифікатор книги
    
    def display_info(self):         # Метод для виведення інформації про книгу
        print(f"ID: {self.book_id}")
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Кількість сторінок: {self.pages}")


class Library:  # Клас Library для управління бібліотекою книг
    def __init__(self):  # Конструктор класу Library
        self.books = []  # Список книг у бібліотеці
    
    def __iadd__(self, book):  # Перевантаження оператора += для додавання книги
        if isinstance(book, Book):  # Перевірка, чи є book екземпляром класу Book
            self.books.append(book)  # Додаємо книгу до списку
            return self  # Повертаємо self для підтримки ланцюгових операцій
        else:
            raise TypeError("Можна додавати тільки об'єкти класу Book")
    
    def __isub__(self, book_id):  # Перевантаження оператора -= для видалення книги за ID
        # Шукаємо книгу з вказаним ідентифікатором
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                del self.books[i]  # Видаляємо книгу зі списку
                return self  # Повертаємо self для підтримки ланцюгових операцій
        # Якщо книга не знайдена, можна викинути виняток або просто повернути self
        print(f"Книга з ID {book_id} не знайдена в бібліотеці")
        return self
    
    def search_by_title(self, title):  # Метод для пошуку книги за назвою
        for book in self.books:  # Перебираємо всі книги в бібліотеці
            if book.title.lower() == title.lower():  # Порівнюємо назви (без урахування регістру)
                return book  # Повертаємо знайдену книгу
        return None  # Якщо книга не знайдена, повертаємо None        

"""4. Облік студентів з файлами

Створіть клас StudentDatabase, який зберігає студентів у файлі.
Клас Student:
ім'я
вік
оцінки

Методи:
повернути середню оцінку

Клас StudentDatabase:
додати студента у файл
зчитати студентів з файлу
знайти студента у файлі
"""
class Student:  # Клас Student для зберігання інформації про студента
    def __init__(self, name, age, grades):  # Конструктор класу Student
        self.name = name        # Ім'я студента
        self.age = age          # Вік студента
        self.grades = grades    # Список оцінок студента
    
    def get_average_grade(self):  # Метод для повернення середньої оцінки
        if not self.grades:  # Якщо список оцінок порожній
            return 0.0  # Повертаємо 0.0
        return sum(self.grades) / len(self.grades)  # Обчислюємо та повертаємо середнє значення
    
    def to_dict(self):  # Метод для перетворення об'єкта в словник (для збереження в JSON)
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }
    
    @classmethod
    def from_dict(cls, data):  # Класовий метод для створення об'єкта зі словника
        return cls(data["name"], data["age"], data["grades"])


class StudentDatabase:  # Клас StudentDatabase для роботи з базою даних студентів у файлі
    def __init__(self, filename="students.json"):  # Конструктор, приймає ім'я файлу
        self.filename = filename  # Зберігаємо ім'я файлу для зберігання даних
    
    def add_student(self, student):  # Метод для додавання студента у файл
        students = self.read_students()  # Зчитуємо всіх студентів з файлу
        students.append(student.to_dict())  # Додаємо нового студента до списку
        # Записуємо оновлений список у файл
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
    
    def read_students(self):  # Метод для зчитування студентів з файлу
        if not os.path.exists(self.filename):  # Перевіряємо, чи існує файл
            return []  # Якщо файл не існує, повертаємо порожній список
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)  # Зчитуємо дані з JSON файлу
        except (json.JSONDecodeError, FileNotFoundError):
            return []  # Якщо помилка читання, повертаємо порожній список
    
    def find_student(self, name):  # Метод для пошуку студента у файлі за ім'ям
        students_data = self.read_students()  # Зчитуємо всіх студентів
        for student_data in students_data:  # Перебираємо студентів
            if student_data["name"].lower() == name.lower():  # Порівнюємо імена (без урахування регістру)
                return Student.from_dict(student_data)  # Повертаємо знайденого студента як об'єкт
        return None  # Якщо студент не знайдений, повертаємо None        