set1 = set() # create set.
set1 = {2,3,4,5} # create set

print(set1)
set2 = {6,7,8,9}
# методи set

# union(iterable) чи set1 | set2 – об’єднання множин
union = set1.union(set2)
union = set1 | set2
print(union) # Output: {1,2,3,4,5,6,7,8,9}

# intersection(iterable) чи set1 & set2 – перетин множин
print(set1.intersection({1,2,3,4,5,6,7,8})) # Output: {1,2,3,4,5}

# difference(iterable) чи set1 - set2 – різниця множин
print(set1.difference({4,5,6,7,8})) # Output: {1,2,3}

# symetric_difference(iterable) чи set1 ^ set2 – різниця множин
print(set1.symmetric_difference({4,5,6,7,8})) # Output: {1,2,3,6,7,8}

# isdisjoint(iterable) – перевіряє чи немає у множин спільних елементів
print(set1.isdisjoint(set2)) # Output: True

# issubset(iterable) – перевіряє чи є одна множина підмножиною іншої
print(set1.issubset({1,2,3,4,5})) # Output: False

# issuperset(iterable) – перевіряє чи є одна множина надмножиною іншої
print(set1.issuperset(set2)) # Output: False

# add(value) – додає новий елемент у множину
set1.add(6)
print(set1) # Output: {1, 2, 3, 4, 5, 6}

# remove(value), discard(value) – видаляє елемент з множини
set1.remove(6)
#set1.remove(6)# error KeyError: 6
set1.discard(6)
print(set1) # Output: {1, 2, 3, 4, 5}

# clear() – очищення множини
set1.clear()
print(set1)

