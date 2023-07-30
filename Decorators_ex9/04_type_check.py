def type_check(type_):
    def decorator(function):
        def wrapper(*args):
            if isinstance(args[0], type_):
                result = function(*args)
            else:
                result = "Bad Type"
            return result
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
