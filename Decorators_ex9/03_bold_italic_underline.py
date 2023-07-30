def make_bold(function):
    def wrapper(*args):
        text = "<b>"
        text += function(*args)
        text += "</b>"
        return text
    return wrapper


def make_italic(function):
    def wrapper(*args):
        text = "<i>"
        text += function(*args)
        text += "</i>"
        return text
    return wrapper


def make_underline(function):
    def wrapper(*args):
        text = "<u>"
        text += function(*args)
        text += "</u>"
        return text
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
