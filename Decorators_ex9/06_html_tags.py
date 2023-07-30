def tags(tag_name):
    def decorator(func):
        def wrapper(*args):
            text = f"<{tag_name}>"
            text += func(*args)
            text += f"</{tag_name}>"
            return text
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
 return text.upper()
print(to_upper('hello'))
