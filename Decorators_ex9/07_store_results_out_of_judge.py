class store_results:

    _results = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        func_result = self.function(*args)
        result_string = f"Function '{self.function.__name__}' was called. Result: {func_result}"
        with open(self._results, "a") as opened_file:
            opened_file.write(result_string + "\n")
        return self.function(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
