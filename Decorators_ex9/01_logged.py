def logged(func):
    def wrapper(*args):
        text = f"you called " + f"{func.__name__}{args}"
        text += "\n" + "it returned " f"{func(*args)}"
        return text
    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
