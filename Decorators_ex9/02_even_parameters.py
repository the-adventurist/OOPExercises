def even_parameters(function):
    def wrapper(*args):
        if not args:
            return function()
        for el in args:
            if isinstance(el, str):
                return "Please use only even numbers!"
        odd_numbers = [x for x in args if x % 2 == 1]
        if not odd_numbers:
            return function(*args)
        else:
            return "Please use only even numbers!"
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))