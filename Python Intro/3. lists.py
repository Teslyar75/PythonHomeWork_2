import random

variable = 12

print("Variable: ", variable)
print("Typeof variable: ", type(variable))

variable = 'Hello'

print("Variable: ", variable)
print("Typeof variable: ", type(variable))

condition = False


# if condition is True:
if condition:
    print("Condition is True")
else:
    print("Condition is False")

rand_value = random.randint(-10, 20)
print("Random value: ", rand_value)

if rand_value < 0:
    print("value lt 0")
elif rand_value > 0 and rand_value < 10:
    print("value gt 0 and lt 10")
else:
    print("value gt 10")

print("Variable, rand_value: ",variable, rand_value, sep="|", end=" ")
print("Sample")

# comment

"""
int - 1,2,3,4,5
float - 1.5, 10.2351, 3.14
bool - True, False
str - "Hello", 'world'
"""

# print("Your number^2: ",int(input("Enter number: ")) **2)


# Списки це тип даних, який зберігає впорядкований набір або послідовність елементів. 
# Список може зберігати як і однотипні елементи так і елементи різних типів.

l1 = list() # створення пустого списку
l2 = [1,2,3,4,5] # створення списку з елментами

# len() - повертає кількість елментів будь-якої послідовності
length=len(l2)
print("Length of l2:", length)
# Зі списками ми можемо працювати використовуючи індекси
print("Element: ",l2[-2]) # Output: 1

#[start:stop:step] зрізи(slice)

print(l2[::-1])

# оборбка елментів списку за допомогою циклу
for value in l2:
    print("Value of l2:", value)
    
#range(start, stop, step) - функція яка повертає послідовність чисел у зазначеному діапазоні
for i in range(length):
    print("Index:", i,"Value:",l2[i])

# Методи списку
# append(value) – додає новий елемент в кінець
l1.append("Hello")
print(l1)

# reverse() змінює порядок елементів на протилежний
print(l2) # Output: [1,2,3,4,5]
l2.reverse()
print(l2) # Output: [5,4,3,2,1]

# extend(iterable) – додає до існуючих елементів нові з будь-якої послідовності 
l2.extend("Hello")
print(l2)

# pop(index_optional) – видаляє елемент зі списку попередньо повернувши його
element = l2.pop()
print(element)
print(l2)

# insert(index, value) – вставка елемента по індексу
l2.insert(5,"K")
print(l2)

# index(value, start, stop) – пошук індекса за значенням
print("Index:",l2.index("K"))

# count(value) – повертає кількість повторень значення у списку
print("Count: ",l2.count("l"))

# copy() – створює копію списку та повертає її
newList = l2.copy()
print(newList)

# reverse() – змінює послідовність елементів на протилежну
l2.reverse()
print(l2)
print(l2[::-1])

# clear() – очищує список
l2.clear()
print(l2)

# remove(value) – видаляє перший знайдений елемент
newList.remove("l")
print(newList)
