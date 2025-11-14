# Кортеж(tuple) – це тип даних, який зберігає впорядкований набір або послідовність елементів.
# Це колекція яка зберігає незмінну(immutable) послідовність елементів. 
my_tuple = (1,2,3,4,5)


# len() - повертає кількість елментів будь-якої послідовності
length=len(my_tuple)
print("Length of tuple:", length)
# З кортежами ми можемо працювати використовуючи індекси
print(my_tuple[0]) # Output: 1

#[start:stop:step] зрізи(slice)
print(my_tuple[::2])

# оборбка елментів кортежу за допомогою циклу
for value in my_tuple:
    print("Value of l2:", value)
    
#range(start, stop, step) - функція яка повертає послідовність чисел у зазначеному діапазоні
for i in range(length):
    print("Index:", i,"Value:",my_tuple[i])
    
# index(value, start, stop) – пошук індекса за значенням
print("Index:",my_tuple.index(3))

# count(value) – повертає кількість повторень значення у кортежі
print("Count:",my_tuple.count(2))

a = 5
b = 2
(a,b)=(b,a)
print(a, b)

    