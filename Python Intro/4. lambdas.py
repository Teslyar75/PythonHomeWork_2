def sample():
    print("Hello, world")
    
sample()

def sample2(a, b):
    return a + b

print(sample2(1,2))

def sample3(a:int, b:int) -> int:
    return a+b

sample3(a=10, b=20)
sample3(1, b=2)

# *args = list, 
# **kwargs(key-word arguments) = dict

def sample4(*args, **kwargs):
    print("Args: ", type(args))
    print("Kwargs: ", type(kwargs))
    for item in args:
        print("Arg: ",item)
        
    for k,v in kwargs.items():
        print(f"kwarg: {k}|{v}")
    
sample4(1,"Hello",3,4,[5,6,7], name='Joe', surname='Due', d={"key1":"value1", "key2":'value2'})
sample4(1,*"Hello",3,4,*[5,6,7], name='Joe', surname='Due', **{"key1":"value1", "key2":'value2'})


def sum(*args,**kwargs):
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print("Key: ",key, "Value",value)

sum(1,2,3,4,5,6, name="Ivan",age=18)


# create lambda
greeting = lambda :print("hello")

greeting() # Output: hello

def greeting():
    print("Hello")

greeting()
# lambda as param
def operation(value1,value2, operation):
    return operation(value1, value2)

print(operation(12,10,lambda x, y: x+y))

# return lambda
def selectOperation(operation):
    if operation=="sum":
        return lambda x, y: x+y
    if operation=="dif":
        return lambda x, y: x+y
    
operation = selectOperation("sum")
print(operation(12,10))

# sort, sorted, map, filter

l = [1,2,3,4,5,6,7,8,9,10]

# sort(key=func, reverse=True|False)

l.sort(key=lambda x:x%2==0, reverse=True)
print(l)

l3 = list("Hello")
print(l3)
# map(func, iterable)
l2 = list(map(lambda x :x**2,l))
print(l2)

# sorted(iterable, func, reverse=True|False)
l = [1,2,3,4,5,6,7,8,9,10]
print(sorted(l,key=lambda x:x%2==0, reverse=False))

# filter()
print(list(
    filter(lambda x:x%2==0,l)
))



