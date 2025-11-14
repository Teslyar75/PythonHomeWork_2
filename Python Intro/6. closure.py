"""
- Built-in (print, input)
-- Global 
--- Enclosure
---- Local

"""

x = 10 # global
x = 2.5

def sample():
    x = 5 # local(not global)
    print("Local x: ", x)
    
def changeGlobal():
    global x
    x = 20
    print("Changed X value: ", x)

print("Global x: ", x) # Built-in
sample()
print("Global x: ", x)
changeGlobal()
print("Global x: ", x)

print("\n\n\n\n\n----------------------------------------------\n\n")

def outer_func():
    x = 10
    print("Outer x: ", x)
    def inner_func():
        nonlocal x
        x = 20
        print("Inner x: ",x)
    inner_func()
    print("Outer(again) x: ",x)

outer_func()

def outer(maxValue):
    
    def inner():
        nonlocal maxValue
        maxValue -= 1
        print("Count: ", maxValue)
        
    return inner

inner = outer(10)

inner()
inner()
inner()
inner()
inner()


def make_storage():
    data = []
    
    push_data = lambda value: data.append(value)
    print_data = lambda: print("Storage: ", data)
    def remove_item(item):
        if item in data:
            data.remove(item)
    
    return (push_data, print_data, remove_item)

push, show, remove = make_storage()

push("Hello")
push("world")

show()
remove("Hello")
show()

data = ["Hello"]

def func():
    data.append("World")
    print(data)
    
func()