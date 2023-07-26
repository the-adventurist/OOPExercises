class MyStaticMethod:

    def __init__(self, decorated_method):
        self.decorated_method = decorated_method

    def __get__(self, instance, owner):
        return self.decorated_method

class Dummy:
    @MyStaticMethod
    def a_method_which_is_static(param): # no implicit self
        print(param)

testing = Dummy.a_method_which_is_static("p1")