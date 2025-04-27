def decolator_func(fn):
    def wrapper(*args):
        print('start')
        result = fn(*args)
        print('end')
        return result
    return wrapper

@decolator_func
def add_fn(a, b):
    return a + b

@decolator_func
def minus_fn(a, b):
    return a - b


result = add_fn(10, 7)
print(result)

result2 = minus_fn(20, 8)
print(result2)

