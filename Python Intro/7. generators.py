# l = [1,2,3,4,5]

# list_iter = iter(l);
# """
# __next__()

# __getitem__
# __iter__
# """

# for item in l:
#     print(item)

# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))

print("Example generator: ")

def counter(stop):
    counter = 0
    for _ in range(stop):
        counter+=1
    return counter

print("Counter result: ", counter(10))

def generate():
    item = 0
    while True:
        item += 1
        yield item ** 2

g = generate()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def fibo():
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

print("Fibonacci generator")

fg = fibo()
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))


"""
def loadProducts():
    productList = cursor.from_query("SELECT * FROM products")
    return productList
    
loadProducts() -> returns : [{Product1Obj}, {Product2Obj}...{ProductNObj}]

def generateProducts():
    with cursor:
        for item in cursor.from_query("SELECT * FROM products"):
            yield item

g = generateProducts()

next(g) -> returns: {ProductObj1}
next(g) -> returns: {ProductObj2}
...
next(g) -> returns: {ProductObjN}

"""

import os
def read_file_generator(filepath:str):
    with open(filepath, 'r') as file:
        for line in file:
            yield line[0:3]
            

fileLinesGenerate = read_file_generator("file.txt")
print(next(fileLinesGenerate))


print(next(fileLinesGenerate))

fileLinesGenerate.send("SendData")
print(next(fileLinesGenerate))

g = (x ** 2 for x in range(20) if x%2 == 0)

# for item in g:
#     print(item)

def sendExample():
    print("Generator started")
    value = yield "Init value"
    print(f"Generator recieved: {value}")
    yield "Generator finished"
    
g = sendExample()
print(next(g))
g.send("First message")
print(next(g))