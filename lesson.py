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


result = add_fn(10, 7)
print(result)

